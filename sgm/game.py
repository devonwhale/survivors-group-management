from survivor import Survivor
import random

def game():
    print('Welcome to Survivors Group Management!')
    survivors = setup_survivors()
    day = 1
    while len(survivors) > 0:
        print(f'Day {day}')
        dead_survivors = []
        for survivor in survivors:
            survivor.next_day()
            if survivor.health < 0:
                print('Someone has died...')
                dead_survivors.append(survivor)
        for dead_survivor in dead_survivors:
            survivors.remove(dead_survivor)
        day += 1
    print('The outpost has fallen')

def setup_survivors():
    survivors = []
    for _ in range(10):
        survivors.append(Survivor(random.randrange(1, 100), random.randrange(1, 100)))
    return survivors

if __name__ == "__main__":
    game()