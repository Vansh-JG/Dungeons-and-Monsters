from enemy_factory import EnemyFactory
import random
from easy_zombie import EasyZombie
from easy_skeleton import EasySkeleton
from easy_goblin import EasyGoblin


class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        easy_enemies = [EasyZombie, EasySkeleton, EasyGoblin]
        enemy_class = random.choice(easy_enemies)
        return enemy_class()
