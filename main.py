import check_input
from hero import Hero
from map import Map
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory

# Vansh J Gandhi
# OOP
# Asks the user for their name and the level of difficulty they want to choose
name = input("What is your name, traveler? ")
print("Difficulty:")
print("1. Beginner")
print("2. Expert")
difficulty_lvl = check_input.get_int_range("", 1, 2)

# Makes a Hero object and Map object
hero = Hero(name)
m = Map()
map_counter = 1

# For easy level:
if difficulty_lvl == 1:
    fac = BeginnerFactory()
# for expert level
else:
    fac = ExpertFactory()

# Checks if the player has health to play further
while hero.hp > 0:
    print(hero)
    m.show_map(hero.location)
    print("1. North")
    print("2. South")
    print("3. East")
    print("4. West")
    print("5. Quit")

    user_choice = check_input.get_int_range("Enter choice: ", 1, 5)

    # Updates the player's location on the map
    if user_choice == 1:
        location = hero.go_north(m)

    elif user_choice == 2:
        location = hero.go_south(m)

    elif user_choice == 3:
        location = hero.go_east(m)

    elif user_choice == 4:
        location = hero.go_west(m)

    else:
        print("Thanks for playing. Goodbye!!!")
        break

    # If the player encounters a monster
    if location == 'm':
        enemy = fac.create_random_enemy()
        print(f'You encountered a {enemy.name}')
        print(enemy)
        while hero.hp > 0 and enemy.hp > 0:
            print(f'1. Attack {enemy.name}')
            print('2. Run Away')
            choice = check_input.get_int_range("", 1, 2)
            if choice == 1:
                print(hero.attack(enemy))
                if enemy.hp <= 0:
                    print(f'{enemy.name} has been defeated!')
                    m.remove_at_loc(hero.location)
                    break
                print(enemy.attack(hero))
                if hero.hp <= 0:
                    print('Game Over! You were defeated by the monster.')
                    break
            elif choice == 2:
                print('You ran away!')
                if user_choice == 1:
                    hero.go_south(m)
                elif user_choice == 2:
                    hero.go_north(m)
                elif user_choice == 3:
                    hero.go_west(m)
                elif user_choice == 4:
                    hero.go_east(m)
                break

    # To tell player that it cannot go out the wrong direction.
    elif location == 'o':
        print("You cannot go that way...")
    # If player encounters nothing
    elif location == 'n':
        print("There is nothing here...")
    # When the player drinks the health potion
    elif location == 'i':
        print("You found a Health Potion! You drink it to restore your health.")
        hero.heal()
        m.remove_at_loc(hero.location)
    # That is the start position on the map
    elif location == 's':
        print("You are at the start of the dungeon.")
    # That is the finish position
    elif location == 'f':
        print("Congratulations! You found the exit and has been promoted to the next level.")
        map_counter += 1
        if map_counter == 4:
            map_counter = 1
        m.load_map(map_counter)
