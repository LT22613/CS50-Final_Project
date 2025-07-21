from game_model import *

potion = Healing_Potion()
Claire = Character("Claire", 50)
Claire.pouch[potion] = 1
Claire.heal()
print(Claire.health)