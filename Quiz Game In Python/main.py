# QUESTION:

# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game, And add more things you want to make the game better.



# SOLUTION:

# Rules of game.
rules = ["1. You have only 3 life lines, If you lost it your game is over.", 
  "2. There is total 5 rounds", 
  "3. After every round your amount will be safed", 
  "4. If you want to quit, You can by just type 'exit'"
  ]

# Questions, answer, and options of game.
Quiz = [
  [
    "Q1. Who is the prime minister of pakistan in 2020?", "b", "Nawaz Sharif", "Imran Khan", "Arif Alvi", "Bilawal Bhutto"
  ], 
  [
    "Q2. Who is the lead actor of John Wick series?", "d", "Donnie Yen", "John Leguizamo", "Ian McShane", "Keanu Reeves"
  ], 
  [
    "Q3. When was the first world war started?", "b", "August 11, 1956", "July 28, 1914", "March 29, 1884", "October 3, 1818"
  ], 
  [
    "Q4. Who invented the lightbulb?", "a", "Thomas Edison", "Alessandro Cruto", "Marie Curie", "Albert Einstein"
  ], 
  [
    "Q5. Which programing language was used to create fb?", "d", "Python", "French", "JavaScript", "Php"
  ], 
  [
    "Q6. How many minutes are in a full week?", "a", "10,080", "9,560", "10,880", "11,240"
  ], 
  [
    "Q7. What game studio makes the GTA series?", "c", "iTechArt", "Epic Games", "Rockstar Games", "Nintendo"
  ], 
  [
    "Q8. Which planet has the most moons?", "b", "Saturn", "Jupiter", "Neptune", "Uranus"
  ], 
  [
    "Q9. What Netflix show had the most streaming views in 2021?", "a", "Squid Game", "Welcome to Eden", "Shadow and Bone", "Outer Banks"
  ], 
  [
    "Q10. What is the world's fastest bird?", "d", "Goose", "Macaw", "Vulture", "Peregrine Falcon"
  ]
]

# Levels of game.
levels = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]

# Declaring money variable by 0.
money = 0

# Declaring safeAmount variable by 0.
safeAmount = 0

# Declaring lifeLine variable by 3.
lifeLine = 3

# Declaring spaceLength variable by 18.
spaceLength = 18

# Declaring spaceChr variable by empty string.
spaceChr = " "

# Print welcome message.
print("Welcome to the RaDin's Quiz Game !!!")

# Get user name convert it into title format.
name = input("\nWhat is your name: ").title()

# Tell user that they want to play or not.
userInteraction = input(f"\n{name} do you want to play (y/n): ")

# Move to next line.
print("\n")

# If user want to play then run below if block code.
if(userInteraction in ["yes", "y"]):
  # Print rules of game.
  print("Rules: ")
  for r in rules:
    print(r)
  
  # Move to next line.
  print("\n")
  
  # For loop for showing each round, question and their options.
  for c in range(0, len(Quiz)):

    # Every round has 2 questions. So, print round according to the number of question.
    if(c == 0):
      print("Round 1\n")
    elif(c == 2):
      print("Round 2\n")
    elif(c == 4):
      print("Round 3\n")
    elif(c == 6):
      print("Round 4\n")
    elif(c == 8):
      print("Round 5\n")
    
    # Tell user about prize for question.
    print(f"Question for Rs.{levels[c]}\n")
    
    # Declaring question vairable with a question
    question = Quiz[c]
    
    # Find number of spaces between a and b options accourding to their lengths.
    space1Length = spaceLength - len(question[2])
    # Find number of spaces between c and d options accourding to their lengths.
    space2Length = spaceLength - len(question[4])

    # Set spaces between option a and option b.
    space1 = spaceChr.center(space1Length, " ")
    # Set spaces between option c and option d.
    space2 = spaceChr.center(space2Length, " ")
    
    # Showing question.
    print(question[0])
    # Showing options of queston with required spaces.
    print(f"a. {question[2]}{space1}b. {question[3]}")
    print(f"c. {question[4]}{space2}d. {question[5]}")
    
    # Get user's answer.
    reply = input("Ans. What is the right option: ")
    
    # If user's answer is correct then run below if block code.
    if(reply == question[1]):
      # Add winning money to safeAmount variable.
      safeAmount = safeAmount + levels[c]
      
      # Tell user that they choose correct option with their name and how much money he/she win.
      print(f"Correct answer, {name} you have won Rs.{levels[c]}\n")
      
      # After passing each round tell user that how much safe money he/she has, And add safe amount to money variable.
      if(c == 1):
        money = safeAmount
        print(f"Great you passed the round 1, Your safe ammount is Rs.{money}\n")
      elif(c == 3):
        money = safeAmount
        print(f"Great you passed the round 2, Your safe ammount is Rs.{money}\n")
      elif(c == 5):
        money = safeAmount
        print(f"Great you passed the round 3, Your safe ammount is Rs.{money}\n")
      elif(c == 7):
        money = safeAmount
        print(f"Great you passed the round 4, Your safe ammount is Rs.{money}\n")
      elif(c == 9):
        money = safeAmount
        print(f"Great you passed the round 5, Your safe ammount is Rs.{money}\n")
    
    # If user type exit then run below if block code.
    elif(reply == "exit"):
      money = safeAmount
      print("\n")
      break
    
    # If user's answer is wrong then run below if block code.
    else:
      # Minus 1 life line of user.
      lifeLine = lifeLine - 1
      
      # If user has 2 life lines then tell user that he/she has 2 life lines.
      if(lifeLine == 2):
        print(f"Wrong answer, {name} your one life line has lost, Now you have 2 more life lines\n")
      # If user has 1 life lines then tell user that he/she has 1 life lines.
      elif(lifeLine == 1):
        print(f"Wrong answer, {name} your one more life line has lost, Now you have only 1 life line\n")
      # If user has 0 life lines then tell user that his/her all 3 life lines are finished and end the game.
      elif(lifeLine == 0):
        print(f"Wrong answer, {name} your last life line has lost\n")
        break
      
      # After passing each round tell user that how much safe money he/she has, And add safe amount to money variable.
      if(c == 1):
        money = safeAmount
        print(f"Great you passed the round 1, Your safe ammount is Rs.{money}\n")
      elif(c == 3):
        money = safeAmount
        print(f"Great you passed the round 2, Your safe ammount is Rs.{money}\n")
      elif(c == 5):
        money = safeAmount
        print(f"Great you passed the round 3, Your safe ammount is Rs.{money}\n")
      elif(c == 7):
        money = safeAmount
        print(f"Great you passed the round 4, Your safe ammount is Rs.{money}\n")
      elif(c == 9):
        money = safeAmount
        print(f"Great you passed the round 5, Your safe ammount is Rs.{money}\n")
        
  # Tell user that how much money he/she wins and taking to home.
  print(f"Congratulation your take home money is Rs.{money}")

# If user don't want to play then run below else block code.
else:
  # Saying not a problem to user.
  print("Ok, not a problem.")