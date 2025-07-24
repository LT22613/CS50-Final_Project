from game_model import *
from game_interface import *
from maze import Maze

def main():
    """The main function will execute all the functions required to run the game.
    """
    # Initialise the game interface by introducing the user to the game.
    begin_game()
    # Allow the user to create a Hero to play the game with.
    create_hero()
    # Initialise a maze object and display the Hero's starting position.
    game_maze = Maze()
    game_maze.print_maze()




if __name__ == "__main__":
    main()
