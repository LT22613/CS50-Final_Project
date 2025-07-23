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

# --------------------------
# INITIALISATION TESTS
# --------------------------

def test_warrior_init():
    """Verify Warrior starts with correct stats."""
    warrior = Warrior("Dylan")
    assert warrior.health == 100
    assert warrior.power == 20
    assert warrior.defence == 10
    assert warrior.stealth == 6
    assert warrior.accuracy == 7

def test_mage_init():
    """Ensure Mage initializes with correct base stats."""
    mage = Mage("Claire")
    assert mage.health == 75
    assert mage.power == 25
    assert mage.defence == 7
    assert mage.stealth == 8
    assert mage.accuracy == 8

def test_archer_init():
    """Verify Archer starts with correct attributes."""
    Craig = Archer("Craig")
    assert Craig.name == "Craig"
    assert Craig.max_health == 50
    assert Craig.power == 15
    assert Craig.health == 50
    assert Craig.defence == 5
    assert Craig.stealth == 10
    assert Craig.accuracy == 9

def test_monster_init():
    """Verify that Monster starts with attributes in the correct range."""
    for _ in range(100):
        random.seed(_)
        Blob = Monster("Blob")
        assert Blob.name == "Blob"
        assert 40 <= Blob.max_health <= 80
        assert 5 <= Blob.defence <= 9
        assert 5 <= Blob.stealth <= 9
        assert 5 <= Blob.power <= 15

def test_HealingPotion_init():
    """Verify that Healing Potion starts with correct attributes."""
    potion = HealingPotion()
    assert potion.num_uses == 5
    assert potion.effect == 20
    
def test_chest_init():
    """Verify that Chest starts with correct attribute
    """
    chest = TreasureChest(100)
    assert chest.num_of_coins == 100

# --------------------------
# ATTRIBUTE SETTER TESTS
# --------------------------

def test_mage_health_clamping():
    """Ensure Mage health doesn’t exceed max_health."""
    mage = Mage("Dean")
    mage.health += 20
    assert mage.health == 75

def test_mage_accuracy_limits():
    """Check Mage accuracy clamps to 30 and raises on invalid input."""
    mage = Mage("Shaun")
    mage.accuracy = 40
    assert mage.accuracy == 10

    mage = Mage("Dylan")
    with pytest.raises(ValueError):
        mage.accuracy = "a"

def test_mage_defence_limits():
    """Ensure Mage defence stays between 0 and 30."""
    mage = Mage("Lily")
    mage.defence = 40
    assert mage.defence == 10
    mage.defence = -10
    assert mage.defence == 0
    mage.defence = 5
    assert mage.defence == 5

def test_mage_stealth_limits():
    """Ensure Mage stealth stays between 0 and 30."""
    mage = Mage("Snape")
    mage.stealth = 40
    assert mage.stealth == 10
    mage.stealth = -10
    assert mage.stealth == 0
    mage.stealth = 10
    assert mage.stealth == 10
    mage.stealth = 0
    assert mage.stealth == 0
    mage.stealth = 5
    assert mage.stealth == 5

# --------------------------
# METHOD BEHAVIOUR TESTS
# --------------------------

def test_warrior_pouch():
    """Test that the Warrior’s pouch behaves as expected."""
    warrior = Warrior("Lucifer")
    warrior.pouch["Healing Potion"] = 2
    assert warrior.pouch == {"Healing Potion": 2}

def test_heal_with_potion():
    """
    Ensure that using a HealingPotion increases the character's health
    and reduces the number of potion uses.
    """
    potion = HealingPotion()
    Claire = Warrior("Claire")
    Claire.health = 50
    Claire.pouch[potion] = 1
    Claire.heal()
    assert Claire.health == 70
    assert potion.num_uses == 4

def test_heal_without_potion(capsys):
    """Test that a warning is printed if no healing potion is available."""
    Dean = Warrior("Dean")
    Dean.heal()
    captured = capsys.readouterr()
    assert captured.out.strip() == "You do not have a healing potion."

