from typing import Optional

import pytest

from topdrawersoccer.extractors.transfer_extractor import TransferExtractor, get_position, get_name


@pytest.mark.parametrize("name_field, expected_position", [
    ("", None),
    ("F Desiree Foster", "F"),
    ("F/D Nina Norshie", "F/D"),
    ("D Remini Tillotson", "D"),
    ("M Emily Mathews", "M"),
    ("GK Azul Alvarez", "GK"),
    ("D/M Zoe Lam", "D/M"),
    ("F Vivian Akyirem", "F")
])
def test_get_position(name_field: str, expected_position: Optional[str]):
    actual_position = get_position(name_field)

    assert actual_position == expected_position, f"Expected position: '{expected_position}' got '{actual_position}'"


@pytest.mark.parametrize("name_field, expected_name", [
    ("", ""),
    ("F Desiree Foster", "Desiree Foster"),
    ("F/D Nina Norshie", "Nina Norshie"),
    ("D Remini Tillotson", "Remini Tillotson"),
    ("M Emily Mathews", "Emily Mathews"),
    ("GK Azul Alvarez", "Azul Alvarez"),
    ("D/M Zoe Lam", "Zoe Lam"),
])
def test_get_name(name_field: str, expected_name: Optional[str]):
    actual_name = get_name(name_field)

    assert actual_name == expected_name, f"Expected name: '{expected_name}' got '{actual_name}'"
