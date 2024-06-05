# QUESTION:
# Write the python script that can perform a numbers magic. The magic is tha user choose a number between 21 numbers and you tells the number to user. It is not as simple as it sounds. The numbers are generated randomly by random module and try to use if-else.



# SOLUTION:

# Importing random module.
import random

# Decorator function for adding a blank line before taking option from user.
def move_to_nextline(func):
  def get_option_func(*args, **kwargs):
    print("\n")
    return func(*args, **kwargs)
  return get_option_func

# Add move_to_nextline decorator function to get_option() function.
@move_to_nextline
# get_option() function can take only options from user and return.
def get_option(str):
  while True:
    option = input(str)
    print("\n")
    if option in ["a", "b", "c", "A", "B", "C"]:
      return option

# first_option() function can arrange numbers according to option "a" and return a, b, c.
def first_option(a, b, c):
  n = b + a + c
  a = n[0:21:3]
  print("a = ", a)
  b = n[1:21:3]
  print("b = ", b)
  c = n[2:21:3]
  print("c = ", c)
  return a, b, c

# second_option() function can arrange numbers according to option "b" and return a, b, c.
def second_option(a, b, c):
  n = a + b + c
  a = n[0:21:3]
  print("a = ", a)
  b = n[1:21:3]
  print("b = ", b)
  c = n[2:21:3]
  print("c = ", c)
  return a, b, c

# third_option() function can arrange numbers according to option "c" and return a, b, c.
def third_option(a, b, c):
  n = a + c + b
  a = n[0:21:3]
  print("a = ", a)
  b = n[1:21:3]
  print("b = ", b)
  c = n[2:21:3]
  print("c = ", c)
  return a, b, c

# main() function for running the game.
def main():
  # Get 21 random numbers.
  randomlist = random.sample(range(10, 100), 21)
  # Tell user to choose a number.
  print("Choose a number in any line and don't tell anyone\n")

  # List "a" with 7 random numbers.
  a = randomlist[0:7]
  # List "b" with 7 random numbers.
  b = randomlist[7:14]
  # List "c" with 7 random numbers.
  c = randomlist[14:21]

  # Print all three lists (a, b, c).
  print("a = ", a)
  print("b = ", b)
  print("c = ", c)

  # Get option from user by get_option() function.
  o = get_option("The number lyes in which option (a, b, c): ")

  # If user take option "a" then run below if block code.
  if (o in ["a", "A"]):
    # Arrange numbers aaording to option "a" by first_option() function.
    o_a = first_option(a, b, c)

    # Get option from user by get_option() function.
    o1 = get_option("Now the number lyes in which option (a, b, c): ")

    # If user take option "a" then run below if block code.
    if (o1 in ["a", "A"]):
      # Arrange numbers aaording to option "a" by first_option() function.
      o_a_a = first_option(o_a[0], o_a[1], o_a[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")

      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_a_a[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_a_a[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_a_a[2][3])
    
    # If user take option "b" then run below elif block code.
    elif (o1 in ["b", "B"]):
      # Arrange numbers aaording to option "b" by second_option() function.
      o_a_b = second_option(o_a[0], o_a[1], o_a[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")
      
      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_a_b[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_a_b[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_a_b[2][3])
    
    # If user take option "c" then run below elif block code.
    elif (o1 in ["c", "C"]):
      # Arrange numbers aaording to option "c" by third_option() function.
      o_a_c = third_option(o_a[0], o_a[1], o_a[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")
      
      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_a_c[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_a_c[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_a_c[2][3])
  
  # If user take option "b" then run below elif block code.
  elif(o in ["b", "B"]):
    # Arrange numbers aaording to option "b" by second_option() function.
    o_b = second_option(a, b, c)

    # Get option from user by get_option() function.
    o1 = get_option("Now the number lyes in which option (a, b, c): ")
    
    # If user take option "a" then run below if block code.
    if (o1 in ["a", "A"]):
      # Arrange numbers aaording to option "a" by first_option() function.
      o_b_a = first_option(o_b[0], o_b[1], o_b[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")
      
      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_b_a[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_b_a[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_b_a[2][3])
    
    # If user take option "b" then run below elif block code.
    elif (o1 in ["b", "B"]):
      # Arrange numbers aaording to option "b" by second_option() function.
      o_b_b = second_option(o_b[0], o_b[1], o_b[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")
      
      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_b_b[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_b_b[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_b_b[2][3])
    
    # If user take option "c" then run below elif block code.
    elif (o1 in ["c", "C"]):
      # Arrange numbers aaording to option "c" by third_option() function.
      o_b_c = third_option(o_b[0], o_b[1], o_b[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")
      
      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_b_c[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_b_c[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_b_c[2][3])
  
  # If user take option "c" then run below elif block code.
  elif(o in ["c", "C"]):
    # Arrange numbers aaording to option "c" by third_option() function.
    o_c = third_option(a, b, c)

    # Get option from user by get_option() function.
    o1 = get_option("Now the number lyes in which option (a, b, c): ")
    
    # If user take option "a" then run below if block code.
    if (o1 in ["a", "A"]):
      # Arrange numbers aaording to option "a" by first_option() function.
      o_c_a = first_option(o_c[0], o_c[1], o_c[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")
      
      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_c_a[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_c_a[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_c_a[2][3])
    
    # If user take option "b" then run below elif block code.
    elif (o1 in ["b", "B"]):
      # Arrange numbers aaording to option "b" by second_option() function.
      o_c_b = second_option(o_c[0], o_c[1], o_c[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")
      
      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_c_b[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_c_b[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_c_b[2][3])
    
    # If user take option "c" then run below elif block code.
    elif (o1 in ["c", "C"]):
      # Arrange numbers aaording to option "c" by third_option() function.
      o_c_c = third_option(o_c[0], o_c[1], o_c[2])

      # Get option from user by get_option() function.
      o2 = get_option("Ok one more time tell me the number lyes in which option (a, b, c): ")
      
      # If user take option "a" then print 4th number of option "a".
      if(o2 in ["a", "A"]):
        print("The number is", o_c_c[0][3])
      # If user take option "b" then print 4th number of option "b".
      elif(o2 in ["b", "B"]):
        print("The number is", o_c_c[1][3])
      # If user take option "c" then print 4th number of option "c".
      elif(o2 in ["c", "C"]):
        print("The number is", o_c_c[2][3])

# If running file name is "__main__" then run below main() function.
if __name__ == "__main__":
  main()