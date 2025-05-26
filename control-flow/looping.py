# Challenge: Nested Loop Art!
# Let’s create some text-based art using nested loops! Here’s the idea:

# You’ll write a program that uses nested while loops to print a pyramid pattern of asterisks (*).
# Steps:
# Define the height of the pyramid (number of rows) as a variable, for example: rows = 5.
# Use nested while loops to achieve the following:
# The outer loop will control the number of rows.
# The inner loop will print spaces and then asterisks in each row, creating a triangular shape.
# Remember to adjust the number of spaces and asterisks printed within the inner loop based on the current row number to form the pyramid.
# Example Output (for rows = 5):

#     *
#    ***
#   *****
#  *******
# *********

# Define the height of the pyramid
rows = 5 
# Outer Loop for each row
row = 0
while row < rows:
    # Inner Loop for spaces
    space = 0
    while space < rows - row - 1:
        print(" ", end="")
        space += 1

    # Inner Loop for asterisks
    asterisks = 0
    while asterisks < 2 * row + 1:
        print("*", end="")
        asterisks += 1
    # Move to the next line after each row
    print()
    row += 1
# The pyramid pattern is now printed usiing nested while loops.
# The pyramid pattern is now printed using nested while loops.