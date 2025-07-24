"""
game_interface.py

This module creates the interface through which the user plays the game.

This module focuses on creating the interaction between the users and the game, as well
as the visuals of the game.
"""
from game_model import *
import re        
import tabulate

class QuitGameException(Exception):
    pass

def begin_game():
        print("Welcome to Mazes and Monsters!\nThe objective of the game is to guide your Hero from the Start cell to the Finish cell.")
        answer = input("\nAre you ready to begin? Yes or No.\n")
        if re.fullmatch("yes|y", answer, flags = re.IGNORECASE):
            pass
        else:
            raise QuitGameException

def create_hero():
    while True:
        name = input("\nPlease choose a name for your Hero\n").capitalize()
        if name == "":
            continue
        else:
            break
        
    while True:
        option = input("\nPlease select which class you would like your Hero to be: Warrior/Mage/Archer\n")
        
        if re.search("warrior", option, flags=re.IGNORECASE):
            hero = Warrior(name)
            break
        elif re.search("mage", option, flags=re.IGNORECASE):
            hero = Mage(name)
            break
        elif re.search("archer", option, flags = re.IGNORECASE):
            hero = Archer(name)
            break
        else:
            print("\nPlease enter a valid class.")
            print("-" * 27)
            continue 
    return hero

class Game(object):
    """A class representing the state and flow of the game.
    
    This class manages the game state, including the hero's position, movement,
    combat, interactions with items and NPCs, and overall game progression.
    
    Attributes:
        hero (Character): The player's character (Warrior, Mage, or Archer)
        grid (List[List]): The 2D maze grid containing game objects
        hero_position (tuple): Current (row, col) position of hero in the maze
    """
    def __init__(self, hero, grid):
        """Initialize a new game instance.
        
        Args:
            hero (Character): The player's chosen character
            grid (List[List]): The 2D maze grid
        """
        self.hero = hero
        self.grid = grid
        self.hero_position = (0, 0)  # Start at top-left corner
        print(f"{"\n"}Welcome to the Maze, {hero.name}!")
    
    def user_turn(self):
        """Display turn indicator for the player."""
        print(f"\n🔹 It's {self.hero.name}'s turn 🔹")
        
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

            if choice == 'a' or 'A':
                self.move_hero()
                break
            elif choice == 'b':
                if self.hero.use_healing_potion():
                    print("You feel rejuvenated!")
                else:
                    print("No healing potions available.")
            elif choice == 'c':
                raise QuitGameException("Thanks for playing!")
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

        # Handle different cell contents
        if cell is None:
            print("Yay! No scary monsters here.")
        elif isinstance(cell, Monster):
            print("Aaargh! A terrifying monster!")
            self.fight(cell)
        elif isinstance(cell, Boss):
            print("😱 Boss Battle!")
            self.fight(cell)
        elif isinstance(cell, TreasureChest):
            print("Oooooh! A treasure chest. I hope there are a lot of coins inside!")
            print(f"{self.hero.name} found {cell.num_of_coins} coins!")
            self.hero.coins += cell.num_of_coins
            self.grid[self.hero_position[0]][self.hero_position[1]] = None
        elif isinstance(cell, HealingPotion):
            print("Wow! You found a healing potion! That's surely going to be useful!")
            self.hero.pouch.add_potion(cell)
            self.grid[self.hero_position[0]][self.hero_position[1]] = None
        elif isinstance(cell, Shopkeeper):
            print("You found Bert the Shopkeeper!")
            self.visit_shopkeeper(cell)
        else:
            print("Unexpected object encountered.")
        
        # Continue game flow
        self.user_turn()    
        self.prompt_user()
    
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
                    potion = shopkeeper.sell_potion()
                    self.hero.pouch.add_potion(potion)
                    self.hero.coins -= 10
                    print("Healing potion added to pouch.")
                else:
                    print("Not enough coins.")
            elif choice == 'b':
                if self.hero.coins >= 20:
                    upgraded = shopkeeper.upgrade_stat(self.hero)
                    if upgraded:
                        self.hero.coins -= 20
                        print("Stat upgraded!")
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
                
                
                
                
            
      
        




        
        
        

    
def prompt_user():
    ...

