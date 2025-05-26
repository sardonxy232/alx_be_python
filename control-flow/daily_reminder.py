# 4. Personal Daily Reminder
# mandatory
# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

# Task Description:

# Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

# Instructions:

# Prompt for a Single Task:

# Ask the user to input a task description and save it into a task variable
# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
# In a time_bound variable, Ask if the task is time-bound (yes or no)
# Process the Task Based on Priority and Time Sensitivity:

# Use a Match Case statement to react differently based on the task’s priority.
# Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
# Provide a Customized Reminder:

# Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
# A message should be ‘that requires immediate attention today!’
# Example Interaction and Output:

# Enter your task: Finish project report
# Priority (high/medium/low): high
# Is it time-bound? (yes/no): yes

# Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
# Or, for a non-time-bound task:

# Enter your task: Read a book
# Priority (high/medium/low): low
# Is it time-bound? (yes/no): no

# Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
# Well done on completing this project! Let the world hear about this milestone achieved.

# 🚀 Click here to tweet! 🚀

# Repo:

# GitHub repository: alx_be_python
# Directory: control-flow
# File: daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()
# Prompmt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()
# Process the task based on priority and time sensitivity
# Use Match Case to handle different priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder +=f" and can be completed later."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += "that should be addressed soon."
        else:
            reminder += "and can be completed when you have time."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that should be done when possible."
        else:
            reminder += "and can be completed when you have free time."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."
# Print the customised reminder
print(f"Reminder: {reminder}")
