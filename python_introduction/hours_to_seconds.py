# Convert Hours to Seconds
# mandatory
# Objective: Demonstrate understanding of variable assignments and arithmetic operations by converting a given number of hours into seconds.

# Task Description:

# For this task, write a Python script that converts a specific number of hours into seconds. This task reinforces the concept of arithmetic operations within a practical context.

# Instructions:

# Create a file named hours_to_seconds.py.
# Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
# Calculate the number of seconds in the given hours. Remember, there are 3600 seconds in an hour (since there are 60 minutes in an hour and 60 seconds in a minute, thus 60 x 60 = 3600).
# Store the result of the conversion in a variable named seconds.
# Print the result in the format: [hours] hour(s) is [seconds] seconds.
# Expected Output:

# Given the value hours = 2, your script should output:

# 2 hour(s) is 7200 seconds.
# Repo:

# GitHub repository: alx_be_python
# Directory: python_introduction
# File: hours_to_seconds.py

# Convert Hours to Seconds
# Objective: Convert a given number of hours into seconds.
# Task Description:

# Your task is to write a Python script that converts a specific number of hours into seconds. This task reinforces the concept of arithmetic operations within a practical context.
# Instructions:
# Create a file named hours_to_seconds.py.
# Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
hours = 2  # Number of hours to convert

# Calculate the number of seconds in the given hours
seconds = hours * 3600

# Print the result
print(f"{hours} hour(s) is {seconds} seconds.")
# The code above defines a variable named hours with the value 2, representing the number of hours to convert.
# It then calculates the number of seconds in the given hours by multiplying hours by 3600 (the number of seconds in an hour) and prints the result in a formatted string.