from game_model import *
from game_interface import *
import pytest

def test_begin_game_yes(capsys, monkeypatch):
    # Simulate user input "yes"
    monkeypatch.setattr('builtins.input', lambda _: "yes")
    begin_game()
    captured = capsys.readouterr()
    assert "Welcome to Mazes and Monsters!" in captured.out

def test_begin_game_y(capsys, monkeypatch):
    # Simulate user input "y"
    monkeypatch.setattr('builtins.input', lambda _: "y")
    begin_game()
    captured = capsys.readouterr()
    assert "Welcome to Mazes and Monsters!" in captured.out

def test_begin_game_no(monkeypatch):
    # Simulate user input "no"
    monkeypatch.setattr('builtins.input', lambda _: "no")
    with pytest.raises(QuitGameException):
        begin_game()

def test_begin_game_other(monkeypatch):
    # Simulate user input "maybe"
    monkeypatch.setattr('builtins.input', lambda _: "maybe")
    with pytest.raises(QuitGameException):
        begin_game()



def test_create_hero_warrior(monkeypatch, capsys):
    inputs = iter(["Conan", "Warrior"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_hero()
    captured = capsys.readouterr()
    assert "Conan" in captured.out
    assert "Warrior" in captured.out

def test_create_hero_mage(monkeypatch, capsys):
    inputs = iter(["Merlin", "Mage"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_hero()
    captured = capsys.readouterr()
    assert "Merlin" in captured.out
    assert "Mage" in captured.out

def test_create_hero_archer(monkeypatch, capsys):
    inputs = iter(["Robin", "Archer"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_hero()
    captured = capsys.readouterr()
    assert "Robin" in captured.out
    assert "Archer" in captured.out

def test_create_hero_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(["Alex", "Thief", "Mage"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_hero()
    captured = capsys.readouterr()
    assert "Please enter a valid class." in captured.out
    assert "Mage" in captured.out
    assert "Alex" in captured.out


