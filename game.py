import random

level = 0

while (level <= 0):
    try:
        level = int(input('Level: '))
    except ValueError:
        pass

number = random.randint(1,level)

while True:
    try:
        guess = int(input('Guess: '))
        if guess == number:
            print ('Just right!')
            break
        if guess > number:
            print('Too large!')
        if guess < number:
            print('Too small!')
    except ValueError:
        pass
