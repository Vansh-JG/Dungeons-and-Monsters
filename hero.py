import entity
import random
class Hero(entity.Entity):
    def __init__(self, name):
        super().__init__(name, max_hp=25)
        self.location = (0, 0)
    def attack(self, entity):
        damage = random.randint(2, 5)
        entity.take_damage(damage)
        return f"{self._name} attacks a {entity._name} for {damage} damage!"
    # To go North
    def go_north(self):
        new_loc = (self.location[0] - 1, self.location[1])
        if new_loc[0] >= 0 and new_loc[1] <= 0:
            self.location = new_loc
            return self.location
        else:
            return 'o'
        # To go South
    def go_south(self):
        new_loc = (self.location[0] + 1, self.location[1])
        if new_loc[0] >= 0 and new_loc[1] <= 0:
            self.location = new_loc
            return self.location
        else:
            return 'o'
        # To go East
    def go_east(self):
        new_loc = (self.location[0], self.location[1] + 1)
        if new_loc[0] >= 0 and new_loc[1] <= 0:
            self.location = new_loc
            return self.location
        else:
            return 'o'
        # To go West

    def go_west(self):
        new_loc = (self.location[0], self.location[1] - 1)
        if new_loc[0] >= 0 and new_loc[1] <= 0:
            self.location = new_loc
            return self.location
        else:
            return 'o'
