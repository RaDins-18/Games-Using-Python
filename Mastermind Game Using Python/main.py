# QUESTION:

# Given the present generation’s acquaintance with gaming and its highly demanded technology, many aspire to pursue the idea of developing and advancing it further. Eventually, everyone starts at the beginning. Mastermind is an old code-breaking game played by two players. The game goes back to the 19th century and can be played with paper and pencil. 

# Rules of the game

# Two players play the game against each other; let’s assume Player 1 and Player 2.
# • Player 1 plays first by setting a multi-digit number.
# • Player 2 now tries his first attempt at guessing the number.
# • If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
# • The game continues till Player 2 eventually is able to guess the number entirely.
# • Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
# • If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
# • If not, then Player 2 wins the game.
# • The real game, however, has proved aesthetics since the numbers are represented by color-coded buttons.



# SOLUTION:

# Importing random module as r.
import random as r

# Make a function that checks user input is a integer and 4 deigits number and returns that.
def userInput(str):
    # Taking user input.
    userInput = input(f"\n{str}: ")

    # While loop for checking the number is integer and also length of digits is 4.
    while len(userInput) != 4 or userInput.isnumeric() != True:
        # Again taking user input.
        userInput = input(f"\n{str}: ")
    
    # Return userInput.
    return userInput

# Defining a list, The (number of turns) take to guess the number for both players.
numOfTurns = [0, 0]

# For loop for turn of both players
for n in range(0, 2):
    
    # The .randrange() function generates a random number within the specified range.
    num = str(r.randrange(1000, 10000))

    # Print which player's turn.
    print(f"\n!!! Player {n+1}'s Turn !!!")

    # Defining UI variable by userinput function.
    UI = userInput("Guess the 4 digit number")

    # Defining a empty string variable for digits.
    strDigits = ""

    # Defining a list for digits.
    digits = ["X", "X", "X", "X"]

    # While X is present in digits this loop will execute.
    while "X" in  digits:
        # Defing a variable with index name.
        index = 0

        # Defining a variable that used to show the number of correct guess or guesses.
        numOfCorrectGuess = 0

        # For loop to checks the user input is matching with digits and change X with correct guess.
        for i in UI:
            # If i is equal to num[index += 1], the code below if condition will execute.
            if i == num[index]:
                # Changing X in digits with correct guess.
                digits[index] = num[index]
                # Increment 1 in (number of correct guesses) variable.
                numOfCorrectGuess += 1

            # Increment 1 in index variable.
            index += 1
        
        # For loop for adding digits in string variable.
        for i in digits:
            # Add i as string in strdigits variable.
            strDigits += f"{i} "

        # If X is present in digits the code below the if condition will execute.
        if "X" in digits:
            # Printing number of right guesses.
            print(f"You did {numOfCorrectGuess} digit(s) correct!")

            # Printing string digits.
            print(strDigits)

            # Redefine strDigits to empty string variable.
            strDigits = ""

            # Defining UI variable again by userinput function.
            UI = userInput("Enter your next choice of numbers")

        # If X is not present in digits the code under the else condition will execute.
        else:
            # Greating the user.
            print("Congratulations you did it!")

        # Increment 1 in numOfTurns variable.
        numOfTurns[n] += 1

    # Prints that player (1 or 2) takes (number of turns) turns to guess the (string digits).
    print(f"\nPlayer {n+1} takes {numOfTurns[n]} turns to guess {strDigits}.")

# If player 1 guess the digits in less turns as compare to player 2, Code below the if condition will execute.
if numOfTurns[0] < numOfTurns[1]:
    # Print Greating for player 1.
    print("Player 1 is a real Mastermind!")

# If player 1's number of guess and player 2's number of guess are same, Code below the elif condition will execute.
elif numOfTurns[0] == numOfTurns[1]:
    # Print the game is draw.
    print("Game is draw.")

# If player 2 guess the digits in less turns as compare to player 1, Code below the else condition will execute.
else:
    # Print Greating for player 2.
    print("Player 2 is a real Mastermind!")