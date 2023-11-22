from entity import Entity
import random


class EasyZombie(Entity):
    def __init__(self):
        self._name = "Easy Zombie"
        self._max_hp = random.randint(4, 5)
        super().__init__(self._name, self._max_hp)

    def attack(self, entity):
        damage = random.randint(1, 5)
        entity.take_damage(damage)
        return f"{self._name} attacks {entity.name} for {damage} damage!"
