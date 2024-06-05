# QUESTION:

# You are a Pokémon trainer. Each Pokémon has its own power, described by a positive integer value. As you travel, you watch Pokémon and you catch each of them. After each catch, you have to display maximum and minimum powers of Pokémon caught so far. You must have linear time complexity. So sorting won’t help here. Try having minimum extra space complexity. Examples: Suppose you catch Pokémon of powers 3 8 9 7.
# Then the output should be:    3 3 
#                               3 8
#                               3 9
#                               3 9

# Input : 
# The single line describing powers of N Pokémon caught. 

# Output : 
# N lines stating minimum power so far and maximum power so far separated by single space.



# SOLUTION:

# Make a list of numbers(powers) by the name of powers.
powers = [3, 8, 9, 7] 

# Describing minimum-power and maximum-power variables with the name of mini and maxi respectively.
mini, maxi = 0, 0

# For loop for taking a number from list of powers.
for power in powers: 

	# If the value of minimum-power and maximum-power variables is 0, So below code is executed.
	if mini == 0 and maxi == 0: 

		# Changing the value of both variables by slicing.
		mini, maxi = powers[0], powers[0] 

		# Printing values of minimum-power and maximum-power variables.
		print(mini, maxi) 

	# If the value of minimum-power and maximum-power variables is not 0, So below code is executed.
	else:

		# Changing the value of mini variable by min built-in function.
		mini = min(mini, power) 
		# Changing the value of maxi variable by max built-in function.
		maxi = max(maxi, power) 

		# Printing values of minimum-power and maximum-power variables.
		print(mini, maxi) 
		
# Time Complexity is O(N) with Space Complexity O(1).