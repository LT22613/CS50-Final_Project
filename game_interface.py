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
        answer = input("Are you ready to begin? Yes or No.\n")
        if re.fullmatch("yes|y", answer, flags = re.IGNORECASE):
            pass
        else:
            raise QuitGameException

def create_hero():
    name = input("\nPlease choose a name for your Hero\n").capitalize()
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
    print()
    print(hero)

class Game(object):
    """A class representing the state of our game.
    """
    def __init__(self, hero):
        self.hero = hero
        
    def visualise_game(self):
        """Provide the visual element of the game. 
        The game is set in a 5x5 grid. The hero begins in the top-left and the game only successfully 
        end if the hero makes it to the bottom right.
        """
        ...
    
    def game_over(self):
        if self.hero.health == 0:
            raise QuitGameException
        
    def run(self):
        
        try:
            while not self.game_over():
                # Visualise the game first
                self.visualise_game()
                
                # Prompt the user for input and execute the output.
                self.prompt_user()
                
                input("Press Enter to continue...")
                
                
                
                
            
        except:
            ...
        




        
        
        

    
def prompt_user():
    ...
    
      