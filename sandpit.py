from game_model import *

test_Warrior = Warrior("Dodge")
print(test_Warrior.dodge_chance())
test_Mage = Mage("Dodge")
print(test_Mage.dodge_chance())
test_Archer = Archer("Dodge")
print(test_Archer.dodge_chance())
enemy = Monster("Blah")
print(enemy.dodge_chance())
