from random import randint
from random import choice

if __name__ == '__main__':
    print(randint(1, 6))

    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    first_up = choice(players)
    print(first_up)
