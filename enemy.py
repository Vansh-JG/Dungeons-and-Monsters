import entity
import random

class Enemy(entity.Entity):
    # To initialize the variale of the monsters
    def __init__(self):
        monster = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie", "Witch"]
        self._name = random.choice(monster)
        self._max_hp = random.randint(4, 8)
        self._hp = self._max_hp

    def attack(self, entity):
        damage = random.randint(1, 4)
        entity.hp -= damage
        print(f"{self._name} attacks {entity._name} for {damage} damage")