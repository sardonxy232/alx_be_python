# Personal Finance Calculator
# #advanced
# Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

# Task Description:

# You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

# Instructions:

# User Input for Financial Details:

# Prompt the user for their monthly income: “Enter your monthly income: ”.
# Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
# Calculate Monthly Savings:

# Calculate the monthly savings by subtracting monthly expenses from the monthly income.
# Project Annual Savings:

# Assume a simple annual interest rate of 5%.
# Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
# Output Results:

# Display the user’s monthly savings.
# Display the projected annual savings after including interest.
# Example Interaction:

# Enter your monthly income: 5000
# Enter your total monthly expenses: 4000
# Your monthly savings are $1000.
# Projected savings after one year, with interest, is: $12600.
# Repo:

# GitHub repository: alx_be_python
# Directory: python_introduction
# File: finance_calculator.py

# Personal Finance Calculator
# Objective: Calculate monthly savings and projected annual savings based on user input.

# Task Description:
# Your task is to create a script that calculates the user’s monthly savings based on their income and expenses, and projects these savings over a year with interest.
# Instructions:
# Create a file named finance_calculator.py.
# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))  # User input for monthly income
# Prompt the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))  # User input for monthly expenses
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses  # Monthly savings calculation
# Assume a simple annual interest rate of 5%
annual_interest_rate = 0.05  # Annual interest rate
# Calculate projected annual savings
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)  # Projected annual savings calculation
# Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")  # Display monthly savings
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")  # Display projected annual savings
# The code above prompts the user for their monthly income and expenses, calculates the monthly savings, and projects the annual savings with interest.

