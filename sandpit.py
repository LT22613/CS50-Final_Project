from game_model import Mage, Healing_Potion

potion = Healing_Potion()
Claire = Mage("Claire", 100)

Claire.health = 50

Claire.pouch[potion] = 1
Claire.heal()
print(Claire.health)


