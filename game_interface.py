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

class Game(object):
    """A class representing the state of our game.

    Attributes:
        player: a Character object representing the player.
        enemies: a dict mapping names (of type str) to Characters.
            Each entry represents an enemy the player must fight.
    """    

    def __init__(self, hero):
        """Initialise a game for your hero.

        Args:
            hero (Character): The Character object that you just created.
        """
        self.hero = hero
    
    def begin_game():
        print("Welcome to Mazes and Monsters!")
        print("The objective of the game is to guide your Hero from the Start cell to the Finish cell.")
        answer = input("Are you ready to begin?")
        if re.search("yes|y", answer, flags = re.IGNORECASE):
            pass
        else:
            raise QuitGameException
    
    def visualise_game():
        """Provide the visual element of the game. 
        The game is set in a 5x5 grid. The hero begins in the top-left and the game only successfully 
        end if the hero makes it to the bottom right.
        """
        ...

    
                
                
        
        
    

def create_hero():
    print("\nPlease select which class you would like your Hero to be")
    while True:
        option = input("Warrior/Mage/Archer\n")
        name = input("Please enter the name you would like your Hero to have\n").capitalize()
    
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
            print("\nPlease enter a valid class.\n")
            continue
    print()
    print(hero)


        
        
        

    
def prompt_user():
    ...
    
      