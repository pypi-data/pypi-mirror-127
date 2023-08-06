import copy
from pathlib import Path
from typing import List, Dict, Text, Any, Tuple, Optional, Union

import rasa.shared.utils.io
import rasa.shared.utils.cli
from rasa.shared.constants import (
    REQUIRED_SLOTS_KEY,
    IGNORED_INTENTS,
)
from rasa.shared.core.constants import ACTIVE_LOOP, REQUESTED_SLOT
from rasa.shared.core.domain import (
    KEY_ENTITIES,
    KEY_SLOTS,
    KEY_FORMS,
    Domain,
)
from rasa.shared.core.slot_mappings import SlotMapping
from rasa.shared.exceptions import RasaException


def _create_back_up(
    domain_file: Path, backup_location: Path
) -> Union[List[Any], Dict[Text, Any]]:
    original_content = rasa.shared.utils.io.read_yaml_file(domain_file)
    rasa.shared.utils.io.write_yaml(original_content, backup_location, True)
    return original_content


def _update_mapping_condition(
    condition: Dict[Text, Text], mapping: Dict[Text, Any], slot_name: Text
) -> Dict[Text, Text]:
    if mapping.get("type") not in [
        str(SlotMapping.FROM_ENTITY),
        str(SlotMapping.FROM_TRIGGER_INTENT),
    ]:
        condition.update({REQUESTED_SLOT: slot_name})
    return condition


def _get_updated_or_new_mappings(
    existing_mappings: List[Dict[Text, Any]],
    new_mappings: List[Dict[Text, Any]],
    condition: Dict[Text, Text],
    slot_name: Text,
) -> List[Dict[Text, Any]]:
    updated_mappings = []

    for existing_mapping in existing_mappings:
        mapping_copy = copy.deepcopy(existing_mapping)

        conditions = existing_mapping.pop("conditions", [])
        if existing_mapping in new_mappings:
            new_mappings.remove(existing_mapping)

            updated_condition = _update_mapping_condition(
                condition, existing_mapping, slot_name
            )

            conditions.append(updated_condition)
            existing_mapping.update({"conditions": conditions})
            updated_mappings.append(existing_mapping)
        else:
            updated_mappings.append(mapping_copy)

    for mapping in new_mappings:
        updated_condition = _update_mapping_condition(condition, mapping, slot_name)
        mapping.update({"conditions": [updated_condition]})
        updated_mappings.append(mapping)

    return updated_mappings


def _migrate_form_slots(
    domain: Dict[Text, Any]
) -> Tuple[Dict[Any, Dict[str, Any]], Optional[Any]]:
    updated_slots = domain.get(KEY_SLOTS, {})
    forms = domain.get(KEY_FORMS, {})

    new_forms = {}

    for form_name, form_data in forms.items():
        ignored_intents = form_data.pop(IGNORED_INTENTS, [])
        if REQUIRED_SLOTS_KEY in form_data:
            form_data = form_data.get(REQUIRED_SLOTS_KEY, {})

        required_slots = []

        for slot_name, mappings in form_data.items():
            condition = {ACTIVE_LOOP: form_name}
            slot_properties = updated_slots.get(slot_name, {})
            existing_mappings = slot_properties.get("mappings", [])
            updated_mappings = _get_updated_or_new_mappings(
                existing_mappings, mappings, condition, slot_name
            )
            slot_properties.update({"mappings": updated_mappings})
            updated_slots[slot_name] = slot_properties

            required_slots.append(slot_name)

        new_forms[form_name] = {
            IGNORED_INTENTS: ignored_intents,
            REQUIRED_SLOTS_KEY: required_slots,
        }
    return new_forms, updated_slots


def _migrate_auto_fill(
    slot_name: Text, properties: Dict[Text, Any], entities: List[Text],
) -> Dict[Text, Any]:
    if slot_name in entities and properties.get("auto_fill", True) is True:
        from_entity_mapping = {
            "type": str(SlotMapping.FROM_ENTITY),
            "entity": slot_name,
        }
        mappings = properties.get("mappings", [])
        if from_entity_mapping not in mappings:
            mappings.append(from_entity_mapping)
            properties.update({"mappings": mappings})

    if "auto_fill" in properties:
        del properties["auto_fill"]

    return properties


def _migrate_custom_slots(
    slot_name: Text, properties: Dict[Text, Any]
) -> Dict[Text, Any]:
    if not properties.get("mappings"):
        properties.update({"mappings": [{"type": "custom"}]})

        rasa.shared.utils.io.raise_warning(
            f"A custom mapping was added to slot '{slot_name}'. "
            f"Please double-check this is correct.",
            UserWarning,
        )

    return properties


