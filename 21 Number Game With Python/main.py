# QUESTION:

# • The player can choose to start first or second.
# • The list of numbers is shown after the Player takes his turn so that it becomes convenient.
# • User only use (1, 2, 3) numbers to add in the list, other interperater tells again.
# • The player loses if he gets the chance to call 21 and wins otherwise.

# An example of (execution of Game) with explaination:

#     Player A                                      Player B 
#     (A Makes the first turn 2)                    (2 + B’s Choice, say 1) = 2+1 = 3
#     (3 + A’s Choice, say 2) = 3+2 = 5              (5 + B’s Choice, say 3) = 5+3 = 8
#     (8 + A’s Choice, say 1) = 8+1 = 9             (9 + B’s Choice, say 3) = 9+3 = 12
#     (12 + A’s Choice, say 2) = 12+2 = 14          (14 + B’s Choice, say 2) = 14+2 = 16
#     (16 + A’s choice, say 3) = 16 + 3 = 19        (19 + B’s Choice, say 2) = 19 + 2 = 20
#     21 (LOSES THE GAME)                           WINNER! WINNER!



# SOLUTION:

# If file is run from main page then, the code is run.
if __name__ == "__main__":
    
    # Importing module.
    import random as r

    # Function for user moves.
    def userMoves(num):
        # Define list of numbers.
        listOfNum = []

        # Ask user's number until the number in (1, 2, 3).
        userCho = int(input("\n> Number you wish to add (1 to 3): "))
        while userCho not in (1, 2, 3):
            print("Try again! between (1 to 3)")
            userCho = int(input("\n> Number you wish to add (1 to 3): "))
            
        # Arrange the numbers in list by for loop.
        if (userCho in (1, 2, 3)):
            for i in range(1, ((num + userCho) + 1)):
                listOfNum.append(i)

        # Print list of numbers.
        print(f"> {listOfNum}\n")

        # Return num's new value.
        return (num + userCho)

    # Function for computer moves.
    def compMoves(num):
        # Define list of numbers.
        listOfNum = []

        # Define computer's number and print it.
        compCho = r.choice(compChos)
        print(f"\n> Computer selects: {compCho}")

        # Arrange the numbers in list by for loop.
        for i in range(1, ((num + compCho) + 1)):
            listOfNum.append(i)

        # Print list of numbers.
        print(f"> {listOfNum}\n")

        # Return num's new value.
        return (num + compCho)

    # Ask user to play the game.
    STP = print("> Do you want to start the game? (y/n)")
    STP = input("> ")

    # If ["y", "yes", "Yes", "Y", "YES"] these key words are in user input so, program will run.
    if(STP in ["y", "yes", "Yes", "Y", "YES"]):

        # Define Computer moves.
        compChos = [1, 2, 3]
        # Define number.
        num = 0

        # Tell user to take First or Second chance with "F" or "S" keywords.
        print("\n> Enter 'F' to take the first chance.")
        print("> Enter 'S' to take the second chance.")

        # Ask user to take First or Second chance.
        FirstOrSecond = input("> ")

        # If user take first chance so, the code below if condition will execute.
        if FirstOrSecond in ["f", "F"]:

            # While loop for repeating the code.
            while True:

                # Redefine the value of num.
                num = userMoves(num)
                # If num's value is 21 or greater then 21, prints (You Lose) and end the game by break.
                if num >= 21:
                    print("> You Lose!")
                    break

                # Redefine the value of num.
                num = compMoves(num)
                # If num's value is 21 or greater then 21, prints (You Win) and end the game by break.
                if num >= 21:
                    print("> Congratulations! You Win")
                    break

        # If user take second chance so, the code below elif condition will execute.
        elif FirstOrSecond in ["s", "S"]:

            # While loop for repeating the code.
            while True:

                # Redefine the value of num.
                num = compMoves(num)
                # If num's value is 21 or greater then 21, prints (You Win) and end the game by break.
                if num >= 21:
                    print("> Congratulations! You Win")
                    break

                # Redefine the value of num.
                num = userMoves(num)
                # If num's value is 21 or greater then 21, prints (You Lose) and end the game by break.
                if num >= 21:
                    print("> You Lose!")
                    break

    # If user say "no" so, program will end by saying Fuck Off.
    else:
        print("> Ok, not a problem")