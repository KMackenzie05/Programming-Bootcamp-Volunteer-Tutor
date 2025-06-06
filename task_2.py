# Author: Kayla Robinson, 06/06/2025

import random

'''
TASK 2: guessing game -- guess a number between 1 and 100, giving a 'higher' or 'lower'
    Approach:
        use randint to select our random number between 1 and 100
        use a while loop and if and elif for the higher or lower

        raise an exception message if the input type is invalid
'''

def guessing_game(): # no inputs to the function directly (user guesses), no function outputs (just responses based on correct or not)
    # generate a number that will be our answer
    answer = random.randint(1,100)

    correct = False # set the users guess to be false to start the while loop

    while correct is False:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("please input a valid number!")
            continue


        if guess < answer:
            print("Higher")

        elif guess > answer:
            print("Lower")
            
        else: # could use another elif guess == answer
            print("That's correct!")
            # set correct = True to stop the while loop
            correct = True

guessing_game()