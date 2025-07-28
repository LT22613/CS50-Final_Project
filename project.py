from game_model import *
from game_interface import *
import sys

def main():
    """The main function will execute all the functions required to run the game.
    """
    # Initialise the game interface by introducing the user to the game.
    """
    print("Welcome to Mazes and Monsters!\n")
    while True:
        answer = input("Are you ready to begin? Yes or No.\n").lower()
        if re.fullmatch("yes|y", answer):
            break
        elif re.fullmatch("no|n", answer):
            sys.exit("\nThat's a shame. Feel free to try the game out soon!")
        else:
            print("\nPlease say yes or no.\n")
    """
    # Allow the user to create a Hero to play the game with
    while True:
        name = input("\nEnter a name for your hero.\n")
        if name == "":
            continue
        else:
            break
    hero = create_hero(name)
    """
    # Ask user if they want to begin the game.
    ask_start()
    # Run the initial welcome message to the user, introducing the gameplay.
    welcome_message()
    """
    # Create a game_instance using the hero and grid created.
    game_instance = Game(hero)
    
    # This while block runs the game loop until completion.
    while True:
        game_instance.prompt_user()
        
class QuitGameException(Exception):
    """Custom exception to handle quitting the game."""
    pass

def create_hero(name):
    """
    Prompts the user to select a hero class and creates a hero instance.

    Args:
        name (str): The name of the hero.

    Returns:
        Hero: An instance of the selected hero class (Warrior, Mage, or Archer).
    """
    while True:
        option = input("\nPlease select which class you would like your Hero to be: Warrior/Mage/Archer\n")
        
        if re.search("warrior", option, flags=re.IGNORECASE):
            hero = Warrior(name)
            break
        elif re.search("mage", option, flags=re.IGNORECASE):
            hero = Mage(name)
            break
        elif re.search("archer", option, flags=re.IGNORECASE):
            hero = Archer(name)
            break
        else:
            print("\nPlease enter a valid class.")
            print("-" * 27)
            continue 
    return hero

def ask_start():
    """
    Asks the user if they are ready to begin the game.
    Exits the program if the user answers 'no'.
    """
    while True:
        answer = input("\nAre you ready to begin your battle through the maze?\n")
        if re.fullmatch("yes|y", answer, flags=re.IGNORECASE):
            break
        elif re.fullmatch("no|n", answer, flags=re.IGNORECASE):
            sys.exit("Ok. Come back when you feel ready to ")
        else:
            print("Please answer yes or no.\n")
            continue
 
def welcome_message():
    """
    Displays a series of welcome messages to introduce the player to the game mechanics.
    Waits for the user to press Enter after each message.
    """
    input("""\nWelcome to the Maze! Here you will guide your hero as they navigate their way through the monsters that block the way to the finish line.
      
Press Enter to continue.
""")
    input("""You will shortly see a display of your hero's starting location. In each cell, your hero may either encounter a monster, healing potion, treasure chest or a shopkeeper. 

Press Enter to continue.
""")
    input("""The treasure chest contains money that can be used to buy healing potions or special upgrades from the shopkeeper!

Press Enter to continue.
""")
    print("""(0,0) is your starting position.
You can move up, left, right or down, so long as you stay within the maze's boundaries.
Remember, the goal is to navigate to the bottom-right square, (4,4). Good luck!""")     


if __name__ == "__main__":
    main()
