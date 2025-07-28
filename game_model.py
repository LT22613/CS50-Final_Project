"""This module creates all the different objects that operate in the game.
1. Template Character Object
2. Warrior Object
3. Mage Object
4. Archer Object
5. Monster Object
6. Healing Potion
7. Shopkeeper
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
        self._coins = 0
        self._potions = 1
    
    @abstractmethod
    def __str__(self):
        pass
        
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
        
    @property
    def coins(self) -> int:
        return self._coins
    
    @coins.setter
    def coins(self, value) -> int:
        if value < 0:
            return "Can't have a negative number of coins"
        else:
            self._coins = value
    
    @property
    def potions(self) -> int:
        return self._potions
    
    @potions.setter
    def potions(self, value):
        if value < 0:
            return "Can't have negative number of potions"
        else:
            self._potions = value 
        

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
        if self.hit_chance(enemy) > 0.7:
            enemy.health -= self.power * 1.5
            return self.power * 1.5
        elif self.hit_chance(enemy) > 0.5:
            enemy.health -= self.power 
            return self.power
        elif self.hit_chance(enemy) > 0.3:
            enemy.health -= self.power * 0.5
            return self.power * 0.5
        else:
            return "Your accuracy is too low to harm this enemy."
        

    def heal(self, potion) -> float:
        """Defines a healing method

        Args:
            potion (HealingPotion): Restores health to the user

        Returns:
            int: New health of the Character
        """
        if self.potions:
            # Check if the potion heals beyond the Character's max health
            if self.health + potion.effect  > self.max_health:
                self.health = self.max_health
            else:
                self.health += potion.effect
            # Reduce the number of uses of the healing potion by 1
            self.potions -= 1
        else:
            print("You do not have a healing potion.")

    def empty_chest(self, chest):
        """Add the number of coins in the chest to the Character's pouch.

        Args:
            chest (TreasureChest): A TreasureChest instance that contains a number of coins
        """
        # Add the number of coins in the chest to the number of coins the character has
        if self.coins:
            self.coins += chest.num_of_coins
        else:
            self.coins = chest.num_of_coins


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
    
    def __str__(self):
        return f"""{self.name} is a mighty warrior with the following attributes:
Health: {self.health}
Power: {self.power}
Defence: {self.defence}
Stealth: {self.stealth}
Accuracy: {self.accuracy}
    """


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
    
    def __str__(self):
        return f"""{self.name} is a powerful Mage with the following attributes:
Health: {self.health}
Power: {self.power}
Defence: {self.defence}
Stealth: {self.stealth}
Accuracy: {self.accuracy}
    """


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
        self.accuracy = 9
        
    def __str__(self):
        return f"""{self.name} is a powerful Archer with the following attributes:
Health: {self.health}
Power: {self.power}
Defence: {self.defence}
Stealth: {self.stealth}
Accuracy: {self.accuracy}
"""


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
    
    def __str__(self):
        return f"{self.name} is a nasty monster with {self.health} life points."


class TreasureChest():
    """Defines a Treasure Chest item that contains a large number of coins."""

    def __init__(self):
        """Defines the number of coins in the treasure chest.

        Args:
            num_of_coins (int): Number of coins in the treasure chest.
        """
        self.num_of_coins = random.randint(20, 50)


class HealingPotion:
    """Defines a Healing Potion

    Attributes:
        num_uses (int): Number of times the Healing Potion can be used
        effect (int): Amount the Healing Potion heals

    """

    def __init__(self):
        self.effect = 20
        
class Shopkeeper:
    """A Shopkeeper object that sells HealingPotion objects and stat upgrades for coins.

    Attributes:
        store (dict): Dictionary of items and their prices in coins
    """
    
    def __init__(self):
        self.store = {
            "healing_potion": 10,  # Cost in coins
            "accuracy_boost": 30,
            "defence_boost": 30,
            "stealth_boost": 30
        }

    def sell_potion(self, character):
        """Sells a healing potion to a character if they have enough coins.
        
        Args:
            character (Character): The character buying the potion
        """
        if character.coins < self.store["healing_potion"]:
            print("Not enough coins!")
            return
        
        character.potions += 1
        character.coins -= self.store["healing_potion"]
        print(f"Bought healing potion for {self.store['healing_potion']} coins")

    def upgrade_stat(self, character, stat):
        """Upgrades a character's stat if they have enough coins.
        
        Args:
            character (Character): The character to upgrade
            stat (str): The stat to upgrade (accuracy, defence, or stealth)
        """
        if stat not in ["accuracy", "defence", "stealth"]:
            print("Invalid stat!")
            return
            
        cost = self.store[f"{stat}_boost"]
        if character.coins < cost:
            print("Not enough coins!")
            return

        current_value = getattr(character, stat)
        setattr(character, stat, current_value + 1)
        character.coins -= cost
        return f"Upgraded {stat} for {cost} coins"