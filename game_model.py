"""This module creates all the different objects that operate in the game.
1. Template Character Object
2. Warrior Object
3. Mage Object
4. Archer Object
5. Monster Object
6. Healing Potion
7. Mana Potion
8. Shopkeeper
9. Boss - Subclass of Monster
"""

from abc import ABC, abstractmethod
import random
import re


class Character(ABC):
    """A generic Character class for the player in the Maze

    Attributes:
        name (str): The Character's name
        accuracy (int): The Character's accuracy
        pouch (dict): The Character's pouch
        defence (int): The Character's defence rating
        stealth (int): The Character's stealth rating
        health (int): The Character's current health
    """

    def __init__(self, name: str, max_health: float = 100, accuracy = 8, defence = 8, stealth = 8):
        """Initialises a Character object.

        Args:
            name (str): The character's name
            max_health (int): The character's maximum health
        """
        self.name = name
        self.max_health = max_health
        self._health = max_health
        self._accuracy = accuracy
        self._defence = defence
        self._stealth = stealth
        self.pouch = {}

    @property
    def health(self) -> float:
        """Creates a health property that returns the character's current health.

        Returns:
            health (int) : The character's current health.
        """
        return self._health

    @health.setter
    def health(self, value) -> float:
        """Creates a health setter that allows the user to set a new health for the character.

        Args:
            health (int) : The character's current health.
            new_health (int): The character's new health.
        """
        # If current health + the added value is above max health, then set to max health
        if value > self.max_health:
            self._health = self.max_health
        # Otherwise, add the value
        elif value < 0:
            self._health = 0
        else:
            self._health = value
            
    @property
    def accuracy(self) -> int:
        """Getter method for retrieving the Character's accuracy

        Returns:
            int: Accuracy of the Character
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value):
        # Only set accuracy if value is an integer
        if isinstance(value, int):
            if 0 <= value <= 10:
                self._accuracy = value
            elif value > 10:
                self._accuracy = 10
            else:
                self._accuracy = 0
        else:
            raise ValueError("Accuracy must be an integer")
    

    @property
    def defence(self) -> int:
        """Getter method for retrieving the Character's defence stat

        Returns:
            self._defence: The Character's stealth stat
        """
        return self._defence

    @defence.setter
    def defence(self, value):
        if isinstance(value, int):
            if 0 <= value <= 10:
                self._defence = value
            elif value < 0:
                self._defence = 0
            else:
                self._defence = 10
        else:
            raise ValueError("Defence must be an integer")

    @property
    def stealth(self) -> int:
        """Getter method for retrieving the Warrior's stealth stat

        Returns:
            self._stealth: The Warrior's stealth stat
        """
        return self._stealth

    @stealth.setter
    def stealth(self, value) -> int:
        """Setter method for setting the stealth attribute of a Character object.

        Args:
            stealth (int): How well the object can dodge an attack

        Returns:
            stealth (int): The updated stealth value of the object.
        """
        if isinstance(value, int):
            if 0 <= value <= 10:
                self._stealth = value
            elif value < 0:
                self._stealth = 0
            else:
                self._stealth = 10
        else:
            raise ValueError("Defence must be an integer")

    def dodge_chance(self) -> int:
        """A method defining the chance of successfully avoiding an attack

        Returns:
            int: The calculated dodge chance based on stealth and defence
        """
        return self.stealth * self.defence / 100

    def hit_chance(self, enemy):
        """A method defining the chance of attacking an enemy

        Args:
            enemy (Character): An enemy object
        """
        return (1 - enemy.dodge_chance()) * self.accuracy / 10

    def attack(self, enemy):
        """An attack method for attacking an enemy object"""
        if self.hit_chance > 0.7:
            enemy.health -= self.power * 1.5
        

    def heal(self) -> float:
        """Defines a healing method

        Args:
            potion (HealingPotion): Restores health to the user

        Returns:
            int: New health of the Character
        """
        # Check if any of the items in the pouch are Healing_Potion objects
        healing_potions = [
            item for item in self.pouch.keys() if isinstance(item, Healing_Potion)
        ]
        if healing_potions:
            potion = healing_potions[0]
            # Check if the potion heals beyond the Character's max health
            if self.health + potion.effect > self.max_health:
                self.health = self.max_health
            else:
                self.health += potion.effect
            # Reduce the number of uses of the healing potion by 1.
            potion.num_uses -= 1
        else:
            print("You do not have a healing potion.")

    def empty_chest(self, chest):
        """Add the number of coins in the chest to the Character's pouch.

        Args:
            chest (Treasure_Chest): A Treasure_Chest instance that contains a number of coins
        """
        # Add the number of coins in the chest to the number of coins the character has
        if "coins" in self.pouch.keys():
            self.pouch["coins"] += chest.num_of_coins
        else:
            self.pouch["coins"] = chest.num_of_coins


class Warrior(Character):
    """Defines a Warrior, a subclass of the Character object

    Args:
            name (str): The Warrior's name
            max_health(int): The maximum health of the Warrior
            health (int): The current health of the Warrior
            defence (int): How well the Warrior repels attacks
            stealth (int): How well the Warrior dodges attacks
            power(int): How hard the Warrior hits
    """

    def __init__(self, name: str, max_health: int = 100):
        """Initialises a Warrior object

        Args:
            name (str): The name of the Warrior object
        """
        super().__init__(name, max_health)
        self._health = max_health
        self.power = 20
        self._defence = 10
        self._stealth = 6
        self._accuracy = 7


class Mage(Character):
    """Defines a Mage Character, a subclass of the Character object

    Attributes:
        name (str): The Mage's name
        health (int): The current health of the mage
        max_health (int): The max health of the mage
        defence (int): How well the Character repels attacks
        stealth (int): How well the Character dodges attacks
        power (int): How hard the Mage hits
        accuracy (int): How accurate the Mage's attacks are
    """

    def __init__(self, name: str, max_health = 75):
        """Initialises a Mage Character Instance.

        Args:
            name (str): The character's name
            health (int): The current health of the character
            defence (int): How well the Character repels attacks
            stealth (int): How well the Character dodges attacks
        """
        super().__init__(name, max_health)
        self._health = max_health
        self.power = 25
        self.defence = 7
        self.stealth = 8
        self._accuracy = 8


class Archer(Character):
    """Archer subclass of Character

    Attributes:
            name (str): The Archer's name
            health (int): The current health of the Archer
            max_health (int): The max health of the Archer
            defence (int): How well the Archer repels attacks
            stealth (int): How well the Archer dodges attacks
            power (int): How hard the Archer hits
            accuracy (int): How accurate the Archer's attacks are
    """

    def __init__(self, name: str, max_health: int = 50):
        """Initialises an Archer Object

        Args:
            name (str): The Archer's name
            max_health (int): The max health of the Archer
        """
        super().__init__(name, max_health)
        self._health = self.max_health
        self.power = 15
        self.defence = 5
        self.stealth = 10
        self.accuracy = 8


class Monster(Character):
    def __init__(self, name, seed = random.seed()):
        """Instantiates a Monster Object that inherits its methods and attributes from the Character Class."""
        super().__init__(name)
        self.seed = seed
        self.max_health = random.randint(40, 80)
        self.health = self.max_health
        self.defence = random.randint(5, 8)
        self.stealth = random.randint(5, 8)
        self.power = random.randint(5, 15)


class Treasure_Chest:
    """Defines a Treasure Chest item that contains a large number of coins."""

    def __init__(self, num_of_coins):
        """Defines the number of coins in the treasure chest.

        Args:
            num_of_coins (int): Number of coins in the treasure chest.
        """
        self.num_of_coins = num_of_coins


class Healing_Potion:
    """Defines a Healing Potion

    Attributes:
        num_uses (int): Number of times the Healing Potion can be used
        effect (int): Amount the Healing Potion heals

    """

    def __init__(self):
        self.num_uses = 5
        self.effect = 20