def test_empty_chest():
    """Check that coins from a TreasureChest are added to the pouch."""
    chest = TreasureChest(100)
    Char_3 = Warrior("Damian")
    Char_3.empty_chest(chest)
    assert Char_3.pouch["coins"] == 100

def test_dodge_chance_warrior():
    """
    Test that a Warrior's dodge chance is calculated correctly.

    The formula is (stealth * defence) / 100.
    For a Warrior with default stealth=5 and defence=12, dodge chance = 0.6.
    """
    warrior = Warrior("Dennis")
    assert warrior.dodge_chance() == 0.6


def test_dodge_chance_mage():
    """
    Test that a Mage's dodge chance is calculated correctly.

    Default stats: stealth=10, defence=15 → dodge chance = 0.56
    """
    mage = Mage("Daisy")
    assert mage.dodge_chance() == 0.56


def test_dodge_chance_archer():
    """
    Test that an Archer's dodge chance is calculated correctly.

    Default stats: stealth=20, defence=10 → dodge chance = 0.5
    """
    archer = Archer("Dart")
    assert archer.dodge_chance() == 0.5


def test_dodge_chance_monster():
    """
    Test that a Monster's dodge chance is computed correctly
    based on its randomly assigned stealth and defence stats.
    """
    monster = Monster("Mawg")
    expected = (monster.stealth * monster.defence) / 100
    assert monster.dodge_chance() == expected


def test_hit_chance_warrior():
    """
    Test hit chance values for a Warrior attacking three different Monsters.
    The expected values are precomputed using known enemy stats (seeded randomness).
    """
    warrior = Warrior("Arthur")
    enemy_1 = Monster("Argie", random.seed(1))
    enemy_2 = Monster("Bleurgh", random.seed(2))
    enemy_3 = Monster("Coral", random.seed(3))
    assert round(warrior.hit_chance(enemy_1), 3) == 0.455
    assert round(warrior.hit_chance(enemy_2), 3) == 0.525
    assert round(warrior.hit_chance(enemy_3), 3) == 0.406


def test_hit_chance_mage():
    """
    Test hit chance values for a Mage attacking three different Monsters.
    Mage has higher accuracy, so results should be higher than Warrior's.
    """
    mage = Mage("Henry")
    enemy_1 = Monster("Argie", random.seed(1))
    enemy_2 = Monster("Bleurgh", random.seed(2))
    enemy_3 = Monster("Coral", random.seed(3))
    assert round(mage.hit_chance(enemy_1), 3) == 0.520
    assert round(mage.hit_chance(enemy_2), 3) == 0.600
    assert round(mage.hit_chance(enemy_3), 3) == 0.464


def test_hit_chance_archer():
    """
    Test hit chance values for an Archer attacking three different Monsters.
    Archer has high accuracy, expected to have the best hit rates.
    """
    archer = Archer("Shooter")
    enemy_1 = Monster("Argie", random.seed(1))
    enemy_2 = Monster("Bleurgh", random.seed(2))
    enemy_3 = Monster("Coral", random.seed(3))
    assert round(archer.hit_chance(enemy_1), 3) == 0.585
    assert round(archer.hit_chance(enemy_2), 3) == 0.675
    assert round(archer.hit_chance(enemy_3), 3) == 0.522


def test_attack_warrior(capsys):
    """
    Test the Warrior's attack outcomes and their corresponding messages.
    
    Simulates attacks on 3 monsters with seeded randomness.
    Captures printed output to assert expected hit quality message.
    """
    warrior = Warrior("Dave")
    
    enemy_1 = Monster("Argie", random.seed(1))
    warrior.attack(enemy_1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Your low accuracy caused you to deal reduced damage"

    enemy_2 = Monster("Bleurgh", random.seed(2))
    warrior.attack(enemy_2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Your accuracy enabled you to deal regular damage"

    enemy_3 = Monster("Coral", random.seed(3))
    warrior.attack(enemy_3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Your low accuracy caused you to deal reduced damage"
    
def test_str(capsys):
    warrior_1 = Warrior("Bob")
    print(warrior_1)
    captured = capsys.readouterr()
    assert captured.out.strip() == f"{warrior_1.name} is a mighty warrior with 100 life points!"


    
