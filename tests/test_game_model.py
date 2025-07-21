from game_model import *


def test_Character_1():
    """Tests basic features of a Character object."""
    Char_1 = Character("Bob")
    assert Char_1.name == "Bob"
    assert Char_1.pouch == {}


def test_Character_2():
    """Checks that the pouch of a Character object works as expected."""
    Char_2 = Character("Chloe")
    Char_2.pouch["Healing Potion"] = 1
    assert Char_2.name == "Chloe"
    assert Char_2.pouch == {"Healing Potion": 1}


def test_Character_3():
    """Tests that a Character object empties a Treasure_Chest object correctly"""
    chest = Treasure_Chest(100)
    assert chest.num_of_coins == 100
    Char_3 = Character("Damian")
    Char_3.empty_chest(chest)
    assert Char_3.pouch["coins"] == 100


def test_Warrior_1():
    """Tests the basic features of a Warrior object"""
    Warrior_1 = Warrior("Dylan")
    assert Warrior_1.health == 100
    assert Warrior_1.power == 20
    assert Warrior_1.health == 100
    assert Warrior_1.defence == 20
    assert Warrior_1.stealth == 5


def test_Warrior_2():
    """Tests the pouch feature of a Warrior object"""
    Warrior_2 = Warrior("Lucifer")
    Warrior_2.pouch["Healing Potion"] = 2
    assert Warrior_2.pouch == {"Healing Potion": 2}


def test_Mage_1():
    """Tests the basic features of a Mage object"""
    Mage_1 = Mage("Claire")
    Mage.health = 75
    Mage.power = 25
    Mage.defence = 15
    Mage.stealth = 10
    Mage.accuracy = 15


def test_Mage_2():
    """Tests the methods a Mage object has."""
    Mage_2 = Mage("Serena")
    Mage_2.health = 95
    assert Mage_2.health == 75