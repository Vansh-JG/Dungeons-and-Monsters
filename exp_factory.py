from enemy_factory import EnemyFactory
import random
from zombie import Zombie
from skeleton import Skeleton
from goblin import Goblin


class ExpertFactory(EnemyFactory):
    def create_random_enemy(self):
        difficult_enemies = [Zombie, Skeleton, Goblin]
        enemy_class = random.choice(difficult_enemies)
        return enemy_class()
