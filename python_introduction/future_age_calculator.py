# User Input Age Calculator
# mandatory
# Objective: Practice receiving user input in Python and perform a simple arithmetic operation to calculate the user’s age in a future year.

# Task Description:

# Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

# Instructions:

# Create a file named future_age_calculator.py.
# Prompt the user to input their current age with the question: “How old are you? ”.
# Assume the user will input a valid integer value.
# Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
# Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.
# Expected Script Flow:

# The script prompts the user for their current age.
# The user enters their age.
# The script calculates and prints how old the user will be in 2050.
# Example Interaction:

# If the user inputs 30 when prompted for their current age, the output should be:

# In 2050, you will be 57 years old.
# Repo:

# GitHub repository: alx_be_python
# Directory: python_introduction
# File: future_age_calculator.py

# Future Age Calculator
# Objective: Calculate the user's age in a future year based on their current age.
# Task Description:
# Your task is to write a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.
# Instructions:

# Create a file named future_age_calculator.py.
# Prompt the user to input their current age
current_age = int(input("How old are you? ")) # Assume the user will imput a valid integer value
# calculate how old the user will be in the year 2050
future_year = 2050
age_in_future = current_age + (future_year -2023)
# print the user's age in 2050
print(f"In {future_year}, you will be {age_in_future} years old.")
# The code above prompts the user to input their current age, calculates how old they will be in the year 2050 by adding 27 years to their current age, and prints the result in a formatted string.