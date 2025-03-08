from survivor import Survivor
import math
import random

def game():
    print('Welcome to Survivors Group Management!')
    survivors = setup_survivors()
    player = Survivor(100, 100)
    day = 1
    while len(survivors) > 0:
        print(f'Day {day}')

        number_of_actions = math.floor(player.health / 10)
        print(f'You have {number_of_actions} actions available today')

        dead_survivors = []
        for survivor in survivors:
            survivor.next_day()
            if survivor.health <= 0:
                print('Someone has died...')
                dead_survivors.append(survivor)
        for dead_survivor in dead_survivors:
            survivors.remove(dead_survivor)
        day += 1
        player.next_day()

        if player.health <= 0:
            print('You have fallen. Without you the outpost will not last...')
        if len(survivors) == 0:
            print('There is no-one left for you to look after at the outpost...')
    print(f'The outpost has fallen after {day} days')

def setup_survivors():
    survivors = []
    for _ in range(10):
        survivors.append(Survivor(random.randrange(1, 100), random.randrange(1, 100)))
    return survivors

if __name__ == "__main__":
    game()