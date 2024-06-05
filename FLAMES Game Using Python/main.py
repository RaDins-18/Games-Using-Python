# QUESTION:

# FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling. This game does not accurately predict whether or not an individual is right for you, but it can be fun to play this with your friends.

# Following are the steps in this game:

# • Take the two names.
# • Remove the common characters with their respective common occurrences.
# • Get the count of the characters that are left .
# • Take FLAMES letters as [“F”, “L”, “A”, “M”, “E”, “S”]
# • Start removing letter using the count we got.
# • The letter which last the process is the result.

# Example : 
#           Input :   player1 name : AJAY
#                     player2 name : PRIYA
#           Output :  Relationship status : Friends

# Explanation: In above given two names A and Y are common letters which are occurring one time(common count) in both names so we are removing these letters from both names. Now count the total letters that are left here it is 5. Now start removing letters one by one from FLAMES using the count we got and the letter which lasts the process is the result.

# Counting is done in anti-clockwise circular fashion.
# FLAMES 
# counting is start from F, E is at 5th count so we remove E and start counting again but a this time start from S. 
# FLAMS 
# M is at 5th count so we remove M and counting start from S. 
# FLAS 
# S is at 5th count so we remove S and counting start from F. 
# FLA 
# L is at 5th count so we remove L and counting start from A. 
# FA 
# A is at 5th count so we remove A. now we have only one letter is remaining so this is the final answer. 
# F 
# So, the relationship is F i.e. Friends .



# SOLUTION:

# Function for getting simple name without spaces, capital letters and numbers.
def get_simple_name_with_no_num(NAME):
    # Get name of user.
    name = input(NAME)
    # Remove space and change capital letters to lower letters.
    name = name.lower().replace(" ", "")

    # While loop for getting only alphabets.
    while True:
        # If name has only alphabets.
        if name.isalpha() == True:
            # Return name.
            return name
        
        # If name has numbers.
        else:
            # Remind user to use only aphabets.
            print("\nUse only alphabets!")
            # Again get user name.
            name = input(NAME)
            # Again remove space and change capital letters to lower letters.
            name = name.lower().replace(" ", "")

# Function for removing common letters in name.
def remove_common_chr(f_name, s_name):

    # Define empty string for final first name.
    final_fn = ""
    # Define empty string for final second name.
    final_sn = ""

    # For loop for remove common letters in first name.
    for i in f_name:
        # If a character of first name not in second name.
        if i not in s_name:
            # Add character to final_fn string.
            final_fn += i

    # For loop for remove common letters in second name.
    for i in s_name:
        # If a character of second name not in first name.
        if i not in f_name:
            # Add character to final_sn string.
            final_sn += i

    # Define a varible that joins final_fn and final_sn.
    joint_name = final_fn + final_sn

    # Return joint_name.
    return joint_name

# List of FLAMES game's result.
result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

# If file is running from main page.
if __name__ == "__main__":
    
    # Define final_word variable that has name without common characters, spaces and numbers.
    final_word = remove_common_chr(get_simple_name_with_no_num("First Name: "), get_simple_name_with_no_num("Second Name: "))

    # Length of final word.
    count = len(final_word)

    # While loop for getting result.
    while len(result) > 1:

        # Define sub_word_will_be variable that is index of word in result list that will be subtracted.
        sub_word_will_be = (count % len(result) - 1)

        # If sub_word_will_be is greater than and equal to zero.
        if sub_word_will_be >= 0:
 
            # Slicing of result variable.
            # Define left variable that has words before index of sub_word_will_be.
            left = result[: sub_word_will_be]
            # Define right variable that has words after index of sub_word_will_be.
            right = result[sub_word_will_be + 1:]

            # Redefine result variable by join right and left variables.
            result = right + left
 
        # If sub_word_will_be is less than zero.
        else:
            # Redefine result variable by slicing.
            result = result[: len(result) - 1]
 
    # Print final result.
    print("Relationship status :", result[0])