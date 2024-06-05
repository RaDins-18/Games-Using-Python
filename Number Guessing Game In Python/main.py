# QUESTIONL:

# • Build a Number guessing game, in which the user selects a range.
# • Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# • Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses.



# SOLUTION:

# Importing randrange from random module.
from random import randrange as rr

# Taking Inputs.
userInput1 = int(input("Minimum number: "))
userInput2 = int(input("Maximum number: "))

# generating random number between the minimum and maximum.
randomNumber = rr(userInput1, userInput2)
# print(f"\nThe correct answer is {randomNumber}\n") # If you want to cheating, So uncomment it.

# Number of guesses.
print("\tTotal Number of Guesses = 7")

# Loop for 7 guesses.
for i in range(1, 9):
    # If all Guesses are remained, shows this output.
    if(i <= 7):
        userInput3 = int(input("Guess the number: "))

        # Condition testing.
        if(userInput3 == randomNumber):        
            print(f"Congratulations, you did it in {i} trys.\n")
            # Once guessed, loop will break.
            break

        # Condition testing.
        elif(userInput3 > randomNumber):
            print(f"Try Again! You guessed too high, {7-i} guesses left.\n")

        else:
            print(f"Try Again! You guessed too small, {7-i} guesses left.\n")
    
    # If all Guesses are used, shows this output.
    else:
        print(f"The number is {randomNumber}.")
        print("\tBetter Luck Next time!")