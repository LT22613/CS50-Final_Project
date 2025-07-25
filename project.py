from game_model import *
from game_interface import *
from maze import Maze

def main():
    """The main function will execute all the functions required to run the game.
    """
    # Initialise the game interface by introducing the user to the game.
    begin_game()
    # Allow the user to create a Hero to play the game with.
    hero = create_hero()
    # Initialise a maze object and display the Hero's starting position.
    answer = input("\nAre you ready to begin your battle through the maze?\n")
    if re.fullmatch("yes|y", answer, flags = re.IGNORECASE):
        pass
    else:
        raise QuitGameException
    
    input("""\nWelcome to the Maze! Here you will guide your hero as they navigate their way through the monsters that block their way to the finish line.
      
Press Enter to continue.
""")
    input("""You will shortly see a display of your hero's starting location. In each cell, your hero may either encounter a monster, healing potion,
treasure chest or a shopkeeper. 

Press Enter to continue.
""")
    input("""The treasure chest contains money that can be used to buy healing potions or special upgrades from the shopkeeper!

Press Enter to continue.
""")
    print("""This is your starting position. The H represents your hero's current position.
You can move up, left, right or down, so long as you stay within the maze's boundaries.
Remember, the goal is to navigate to the bottom-right square. Good luck!""")
    # Instantiate a Maze object called grid
    grid = Maze()
    # Create a game_instance using the hero and grid created.
    game_instance = Game(hero, grid)
    # Print the maze to show the starting position.
    grid.print_maze()
    
    # Ask the player what they would like to do.
     




if __name__ == "__main__":
    main()
