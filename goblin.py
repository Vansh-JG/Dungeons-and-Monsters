from entity import Entity
import random


class Goblin(Entity):
    def __init__(self):
        self._name = "Green Goblin"
        self._max_hp = random.randint(8, 12)
        super().__init__(self._name, self._max_hp)

    def attack(self, entity):
        damage = random.randint(6, 12)
        entity.take_damage(damage)
        return f"{self.name} attacks {entity.name} for {damage} damage!"
