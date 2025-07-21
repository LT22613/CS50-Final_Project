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

    def __init__(self, name: str, max_health: int = 100):
        """Initialises a Character object.

        Args:
            name (str): The character's name
            max_health (int): The character's maximum health
        """
        self.name = name
        self.max_health = max_health
        self.pouch = {}
        
    @property
    def health(self):
        """Creates a health property that returns the character's current health.

        Returns:
            health (int) : The character's current health.
        """
        return self._health
    
    @health.setter
    def health(self, new_health):
        """Creates a health setter that allows the user to set a new health for the character.

        Args:
            health (int) : The character's current health.
            new_health (int): The character's new health.
        """
        # If the new health is set to below 0, the new health is corrected to be 0.
        if new_health < 0:
            self._health = 0
        # If the new health is set higher than the character's max health, set it to the character's max health.
        elif new_health > self.max_health:
            self._health = self.max_health
        # Otherwise, if the new health is between 0 and the character's max health, the new health is set to the entered value.
        else: 
            self._health = new_health
        
    @property
    def accuracy(self) -> int:
        """Getter method for retrieving the Character's accuracy

        Returns:
            int: Accuracy of the Character
        """
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self, accuracy):
        if 0 <= accuracy <= 30:
            self._accuracy = accuracy
        else:
            return "Accuracy must be between 0 and 30"

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
    
    def hit_chance(self, enemy):
        """A method defining the chance of attacking an enemy

        Args:
            enemy (Character): An enemy object
        """
        return (1 - enemy.dodge_chance()) * self.accuracy / 10

    def attack(self, enemy):
        """An attack method for attacking an enemy object"""
        if self.hit_chance > 0.5:
            enemy.health -= self.power
            
    def heal(self, potion) -> int:
        """Defines a healing method

        Args:
            potion (HealingPotion): Restores health to the user

        Returns:
            int: New health of the Character
        """
        # Check if the potion is a healing potion
        if isinstance(potion, Healing_Potion):
            # Check if the user has the potion in their pouch.
            if potion in self.pouch.keys():
                # Check if the potion heals beyond the Character's max health
                if self.health + potion.effect > self.max_health:
                    self.health = self.max_health
                # If not, then just add the healing effect of the potion.
                else:
                    self.health += potion.effect
                # Reduce the number of uses of the healing potion by 1.
                self.pouch[potion] -= 1
            # Print("You do not have a healing potion. ")
            # Write code to re-prompt the playet to enter a different command.
            else:
                print("You do not have a healing potion. ")
        # Print("Potion is not a healing potion. ")
        # Write code to re-prompt the player to enter a different command. 
        else:
            print("Potion is not a healing potion. ")
    
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
        self.health = self.max_health
        self.power = 20
        self.defence = 20
        self.stealth = 5
        self.accuracy = 10

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

    def __init__(self, name: str, max_health: int = 75):
        """Initialises a Mage Character Instance.

        Args:
            name (str): The character's name
            health (int): The current health of the character
            defence (int): How well the Character repels attacks
            stealth (int): How well the Character dodges attacks
        """
        super().__init__(name, max_health)
        self.health = self.max_health
        self.power = 25
        self.defence = 15
        self.stealth = 10
        self.accuracy = 15
        
        
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
        self.health = self.max_health
        self.defence = 10
        self.stealth = 20
        self.power = 15
        self.accuracy = 20

class Monster(Character):
    def __init__(self):
        """Instantiates a Monster Object that inherits its methods and attributes from the Character Class.
        """
        self.max_health = random.randint(40, 80)
        self.health = self.max_health
        self.defence = random.randint(5, 9)
        self.stealth = random.randint(5, 9)
        self.power = random.randint(5, 15)


class Treasure_Chest:
    """Defines a Treasure Chest item that contains a large number of coins.
    """
    
    def __init__(self, num_of_coins):
        """Defines the number of coins in the treasure chest.

        Args:
            num_of_coins (int): Number of coins in the treasure chest.
        """
        self.num_of_coins = num_of_coins

class Healing_Potion:
    """Defines a Healing Potion
    
    Attributes:
        
    """
    def __init__(self):
        self.effect = 20
        