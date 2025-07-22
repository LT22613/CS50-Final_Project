from game_model import *


warrior = Warrior("Dodge")
enemy_1 = Monster("Argie", random.seed(1))
enemy_2 = Monster("Bleurgh", random.seed(2))
enemy_3 = Monster("Coral", random.seed(3))
print(warrior.attack(enemy_3))

"""

print(test_Mage.dodge_chance())
test_Archer = Archer("Dodge")
print(test_Archer.dodge_chance())
enemy = Monster("Blah")
print(enemy.dodge_chance())
"""