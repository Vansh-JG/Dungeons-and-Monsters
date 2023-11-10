from abc import abstractmethod
class Entity:
    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    def take_damage(self, dmg):
        self._hp = self._hp - dmg
        if self._hp < 0:
            self._hp = 0
    def heal(self):
        self._hp = self._max_hp
    def __str__(self):
        return str(f"{self._name}\nHP: {self._hp}/{self._max_hp}")
    @abstractmethod
    def attack(self,entity):
        pass




