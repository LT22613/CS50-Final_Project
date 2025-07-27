from game_model import *
from game_interface import *
from maze import Maze
import sys

def main():
    """The main function will execute all the functions required to run the game.
    """
    # Initialise the game interface by introducing the user to the game.
    begin_game()
    # Allow the user to create a Hero to play the game with.
    hero = create_hero()
    # Ask user if they want to begin the game.
    ask_start()
    # Run the initial welcome message to the user, introducing the gameplay.
    welcome_message()
    # Create a game_instance using the hero and grid created.
    game_instance = Game(hero)
    
    # Ask the player what they would like to do.
    while True:
        game_instance.prompt_user()
        
def begin_game():
        print("Welcome to Mazes and Monsters!\n")
        answer = input("Are you ready to begin? Yes or No.\n")
        if re.fullmatch("yes|y", answer, flags = re.IGNORECASE):
            pass
        else:
            raise QuitGameException

def create_hero():
    while True:
        name = input("\nPlease choose a name for your Hero\n").capitalize()
        if name == "":
            continue
        else:
            break
        
    while True:
        option = input("\nPlease select which class you would like your Hero to be: Warrior/Mage/Archer\n")
        
        if re.search("warrior", option, flags=re.IGNORECASE):
            hero = Warrior(name)
            break
        elif re.search("mage", option, flags=re.IGNORECASE):
            hero = Mage(name)
            break
        elif re.search("archer", option, flags = re.IGNORECASE):
            hero = Archer(name)
            break
        else:
            print("\nPlease enter a valid class.")
            print("-" * 27)
            continue 
    return hero

def ask_start():
    while True:
        answer = input("\nAre you ready to begin your battle through the maze?\n")
        if re.fullmatch("yes|y", answer, flags = re.IGNORECASE):
            break
        elif re.fullmatch("no|n", answer, flags = re.IGNORECASE):
            sys.exit("Ok. Come back when you feel ready to ")
        else:
            print("Please answer yes or no.\n")
            continue
 
def welcome_message():
    input("""\nWelcome to the Maze! Here you will guide your hero as they navigate their way through the monsters that block their way to the finish line.
      
Press Enter to continue.
""")
    input("""You will shortly see a display of your hero's starting location. In each cell, your hero may either encounter a monster, healing potion, treasure chest or a shopkeeper. 

Press Enter to continue.
""")
    input("""The treasure chest contains money that can be used to buy healing potions or special upgrades from the shopkeeper!

Press Enter to continue.
""")
    print("""This is your starting position. The H represents your hero's current position.
You can move up, left, right or down, so long as you stay within the maze's boundaries.
Remember, the goal is to navigate to the bottom-right square. Good luck!""")     




if __name__ == "__main__":
    main()
