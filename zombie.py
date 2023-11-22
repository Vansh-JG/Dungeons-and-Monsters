from entity import Entity
import random


class Zombie(Entity):
    def __init__(self):
        self._name = "Dead Zombie"
        self._max_hp = random.randint(8, 10)
        super().__init__(self._name, self._max_hp)

    def attack(self, entity):
        damage = random.randint(5, 12)
        entity.take_damage(damage)
        return f"{self.name} attacks {entity.name} for {damage} damage!"



