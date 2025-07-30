"""
game_interface.py

This module creates the interface through which the user plays the game.

This module focuses on creating the interaction between the users and the game, as well
as the visuals of the game.
"""
from game_model import *
import sys

class QuitGameException(Exception):
    pass

class Game(object):
    """A class representing the state and flow of the game.
    
    This class manages the game state, including the hero's position, movement,
    combat, interactions with items and NPCs, and overall game progression.
    
    Attributes:
        hero (Character): The player's character (Warrior, Mage, or Archer)
        grid (List[List]): The 2D maze grid containing game objects
        hero_position (tuple): Current (row, col) position of hero in the maze
    """
    def __init__(self, hero, grid = [
            [None, TreasureChest(), Shopkeeper(), TreasureChest(), None],
            [HealingPotion(), None, Monster("Orc"), None, None],
            [None, TreasureChest(), None, Monster("Troll"), None],
            [Monster("Skeleton"), None, HealingPotion(), None, Shopkeeper()],
            [None, None, Monster("Dragon"), TreasureChest(), None]
        ]):
        """Initialize a new game instance.
        
        Args:
            hero (Character): The player's chosen character
            grid (List[List]): The 2D maze grid
        """
        self.hero = hero
        self.rows = 5
        self.cols = 5
        self.grid = grid
        self.hero_position = (0, 0)  # Start at top-left corner
        print(f"\nWelcome to the Maze, {hero.name}!")
    
    def user_turn(self):
        """Display turn indicator for the player."""
        print(f"\n🔹 It's {self.hero.name}'s turn 🔹")
        print(f"{self.hero_position} is your current position")
        
    def prompt_user(self):
        """Prompt user for their action choice and handle the input.
        
        Available actions:
        - Move: Navigate the maze
        - Heal: Use a healing potion if available
        - Quit: End the game
        
        Raises:
            QuitGameException: If player chooses to quit
        """
        while True:
            # Display action menu
            print("\nChoose an action:\nA. Move\nB. Heal\nC. Quit")
            choice = input("Enter your choice: ").strip().lower()
            
            if choice == 'a':
                self.move_hero()
                break
            elif choice == 'b':
                if self.hero.potions:
                    potion = HealingPotion()
                    self.hero.heal(potion)
                    if self.hero.health < self.hero.max_health:
                        self.hero.potions -= 1
                        print(f"You feel rejuvenated! {self.hero.name} now has {self.hero.health} lifepoints.")
                    elif self.hero.health == self.hero.max_health:
                        print("Don't waste your potions. You have full life points.")
                else:
                    print("No healing potions available.")
            elif choice == 'c':
                sys.exit("\nGoodbye. Come back soon!")
            else:
                print("Invalid choice. Please try again.")
    
    def move_hero(self):
        """Handle hero movement in the maze.
        
        Gets direction input from user and updates hero position if valid.
        Triggers appropriate events based on destination cell contents.
        """
        # Define possible movement directions and their coordinate changes
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        direction = input("Which direction? (up/down/left/right): ").strip().lower()

        if direction not in directions:
            print("Invalid direction.")
            return

        # Calculate new position
        row_offset, col_offset = directions[direction]
        new_row = self.hero_position[0] + row_offset
        new_col = self.hero_position[1] + col_offset

        # Check if move is within grid bounds
        if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]):
            self.hero_position = (new_row, new_col)
            if self.hero_position == (4, 4):
                print("\nWell done, you won!")
                exit()
            self.game_turn()  # Process events at new position
        else:
            print("You can't move that way!")
        
    def game_turn(self):
        """Process events at hero's current position.
        
        Handles interactions with:
        - Monsters (combat)
        - Treasure chests (coin collection)
        - Healing potions (item pickup)
        - Shopkeeper (trading)
        """
        cell = self.grid[self.hero_position[0]][self.hero_position[1]]
        
        print()
        # Handle different cell contents
        if cell is None:
            print("Yay! No scary monsters here.")
        elif isinstance(cell, Monster):
            print("Aaargh! A terrifying monster!")
            self.fight(cell)
        elif isinstance(cell, TreasureChest):
            print("Oooooh! A treasure chest. I hope there are a lot of coins inside!")
            print(f"{self.hero.name} found {cell.num_of_coins} coins!")
            self.hero.coins = cell.num_of_coins
            self.grid[self.hero_position[0]][self.hero_position[1]] = None
        elif isinstance(cell, HealingPotion):
            print("Wow! You found a healing potion! That's surely going to be useful!")
            self.hero.potions += 1
            self.grid[self.hero_position[0]][self.hero_position[1]] = None
        elif isinstance(cell, Shopkeeper):
            print("You found Bert the Shopkeeper!")
            self.visit_shopkeeper(cell)
        else:
            print("Unexpected object encountered.")
        
        # Continue game flow
        self.user_turn()    
        self.prompt_user()
    
    def fight(self, enemy):
        """
        Simulates a turn-based battle between the hero and an enemy.
        The fight continues until either the hero or the enemy is defeated (health reaches 0).
        Each turn consists of the hero attacking first, followed by the enemy's counter-attack
        if they survive.
        Args:
            enemy (Enemy): The enemy character object that the hero is fighting against
        Returns:
            None: The method either continues until combat is resolved or calls game_over()
            if the hero is defeated
        Side effects:
            - Modifies hero and enemy health values during combat
            - Prints combat results to console after each attack
            - May trigger game_over() if hero is defeated
        """
        while self.hero.health > 0 and enemy.health > 0:
            damage = self.hero.attack(enemy)
            if type(damage) == float or type(damage) == int:
                print(f"You did {damage} damage. Enemy health: {enemy.health}")
            else:
                print(damage)
            if enemy.health <= 0:
                print("Yay! We smashed the nasty beastie to pieces!")
                return

            damage = enemy.attack(self.hero)
            print(f"The enemy did {damage} damage. Your health: {self.hero.health}")

        if self.hero.health <= 0:
            self.game_over()
    
    def visit_shopkeeper(self, shopkeeper):
        """Handle shopping interaction with the shopkeeper.
        
        Args:
            shopkeeper (Shopkeeper): The shopkeeper NPC to interact with
            
        Available purchases:
        - Healing Potion (10 coins)
        - Stat Upgrade (20 coins)
        """
        while True:
            print("\nWhat would you like to buy?\nA. Healing Potion (10 coins)\nB. Stat Upgrade (20 coins)\nC. Nothing")
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'a':
                if self.hero.coins >= 10:
                    shopkeeper.sell_potion(self.hero)
                    self.hero.potions += 1
                    print("Healing potion added to pouch.")
                    print(f"{self.hero.name} has {self.hero.coins} coins left.")
                else:
                    print("Not enough coins.")
            elif choice == 'b':
                if self.hero.coins >= 20:
                    stat = input("Which stat would you like to upgrade? Accuracy, defence or stealth. ").lower()
                    upgraded = shopkeeper.upgrade_stat(self.hero, stat)
                    if upgraded:
                        match stat:
                            case "accuracy":
                                print(f"Your {stat} is now {self.hero.accuracy}")
                            case "defence": 
                                print(f"Your {stat} is now {self.hero.defence}")
                            case "stealth":
                                print(f"Your {stat} is now {self.hero.stealth}")
                    else:
                        print("Stat already at max.")
                else:
                    print("Not enough coins.")
            elif choice == 'c':
                print("You chose not to buy anything.")
                break
            else:
                print("Invalid choice.")
    
    def game_over(self):
        """Handle game over state when hero is defeated."""
        print("💀 Game Over. You were defeated.")
        exit()

