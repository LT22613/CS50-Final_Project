"""
game_interface.py

This module creates the interface through which the user plays the game.

This module focuses on creating the interaction between the users and the game, as well
as the visuals of the game.
"""
from game_model import *
import re


def begin_game():
    print("Welcome to Mazes and Monsters!")
    print("The objective of the game is to guide your Hero from the Start cell to the Finish cell.")
    print("Please select which class you would like your Hero to be")
    while True:
        option = input("Warrior/Mage/Archer\n")
        name = input("Please enter the name you would like your Hero to have\n")
    
        if re.search("warrior", option, flags=re.IGNORECASE):
            hero = Warrior(name)
            break
        elif re.search("mage", option, flags=re.IGNORECASE):
            hero = Mage(name)
            break
        elif option == "Archer":
            hero = Archer(name)
            break
        else:
            return True
        

    
def prompt_user():
    ...
    
      