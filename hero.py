import random
from entity import Entity


class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, max_hp=25)
        self._loc = [0, 0]

    @property
    def location(self):
        return self._loc

    def attack(self, entity):
        damage = random.randint(2, 5)
        entity.take_damage(damage)
        return str(f"{self._name} attacks a {entity.name} for {damage} damage.")

    def go_north(self, map_instance):
        map_instance.reveal(self._loc)
        self._loc[0] -= 1
        if self._loc[0] < 0:
            self._loc[0] = 0
            return "o"

        return map_instance[self._loc[0]][self._loc[1]]

    def go_south(self, map_instance):
        map_instance.reveal(self._loc)
        self._loc[0] += 1
        if self._loc[0] > (len(map_instance) - 1):
            self._loc[0] = len(map_instance) - 1
            return "o"

        return map_instance[self._loc[0]][self._loc[1]]

    def go_east(self, map_instance):
        map_instance.reveal(self._loc)
        self._loc[1] += 1
        if self._loc[1] > len(map_instance[self._loc[0]]) - 1:
            self._loc[1] = len(map_instance[self._loc[0]]) - 1
            return "o"
        return map_instance[self._loc[0]][self._loc[1]]

    def go_west(self, map_instance):
        map_instance.reveal(self._loc)
        self._loc[1] -= 1
        if self._loc[1] < 0:
            self._loc[1] = 0
            return "o"
        return map_instance[self._loc[0]][self._loc[1]]
