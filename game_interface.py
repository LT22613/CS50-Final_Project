"""
game_interface.py

This module creates the interface through which the user plays the game.

This module focuses on creating the interaction between the users and the game, as well
as the visuals of the game.
"""
from game_model import *


def begin_game():
    print("Welcome to Mazes and Monsters!\n")
    print("The objective of the game is to guide your Hero from the Start cell to the Finish cell.")
    print("Please select which class you would like your Hero to be")
    option = input("Warrior/Mage/Archer")
    name = input("Please enter the name you would like your Hero to have")
    if option == "Warrior":
        hero = Warrior(name)
    elif option == "Mage":
        hero = Mage(name)
    else:
        hero = Archer(name)
    
def prompt_user():
    
      