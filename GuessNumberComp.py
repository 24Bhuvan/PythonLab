import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess=int(input(f'Enter a number between 1 and {x} '))
        if guess<random_number:
            print(f'Sorry, guess again, Too low.')
        elif guess > random_number :
            print(f'Sorry, guess again, Too high.')
    print(f'Eureka, You have guessed the number {random_number}')
guess(100)