# QUESTION:

# Python is a multipurpose language and one can do anything with it. Python can also be used for game development. Let’s create a simple command-line Snake-Water-Gun game without using any external game libraries like PyGame. Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI.

# Winning Rules as follows:
# Rock vs Paper-> Paper wins.
# Rock vs Scissor-> Rock wins.
# Paper vs Scissor-> Scissor wins.

# computer =      S W G
#                 0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D



# SOLUTION:

# Import randint from random module as the name of ri.
from random import randint as ri

# Inform user to play Snake Water and Gun game.
print("So lets play the Snake, Water and Gun game\n")

# Reminding rules of the Game.
print('Winning rules of the game SNAKE WATER GUN are :\n'
      + "Snake vs Water -> Snake wins \n"
      + "Water vs Gun -> Water wins \n"
      + "Gun vs Snake -> Gun wins \n")

# Options for the Game.
o = ["", "snake", "water", "gun"]

# Tells user to use key words instead of using options.
print(f"Type any one: \n 1 - {o[1]} \n 2 - {o[2]} \n 3 - {o[3]}\n")

# While loop for continues running.
while(True):

  # Computer Choice.
  # Take a random option by randint function.
  c = ri(1, (len(o)-1))
  
  # User Choice.
  # Teke user input.
  u = input("What's your move: ")
  # If user input is not integer and not in list of [1, 2, 3].
  if(not u in ["1", "2", "3"]):
    # Print try again and continue the loop.
    print("\nWrite option again!\n")
    continue
  # Turn user input type str to int.
  u = int(u)

  # Printing computer choice.
  print(f"\nComputer: {o[c]}")
  # Printing user choice.
  print(f"You: {o[u]}")

  # Result
  # If comp choice and user choice are same then print the Draw.
  if(c == u):
    print("Result: Draw\n")
  # If comp choice is snake and user choice is water then print You lose.
  elif(c == 1 and u == 2):
    print("Result: You lose\n")
  # If comp choice is water and user choice is gun then print You lose.
  elif(c == 2 and u == 3):
    print("Result: You lose\n")
  # If comp choice is gun and user choice is snake then print You lose.
  elif(c == 3 and u == 1):
    print("Result: You lose\n")
    # If above conditions are not true then print You win.
  else:
    print("Result: You win\n")