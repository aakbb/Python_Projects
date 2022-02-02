import random
import time

random_number = random.randint(1,40)
guess_right = 7

while True:
    guess = int(input("Your Guess: "))
    if guess < random_number:
        print("Checking İnformations...")
        time.sleep(1)
        print("Enter a number bigger than that")
        guess_right -=1
    elif guess > random_number:
        print("Checking İnformations...")
        time.sleep(1)
        print("Enter a number smaller than that")
        guess_right -=1
    elif guess == random_number:
        print("Congratulations. You found the number :D ")
        break
    else:
        print("Invalid Value. Please enter a number between 1-40")
    
    if guess_right == 0:
        print("Your guess is over. Number was : " , random_number)
        break