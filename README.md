# Mazes and Monsters
#### Video Demo:  <URL HERE>

**Mazes and Monsters** is a text-based simulation game where a player navigates through a maze, starting at the top-left corner and aiming to reach the bottom-right. Along the way, the player encounters monsters, treasure chests, and shopkeepers—all while managing health, resources, and survival!

## Game Features

- **Maze Adventure:** Traverse a maze from start to finish.
- **Character Classes:** Choose to play as a **Warrior**, **Mage**, or **Archer**—each based on a common `Character` class, but with unique strengths.
- **Dynamic Encounters:** Each maze cell may contain nothing, a monster (combat!), a treasure chest (loot!), a healing potion or a shopkeeper (trade!).
- **Resource & Combat Management:** Survive monster attacks, collect coins, and use items to stay alive.

## Object-Oriented Structure

### Main Classes

- **Game:**  
  Controls the main game flow, including the prompting sequence and user interface for playing the game.

### Character System

- **Player Classes:**  
  - **Warrior**
  - **Mage**
  - **Archer**

  All three inherit from the base `Character` class, which defines:

  - **Attributes:**  
    - `name`  
    - `health`  
    - `max_health`  
    - `power`  
    - `defence`  
    - `stealth`  
    - `accuracy`  
    - `coins'
    - 'potions'
  - **Methods:**  
    - `dodge_chance()`: Calculates chance to dodge attacks.
    - `hit_chance()`: Determines accuracy of attacks.
    - `attack()`: Executes an attack on a monster.
    - `heal()`: *(Class method)* Heals the player by a certain number of health points, a limited number of times.
    - `empty_chest()`: *(Class method)* Collects coins from a `Treasure_Chest`.

### Game Objects

- **Treasure_Chest:**  
  Contains coins. The player can empty the chest into their pouch using the `empty_chest()` class method of `Character`.

- **HealingPotion:**  
  An item that can be used by the player to restore health.

## How to Run

1. **Clone or download** this repository to your local machine.
2. **Open your IDE** and navigate to the project folder.
3. **Run the following command in your terminal:**

   ```bash
   python project.py
   ```

4. **Follow the in-game prompts** to select your character and play.

## Requirements

- Python 3.x  
- *No external libraries are required.*

## Credits

- Developed by Rafi Davis
- Partial help from ChatGPT
- 
---

Enjoy braving the maze as a mighty Warrior, cunning Mage, or sly Archer!
