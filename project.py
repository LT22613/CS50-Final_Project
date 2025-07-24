from game_model import *
from game_interface import *
from maze import Maze

def main():
    """The main function will execute all the functions required to run the game.
    """
    # Initialise the game interface by introducing the user to the game.
    #begin_game()
    # Allow the user to create a Hero to play the game with.
    #create_hero()
    # Initialise a maze object and display the Hero's starting position.
    input("Are you ready to begin your battle through the maze?\n")
    input("""
Welcome to the Maze! Here you will guide your hero as they navigate their way through the monsters that block their way to the finish line.

Press Enter to continue.
""")
    input("""You will shortly see a display of your hero's starting location. In each cell, your hero may either encounter a monster, healing potion,
treasure chest or a shopkeeper. 

Press Enter to continue.
""")
    input("""
The treasure chest contains money that can be used to buy healing potions or special upgrades from the shopkeeper!

Press Enter to continue.
""")
    game_maze = Maze()
    game_maze.print_maze()
    




if __name__ == "__main__":
    main()
