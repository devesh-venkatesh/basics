# get library needed for random numbers
import random

# ask user for range of integers
lowerNum = int(input("Enter a lower bound: "))
higherNum = int(input("Enter a higher bound: "))

randomNumber = random.randint(lowerNum, higherNum)

guess = int(input("Enter a number between %d and %d: " %(lowerNum, higherNum)))

while randomNumber != guess:

    if guess < randomNumber:
        print ("Hint: Guess is too low! Try Again.")
        guess = int(input("Enter a number between %d and %d: " %(lowerNum, higherNum)))

    elif guess > randomNumber:
        print ("Hint: Guess is too high! Try Again.")
        guess = int(input("Enter a number between %d and %d: " %(lowerNum, higherNum)))

print ("You guessed it. Good Job!")