def _migrate_auto_fill_and_custom_slots(
    domain: Dict[Text, Any], slots: Dict[Text, Any]
) -> Dict[Text, Any]:
    new_slots = {}
    entities = domain.get(KEY_ENTITIES, [])

    for slot_name, properties in slots.items():
        updated_properties = _migrate_auto_fill(slot_name, properties, entities)
        updated_properties = _migrate_custom_slots(slot_name, updated_properties)

        new_slots[slot_name] = updated_properties
    return new_slots


def _assemble_new_domain(
    domain_file: Path, new_forms: Dict[Text, Any], new_slots: Dict[Text, Any]
) -> Dict[Text, Any]:
    original_content = rasa.shared.utils.io.read_yaml_file(domain_file)
    new_domain = {}
    for key, value in original_content.items():
        if key == KEY_SLOTS:
            new_domain.update({key: new_slots})
        elif key == KEY_FORMS:
            new_domain.update({key: new_forms})
        else:
            new_domain.update({key: value})
    return new_domain


def _write_final_domain(
    domain_file: Path, new_forms: Dict, new_slots: Dict, out_file: Path,
) -> None:
    if domain_file.is_dir():
        for file in domain_file.iterdir():
            new_domain = _assemble_new_domain(file, new_forms, new_slots)
            rasa.shared.utils.io.write_yaml(new_domain, out_file / file.name, True)
    else:
        new_domain = _assemble_new_domain(domain_file, new_forms, new_slots)
        rasa.shared.utils.io.write_yaml(new_domain, out_file, True)


def migrate_domain_format(
    domain_file: Union[Text, Path], out_file: Union[Text, Path]
) -> None:
    """Converts 2.0 domain to 3.0 format."""
    domain_file = Path(domain_file)
    out_file = Path(out_file)

    current_dir = domain_file.parent

    if domain_file.is_dir():
        backup_dir = current_dir / "original_domain"
        backup_dir.mkdir()

        slots = {}
        forms = {}
        entities = []
        original_domain = {}

        if out_file.is_file() or not out_file.exists():
            out_file = current_dir / "new_domain"
            out_file.mkdir()
            rasa.shared.utils.io.raise_warning(
                f"The out path provided is not a directory, "
                f"creating a new directory '{str(out_file)}' "
                f"for migrated domain files."
            )

        for file in domain_file.iterdir():
            if not Domain.is_domain_file(file):
                continue

            backup = backup_dir / file.name
            original_content = _create_back_up(file, backup)

            if KEY_SLOTS not in original_content and KEY_FORMS not in original_content:
                # this is done so that the other domain files can be moved
                # in the migrated directory
                rasa.shared.utils.io.write_yaml(
                    original_content, out_file / file.name, True
                )
            elif KEY_SLOTS in original_content and slots:
                raise RasaException(
                    f"Domain files with multiple '{KEY_SLOTS}' "
                    f"sections were provided. Please group these sections "
                    f"in one file only to prevent content duplication across "
                    f"multiple files. "
                )
            elif KEY_FORMS in original_content and forms:
                raise RasaException(
                    f"Domain files with multiple '{KEY_FORMS}' "
                    f"sections were provided. Please group these sections "
                    f"in one file only to prevent content duplication across "
                    f"multiple files. "
                )

            slots.update(original_content.get(KEY_SLOTS, {}))
            forms.update(original_content.get(KEY_FORMS, {}))
            entities.extend(original_content.get(KEY_ENTITIES, {}))

        if not slots or not forms:
            raise RasaException(
                f"The files you have provided in '{domain_file}' are missing slots "
                f"or forms. Please make sure to include these for a "
                f"successful migration."
            )

        original_domain.update(
            {KEY_SLOTS: slots, KEY_FORMS: forms, KEY_ENTITIES: entities}
        )
    else:
        if not Domain.is_domain_file(domain_file):
            raise RasaException(
                f"The file '{domain_file}' could not be validated as a "
                f"domain file. Only domain yaml files can be migrated. "
            )

        backup = current_dir / "original_domain.yml"
        original_domain = _create_back_up(domain_file, backup)

    new_forms, updated_slots = _migrate_form_slots(original_domain)
    new_slots = _migrate_auto_fill_and_custom_slots(original_domain, updated_slots)

    _write_final_domain(domain_file, new_forms, new_slots, out_file)

    rasa.shared.utils.cli.print_success(
        f"Your domain was successfully migrated! It's location is {out_file}."
    )
