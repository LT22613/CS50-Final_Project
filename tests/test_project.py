import pytest
from project import welcome_message, ask_start, create_hero
from game_model import Warrior, Mage, Archer


def test_welcome_message_prompts(monkeypatch, capsys):
    # Simulate pressing Enter three times
    monkeypatch.setattr("builtins.input", lambda _: "")
    welcome_message()
    captured = capsys.readouterr()
    # Check that the final print statement is present
    assert "(1,1) is your starting position." in captured.out
    assert "You can move up, left, right or down" in captured.out
    assert "Remember, the goal is to navigate to the bottom-right square, (4,4). Good luck!" in captured.out

def test_ask_start_yes(monkeypatch):
    # Simulate user entering 'yes'
    monkeypatch.setattr("builtins.input", lambda _: "yes")
    ask_start()  # Should not raise or exit

def test_ask_start_no(monkeypatch):
    # Simulate user entering 'no'
    monkeypatch.setattr("builtins.input", lambda _: "no")
    with pytest.raises(SystemExit):
        ask_start()

def test_ask_start_invalid_then_yes(monkeypatch):
    # Simulate user entering invalid, then 'y'
    inputs = iter(["maybe", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    ask_start()  # Should eventually accept 'y' and not exit

@pytest.mark.parametrize("class_input,expected_type", [
    ("Warrior", Warrior),
    ("mage", Mage),
    ("ARCHER", Archer),
])
def test_create_hero_valid(monkeypatch, class_input, expected_type):
    # Simulate user entering a valid class
    monkeypatch.setattr("builtins.input", lambda _: class_input)
    hero = create_hero("TestHero")
    assert isinstance(hero, expected_type)
    assert hero.name == "TestHero"

def test_create_hero_invalid_then_valid(monkeypatch):
    # Simulate user entering invalid then valid class
    inputs = iter(["", "notaclass", "Mage"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    hero = create_hero("TestHero")
    assert isinstance(hero, Mage)
    assert hero.name == "TestHero"
    def test_welcome_message_prompts(monkeypatch, capsys):
        # Simulate pressing Enter three times
        monkeypatch.setattr("builtins.input", lambda _: "")
        welcome_message()
        captured = capsys.readouterr()
        # Check that the final print statement is present
        assert "(1,1) is your starting position." in captured.out
        assert "You can move up, left, right or down" in captured.out
        assert "Remember, the goal is to navigate to the bottom-right square, (4,4). Good luck!" in captured.out