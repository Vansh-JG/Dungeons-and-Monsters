import check_input
from hero import Hero
from enemy import Enemy
from map import Map

# Vansh Gandhi


name = input("What is your name, traveler? ")
hero = Hero(name)
map_instance = Map()
#The loop to ask for choice
while True:
  print(map_instance.show_map(hero.location))

  print("1. North")
  print("2. South")
  print("3. East")
  print("4. West")

  move = check_input.get_int_range("",1,4)
  if move == 1:
    location = hero.go_north()
  elif move == 2:
    location = hero.go_south()
  elif move == 3:
    location = hero.go_east()
  elif move == 4:
    location = hero.go_west()
  else:
    location = 'o'

  #
  if location == 'm':
    enemy = Enemy()
    print(f'You encountered a {enemy._name}')
    print(f'HP: {enemy._hp}/{enemy._max_hp}')
    while hero._hp > 0 and enemy._hp > 0:
      print(f'1. Attack {enemy._name}')
      print('2. Run Away')
      choice = check_input.get_int_range(1,2,"")
      if choice == 1:
        print(hero.attack(enemy))
        if enemy._hp <= 0:
          print(f'{enemy._name} has been defeated!')
          map_instance.remove_at_loc(hero.location)
          break
        print(enemy.attack(hero))
        if hero._hp <= 0:
          print('Game Over! You were defeated by the monster.')
          break
      elif choice == 2:
        print('You ran away!')
        break
  elif location == 'o':
    print("You cannot go that way...")
  elif location == 'n':
    print("There is nothing here...")
  elif location == 'i':
    print("You found a Health Potion! You drink it to restore your health.")
    hero.heal()
    map_instance.remove_at_loc(hero.location)
  elif location == 's':
    print("You are at the start of the dungeon.")
  elif location == 'f':
    print("Congratulations! You found the exit.")
    print("Game Over")
    break
