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

from abc import ABC
import random

class Character(ABC):
    """A generic Character class for Player in the Maze

    Args:
        ABC (Abstract Class): Template for subclasses
    """

    def __init__(self, name: str):
        """Initialises a Character object.

        Args:
            name (str): The character's name
            max_health (int): The maximum health of the character
            defence (int): How well Character repels attacks
            stealth (int): How well Character dodges attacks
        """
        self.name = name
        self.pouch = {}
        
    @property
    def accuracy(self) -> int:
        """Getter method for retrieving the Character's accuracy

        Returns:
            int: Accuracy of the Character
        """
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self, accuracy):
        self._accuracy = accuracy

    @property
    def defence(self) -> int:
        """Getter method for retrieving the Character's defence stat

        Returns:
            self._defence: The Character's stealth stat
        """
        return self._defence

    @defence.setter
    def defence(self, defence):
        self._defence = defence

    @property
    def stealth(self) -> int:
        """Getter method for retrieving the Warrior's stealth stat

        Returns:
            self._stealth: The Warrior's stealth stat
        """
        return self._stealth

    @stealth.setter
    def stealth(self, stealth) -> int:
        self._stealth = stealth

    def dodge_chance(self) -> int:
        """A method defining the chance of successfully avoiding an attack

        Returns:
            int: The calculated dodge chance based on stealth and defence
        """
        return self.stealth * self.defence / 100

    def heal(self, potion) -> int:
        """Defines a healing method

        Args:
            potion (HealingPotion): Restores health to the user

        Returns:
            int: New health of the Character
        """
        if isinstance(potion, HealingPotion):
            if self.health + potion.effect > self.max_health:
                self.health = self.max_health
            else:
                self.health += potion.effect

    def attack(self, enemy):
        """An attack method for attacking an enemy object"""
        if self.attack_chance > 0.5:
            enemy.health -= self.power
    
    def attack_chance(self, enemy):
        """A method defining the chance of attacking an enemy

        Args:
            enemy (Character): An enemy object
        """
        return (1 - enemy.dodge_chance()) * self.accuracy / 10


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

    def __init__(self, name):
        """Initialises a Warrior object

        Args:
            name (str): The name of the Warrior object
        """
        super().__init__(name)
        self.max_health = 100
        self.health = self.max_health
        self.power = 20
        self.defence = 20
        self.stealth = 5
        self.accuracy = 10

    def attack(self, enemy):
        """Attack method for Warrior objects

        Args:
            enemy (Class): An enemy object
        """
        enemy.health -= self.power


class Mage(Character):
    """Defines a Mage Character, a subclass of the Character object

    Args:
        Character (Class): A template Character object
    """

    def __init__(self, name: str):
        """Initialises a Mage Character Instance.

        Args:
            name (str): The character's name
            health (int): The current health of the character
            defence (int): How well the Character repels attacks
            stealth (int): How well the Character dodges attacks
        """
        super().__init__(name)
        self.max_health = 75
        self.power = 25
        self.defence = 15
        self.stealth = 10
        self.accuracy = 15
        
        
class Archer(Character):
    """Archer subclass of Character

    Args:
        Character (Class): Tempate Character Object
    """

    def __init__(self, name: str):
        """Initialises an Archer Object

        Args:
            name (str): _description_
            max_health (int): _description_
            defence (int): _description_
            stealth (int): _description_
        """
        super().__init__(name)
        self.max_health = 100
        self.defence = 10
        self.stealth = 20
        self.power = 15
        self.accuracy = 20

class Monster(Character):
    def __init__(self):
        """Instantiates a Monster Object

        Args:
            max_health (int): Monster's maximum health
            defence (int): Monster's defence rating
            stealth (int): Monster's stealth rating
        """
        self.max_health = random.randint(40, 80)
        self.health = self.max_health
        self.defence = random.randint(5, 9)
        self.stealth = random.randint(5, 9)
        self.power = random.randint(5, 15)
    
    
        