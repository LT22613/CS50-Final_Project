from game_model import *
from game_interface import *
import pytest
import re
from tabulate import tabulate
import numpy as np

def visualise_game():
        """Provide the visual element of the game. 
        The game is set in a 5x5 grid. The hero begins in the top-left and the game only successfully 
        end if the hero makes it to the bottom right.
        """
        """
        headers = [" ", " ", " ", " ", " "]
        table = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
        
        print(tabulate(table, headers, tablefmt = "grid"))
        """
        a = np.zeros(5)
        print(a)

visualise_game()