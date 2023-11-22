from entity import Entity
import random


class Skeleton(Entity):

    def __init__(self):
        self._name = "Vicious Skeleton"
        self._max_hp = random.randint(6, 10)
        super().__init__(self._name, self._max_hp)

    def attack(self, entity):
        damage = random.randint(6, 10)
        entity.take_damage(damage)
        return f"{self.name} attacks {entity.name} for {damage} damage!"
