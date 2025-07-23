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
    
begin_game()