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


def test_character_init():
    """Ensure Character objects initialize correctly with name and empty pouch."""
    Char_1 = Character("Bob")
    assert Char_1.name == "Bob"
    assert Char_1.pouch == {}


def test_character_pouch():
    """Verify that the Character's pouch can store and retrieve items properly."""
    Char_2 = Character("Chloe")
    Char_2.pouch["Healing Potion"] = 1
    assert Char_2.pouch == {"Healing Potion": 1}


def test_heal_with_potion():
    """
    Ensure that using a Healing_Potion increases the character's health
    and reduces the number of potion uses.
    """
    potion = Healing_Potion()
    Claire = Character("Claire")
    Claire.health = 50
    Claire.pouch[potion] = 1
    Claire.heal()
    assert Claire.health == 70
    assert potion.num_uses == 4


def test_heal_without_potion(capsys):
    """Test that a warning is printed if no healing potion is available."""
    Dean = Character("Dean", 100)
    Dean.heal()
    captured = capsys.readouterr()
    assert captured.out.strip() == "You do not have a healing potion."


def test_empty_chest():
    """Check that coins from a Treasure_Chest are added to the pouch."""
    chest = Treasure_Chest(100)
    Char_3 = Character("Damian")
    Char_3.empty_chest(chest)
    assert Char_3.pouch["coins"] == 100


def test_warrior_stats():
    """Verify Warrior starts with correct stats."""
    warrior = Warrior("Dylan")
    assert warrior.health == 100
    assert warrior.power == 20
    assert warrior.defence == 20
    assert warrior.stealth == 5


def test_warrior_pouch():
    """Test that the Warrior’s pouch behaves as expected."""
    warrior = Warrior("Lucifer")
    warrior.pouch["Healing Potion"] = 2
    assert warrior.pouch == {"Healing Potion": 2}


def test_mage_stats():
    """Ensure Mage initializes with correct base stats."""
    mage = Mage("Claire")
    assert mage.health == 75
    assert mage.power == 25
    assert mage.defence == 15
    assert mage.stealth == 10
    assert mage.accuracy == 15


def test_mage_health_clamping():
    """Ensure Mage health doesn’t exceed max_health."""
    mage = Mage("Dean")
    mage.health += 20
    assert mage.health == 75


def test_mage_accuracy_limits():
    """Check Mage accuracy clamps to 30 and raises on invalid input."""
    mage = Mage("Shaun")
    mage.accuracy = 40
    assert mage.accuracy == 30

    mage = Mage("Dylan")
    with pytest.raises(ValueError):
        mage.accuracy = "a"


def test_mage_defence_limits():
    """Ensure Mage defence stays between 0 and 30."""
    mage = Mage("Lily")
    mage.defence = 40
    assert mage.defence == 30
    mage.defence = -10
    assert mage.defence == 0
    mage.defence = 5
    assert mage.defence == 5


def test_mage_stealth_limits():
    """Ensure Mage stealth stays between 0 and 30."""
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

def test_archer_init():
    Craig = Archer("Craig")
    assert Craig.name == "Craig"
    assert Craig.max_health == 50
    assert Craig.health == 50
    assert Craig.defence == 10
    assert Craig.stealth == 20
    assert Craig.power == 15
    assert Craig.accuracy == 20

def test_monster_init():
    for _ in range(100):
        random.seed(_)
        Blob = Monster("Blob")
        assert Blob.name == "Blob"
        assert 40 <= Blob.max_health <= 80
        assert 5 <= Blob.defence <= 9
        assert 5 <= Blob.stealth <= 9
        assert 5 <= Blob.power <= 15
        
def test_healing_potion_init():
    Potion = Healing_Potion()
    assert Potion.num_uses == 5
    assert Potion.effect == 20
    

        