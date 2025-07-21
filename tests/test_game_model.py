"""
test_game_model.py

This test suite verifies the behavior of game objects defined in game_model.py.

The focus is on testing:
- Proper instantiation and attribute handling of characters and subclasses
- Health system logic (including healing with potions and health clamping)
- Pouch and inventory behavior
- Special object behaviors (e.g., treasure chest, potion usage)
"""

from game_model import *
import pytest


def test_character_initialises_with_name_and_empty_pouch():
    """Ensure Character objects initialize correctly with name and empty pouch."""
    Char_1 = Character("Bob")
    assert Char_1.name == "Bob"
    assert Char_1.pouch == {}


def test_character_pouch_can_store_items():
    """Verify that the Character's pouch can store and retrieve items properly."""
    Char_2 = Character("Chloe")
    Char_2.pouch["Healing Potion"] = 1
    assert Char_2.pouch == {"Healing Potion": 1}


def test_healing_potion_heals_character_and_decrements_uses():
    """
    Ensure that using a Healing_Potion increases the character's health
    (up to max_health) and reduces the number of potion uses.
    """
    potion = Healing_Potion()
    Claire = Character("Claire")
    Claire.health = 50
    Claire.pouch[potion] = 1
    Claire.heal()
    assert Claire.health == 70
    assert potion.num_uses == 4


def test_heal_without_potion_prints_warning(capsys):
    """
    Test that the Character receives a warning message when trying to heal
    without a healing potion in their pouch.
    """
    Dean = Character("Dean", 100)
    Dean.heal()
    captured = capsys.readouterr()
    assert captured.out.strip() == "You do not have a healing potion."


def test_character_empties_treasure_chest_correctly():
    """
    Confirm that emptying a Treasure_Chest correctly adds coins to the
    Character's pouch.
    """
    chest = Treasure_Chest(100)
    Char_3 = Character("Damian")
    Char_3.empty_chest(chest)
    assert Char_3.pouch["coins"] == 100


def test_warrior_initial_attributes():
    """
    Ensure that a Warrior initializes with the correct predefined stats.
    """
    warrior = Warrior("Dylan")
    assert warrior.health == 100
    assert warrior.power == 20
    assert warrior.defence == 20
    assert warrior.stealth == 5


def test_warrior_pouch_stores_items_correctly():
    """Check that the Warrior's pouch behaves like a standard dictionary."""
    warrior = Warrior("Lucifer")
    warrior.pouch["Healing Potion"] = 2
    assert warrior.pouch == {"Healing Potion": 2}


def test_mage_initial_attributes():
    """
    Ensure Mage is initialized with correct base stats for health, power,
    defence, stealth, and accuracy.
    """
    mage = Mage("Claire")
    assert mage.health == 75
    assert mage.power == 25
    assert mage.defence == 15
    assert mage.stealth == 10
    assert mage.accuracy == 15


def test_mage_health_does_not_exceed_max():
    """
    Test that the health setter prevents Mage health from exceeding max_health.
    """
    mage = Mage("Dean")
    mage.health += 20
    assert mage.health == 75


def test_mage_accuracy_clamps_to_max_and_raises_on_invalid_type():
    """
    Ensure Mage accuracy clamps to 30 when set too high,
    and raises an error if set to a non-numeric value.
    """
    mage = Mage("Shaun")
    mage.accuracy = 40
    assert mage.accuracy == 30

    mage = Mage("Dylan")
    with pytest.raises(ValueError):
        mage.accuracy = "a"


def test_mage_defence_clamps_within_bounds():
    """
    Test that Mage defence is clamped between 0 and 30 when set out of range.
    """
    mage = Mage("Lily")
    mage.defence = 40
    assert mage.defence == 30
    mage.defence = -10
    assert mage.defence == 0
    mage.defence = 5
    assert mage.defence == 5


def test_mage_stealth_clamps_within_bounds():
    """
    Test that Mage stealth is clamped between 0 and 30 when set out of range.
    """
    mage = Mage("Snape")
    mage.stealth = 40
    assert mage.stealth == 30
    mage.stealth = -10
    assert mage.stealth == 0
    mage.stealth = 30
    assert mage.stealth == 30
    mage.stealth = 0
    assert mage.stealth == 0
    mage.stealth = 5
    assert mage.stealth == 5
    

