from time import time
from game_model import *

Bob = Warrior("Bob")
print(Bob.stealth)

Sally = Mage("Sally")
print(Sally.stealth)

Meg = Archer("Meg")

count = 0
for _ in range(1000):
    Enemy = Monster()
    if Meg.attack_chance(Enemy) > 0.5:
        count += 1
print(count)