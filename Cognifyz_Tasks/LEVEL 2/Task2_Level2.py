# This is taks 2 of Level 2
# The excercise is to create a guessing game for the user

import random 

while True:
    try:
        user_guess = int(input("Guess a Number: \n"))
        generated_number = random.randint(1,50)
        
        if user_guess > generated_number:
            print("Your guess is greater than the generated number")
        elif user_guess < generated_number:
            print("Your guess is lower than the generated number")
        else:
            print("Congratulations! You have guessed the number correctly")
            break
    except ValueError:
        print("Please enter a valid number")
        continue

    #print(generated_number)
