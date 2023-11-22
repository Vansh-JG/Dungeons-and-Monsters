from entity import Entity
import random


class EasySkeleton(Entity):
    def __init__(self):
        self._name = "Easy Skeleton"
        self._max_hp = random.randint(3, 4)
        super().__init__(self._name, self._max_hp)

    def attack(self, entity):
        damage = random.randint(1, 4)
        entity.take_damage(damage)
        return f"{self._name} attacks {entity._name} for {damage} damage!"
