
# Create a game stronge papaer and seager

'''1 = stronge , 2 = paper, 3 = seager'''

print('you want to play game stronge papaer seager game \n  1 = stonge\n  2 = paper\n  3 = seager\n')

f = int(input("Enter your choose (1-3): "))

import random
s = random.randint(1, 3)
print(f'Computer is choose (1-3) {s}')

def check(f, s):
    if f == s:
        print('Game is tie ')

    elif f == 1 and s == 2:
        print('Computer is win')

    elif f == 1 and s == 3:
        print('you win the match')

    elif f == 2 and s == 1:
        print('you win the match')

    elif f == 2 and s == 3:
        print('computer is win')

    elif f == 3 and s == 1:
        print('Cmputer is win the match')

    elif f == 3 and s == 2:
        print('you are win the match')

check(f, s)