from game_model import *


test_Mage = Mage("Dodge")
enemy_1 = Monster("Argie", random.seed(1))
enemy_2 = Monster("Bleurgh", random.seed(2))
enemy_3 = Monster("Coral", random.seed(3))
print(f"{round(test_Mage.hit_chance(enemy_1), 3):.3f}")
print(f"{round(test_Mage.hit_chance(enemy_2), 3):.3f}")
print(f"{round(test_Mage.hit_chance(enemy_3), 3):.3f}")
"""

print(test_Mage.dodge_chance())
test_Archer = Archer("Dodge")
print(test_Archer.dodge_chance())
enemy = Monster("Blah")
print(enemy.dodge_chance())
"""