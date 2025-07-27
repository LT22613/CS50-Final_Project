from game_model import *

def visit_shopkeeper(hero, shopkeeper):
    """Handle shopping interaction with the shopkeeper.
    
    Args:
        hero: The hero character doing the shopping
        shopkeeper (Shopkeeper): The shopkeeper NPC to interact with
        
    Available purchases:
    - Healing Potion (10 coins)
    - Stat Upgrade (20 coins)
    """
    while True:
        print(f"Hero has {hero.pouch["coins"]} coins.")
        print("\nWhat would you like to buy?\nA. Healing Potion (10 coins)\nB. Stat Upgrade (20 coins)\nC. Nothing")
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'a':
            if hero.pouch["coins"] >= 10:
                shopkeeper.sell_potion(hero)
                hero.pouch["potion"] += 1
                print("Healing potion added to pouch.")
                print(f"{hero.name} has {hero.pouch['coins']} coins left.")
            else:
                print("Not enough coins.")
        elif choice == 'b':
            if hero.pouch["coins"] >= 20:
                upgraded = shopkeeper.upgrade_stat(hero)
                if upgraded:
                    hero.pouch["coins"] -= 20
                    print("Stat upgraded!")
                else:
                    print("Stat already at max.")
            else:
                print("Not enough coins.")
        elif choice == 'c':
            print("You chose not to buy anything.")
            break
        else:
            print("Invalid choice.")
            
Hero = Warrior("Bob")
Hero.pouch["coins"] = 40 
Bert = Shopkeeper()

if __name__ == "__main__":
    visit_shopkeeper(Hero, Bert)
