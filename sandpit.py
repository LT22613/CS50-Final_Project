from game_model import *
from game_interface import *
import pytest
import re


def begin_game():
        print("Welcome to Mazes and Monsters!\nThe objective of the game is to guide your Hero from the Start cell to the Finish cell.")
        answer = input("Are you ready to begin?\n")
        if re.fullmatch("yes|y", answer, flags = re.IGNORECASE):
            pass
        else:
            raise QuitGameException   
    
begin_game()