from game_model import *
from game_interface import *
import pytest
import re

"""
def begin_game():
    print("Welcome to Mazes and Monsters!")
    print("The objective of the game is to guide your Hero from the Start cell to the Finish cell.")
    print("Please select which class you would like your Hero to be")
    i = True
    while True:
        option = input("Warrior/Mage/Archer\n")
        name = input("Please enter the name you would like your Hero to have\n")
        try:
                # Check if the user selected warrior case-insensitively
                if re.search("warrior", option, flags = re.IGNORECASE):
                        hero = Warrior(name)
                        break
                # Check if the user selected mage case-insensitively
                elif re.search("mage", option, flags = re.IGNORECASE):
                        hero = Mage(name)
                        break
                # Check if the user selected archer case-insensitively
                elif re.search("archer", option, flags = re.IGNORECASE):
                        hero = Archer(name)
                        break
                # If user did enter a valid class, return a ValueError
                else:   
                        raise ValueError
        # If ValueError is raised, print error message and ask the user for a class and name again.
        except ValueError as e:
                print("Invalid Class Entered")
                continue
    print(hero)            
                
    
begin_game()
"""

"""
warrior_1 = Warrior("Bob")
print(warrior_1)
"""

def test_big(capsys):
        begin_game()

print(test_big)