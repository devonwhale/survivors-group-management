from survivor import Survivor
import math
import random

def game():
    print('Welcome to Survivors Group Management!')
    print('You are the last person at your outpost that has the courage to travel outside a search for food')
    survivors = setup_survivors()
    print(f'There are {len(survivors)} people counting on you. Good luck!')
    player = Survivor(100, 100)
    day = 1
    while len(survivors) > 0:
        print(f'Day {day}')

        number_of_actions = math.floor(player.health / 10)
        print(f'You have {number_of_actions} actions available today')

        actions = []
        while sum(actions) != number_of_actions:
            print('Please provide a space separated list of how you would like to allocate your actions')
            print('1) Scavenge')
            print('2) Rest')
            actions = list(map(int, input().split()))
            if len(actions) != 2:
                actions = []

        # Scavenge
        if actions[0] > 0:
            food = math.floor(random.randrange(0, actions[0]) / 2)
            print(f'You have found {food} pieces of food')
            while player.hunger < 50 and food > 0:
                player.hunger += 7
                food -= 1
                print('You have eaten some of the food to keep your strength up')
            survivors = sorted(survivors, key = lambda s : s.hunger)
            for index, _ in enumerate(range(0, food)):
                if index >= len(survivors):
                    break
                survivors[index].hunger += 7

        # Rest
        if actions[1] > 0:
            healing_amount = actions[1] * 5
            if player.health + healing_amount >= 100:
                print('Resting has let you fully heal')
                player.health == 100
            else:
                print(f'Resting has let you regain {healing_amount} health')
                player.health += healing_amount

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