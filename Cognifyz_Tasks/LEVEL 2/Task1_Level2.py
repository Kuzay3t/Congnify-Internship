# This is taks 1 of Level 2
# The excercise is to create a guessing game for the user

import random 

generated_number = random.randint(1,100)

while True:
    user_guess = int(input("Guess a Number: \n"))

    if user_guess == generated_number:
        print("Congratulations! You have guessed the number correctly")
        break
    elif user_guess > generated_number:
        print("Your guess is higher than the generated number")
    elif user_guess < generated_number:
        print("Your guess is lower than the generated number")

#print(generated_number)

