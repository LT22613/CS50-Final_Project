import pytest
from game_interface import Game, QuitGameException
from game_model import Warrior, Monster, TreasureChest, HealingPotion, Shopkeeper

@pytest.fixture
def basic_game():
    """Create a basic 3x3 game setup for testing."""
    hero = Warrior("TestHero")
    grid = [[None for _ in range(3)] for _ in range(3)]
    return Game(hero, grid)

def test_game_initialization(basic_game):
    """Test game initializes with correct attributes."""
    assert basic_game.hero.name == "TestHero"
    assert basic_game.hero_position == (0, 0)
    assert len(basic_game.grid) == 3
    assert len(basic_game.grid[0]) == 3

def test_move_hero_valid(basic_game, monkeypatch, capsys):
    """Test hero movement within valid grid bounds."""
    # Simulate user input for moving right
    monkeypatch.setattr('builtins.input', lambda _: "right")
    basic_game.move_hero()
    
    assert basic_game.hero_position == (0, 1)
    captured = capsys.readouterr()
    assert "Yay! No scary monsters here." in captured.out

def test_move_hero_invalid(basic_game, monkeypatch, capsys):
    """Test hero movement outside grid bounds."""
    # Simulate user input for moving up (invalid from 0,0)
    monkeypatch.setattr('builtins.input', lambda _: "up")
    basic_game.move_hero()
    
    assert basic_game.hero_position == (0, 0)  # Position shouldn't change
    captured = capsys.readouterr()
    assert "You can't move that way!" in captured.out

def test_encounter_monster(basic_game, monkeypatch, capsys):
    """Test monster encounter in game turn."""
    # Place monster in adjacent cell
    monster = Monster("TestMonster")
    basic_game.grid[0][1] = monster
    
    # Move hero to monster cell
    monkeypatch.setattr('builtins.input', lambda _: "right")
    basic_game.move_hero()
    
    captured = capsys.readouterr()
    assert "Aaargh! A terrifying monster!" in captured.out

def test_find_treasure(basic_game, monkeypatch, capsys):
    """Test treasure chest interaction."""
    # Place treasure in adjacent cell
    chest = TreasureChest()
    basic_game.grid[0][1] = chest
    initial_coins = basic_game.hero.coins
    
    # Move hero to chest cell
    monkeypatch.setattr('builtins.input', lambda _: "right")
    basic_game.move_hero()
    
    assert basic_game.hero.coins > initial_coins
    captured = capsys.readouterr()
    assert "treasure chest" in captured.out

def test_find_potion(basic_game, monkeypatch, capsys):
    """Test healing potion pickup."""
    # Place potion in adjacent cell
    potion = HealingPotion()
    basic_game.grid[0][1] = potion
    initial_potions = len(basic_game.hero.pouch)
    
    # Move hero to potion cell
    monkeypatch.setattr('builtins.input', lambda _: "right")
    basic_game.move_hero()
    
    assert len(basic_game.hero.pouch) > initial_potions
    captured = capsys.readouterr()
    assert "healing potion" in captured.out

def test_shopkeeper_interaction(basic_game, monkeypatch, capsys):
    """Test shopkeeper interaction and purchases."""
    # Place shopkeeper in adjacent cell
    shopkeeper = Shopkeeper()
    basic_game.grid[0][1] = shopkeeper
    basic_game.hero.coins = 50  # Ensure enough coins for testing
    
    # Simulate move to shopkeeper and purchase potion
    inputs = iter(["right", "a", "c"])  # Move right, buy potion, exit shop
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    basic_game.move_hero()
    
    captured = capsys.readouterr()
    assert "Bert the Shopkeeper" in captured.out
    assert "Healing potion added to pouch" in captured.out

def test_game_over(basic_game, capsys):
    """Test game over condition."""
    basic_game.game_over()
    captured = capsys.readouterr()
    assert "Game Over" in captured.out

def test_prompt_user_quit(basic_game, monkeypatch):
    """Test quit game functionality."""
    monkeypatch.setattr('builtins.input', lambda _: "c")
    with pytest.raises(QuitGameException):
        basic_game.prompt_user()