from game_model import *


test_Warrior = Warrior("Dodge")
print(test_Warrior.dodge_chance())
enemy_1 = Monster("Argie", random.seed(1))
enemy_2 = Monster("Bleurgh", random.seed(2))
enemy_3 = Monster("Coral", random.seed(3))
print(round(test_Warrior.hit_chance(enemy_1), 3))
print(round(test_Warrior.hit_chance(enemy_2), 3))
print(round(test_Warrior.hit_chance(enemy_3), 3))
"""
test_Mage = Mage("Dodge")
print(test_Mage.dodge_chance())
test_Archer = Archer("Dodge")
print(test_Archer.dodge_chance())
enemy = Monster("Blah")
print(enemy.dodge_chance())
"""