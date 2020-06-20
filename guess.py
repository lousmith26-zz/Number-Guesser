import random

r = random
num = r.randint(0, 10)

guess = 50

while guess != num:
    guess = int(input('Guess the number I am thinking of: '))

    if guess == num:
        print('CORRECT!')
        exit(0)
    elif guess < num:
        print('Your guess should be higher.')
    elif guess > num:
        print('Your guess should be lower.')