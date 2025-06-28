# 3. Distinguishing Between Class Methods and Static Methods
# mandatory
# Score: 0.0% (Checks completed: 0.0%)
# Objective: Solidify your understanding of class methods and static methods in Python by implementing examples of each in a class, demonstrating their usage and differences.

# Task Description:
# Create a Python script named class_static_methods_demo.py. In this script, define a class Calculator that includes both a class method and a static method to perform calculations. This task aims to illustrate when and how to use @classmethod and @staticmethod decorators, highlighting their differences and practical applications.

# class_static_methods_demo.py:
# Calculator Class:

# Static Method - add(a, b): Returns the sum of two numbers. Use the @staticmethod decorator.
# Class Method - multiply(cls, a, b): Returns the product of two numbers. Use the @classmethod decorator and ensure it prints a class attribute named calculation_type before performing the multiplication.
# Class Attribute:

# Define a class attribute calculation_type with a value of "Arithmetic Operations" that the multiply class method will reference.
# Implementation Example:
# class Calculator:
#     calculation_type = "Arithmetic Operations"

#     @staticmethod
#     def add(a, b):
#         return a + b

#     @classmethod
#     def multiply(cls, a, b):
#         print(f"Calculation type: {cls.calculation_type}")
#         return a * b
# main.py (Provided for Testing):
# This script will test the Calculator class’s static and class methods, demonstrating their functionality and how they are called.

# from class_static_methods_demo import Calculator

# def main():
#     # Using the static method
#     sum_result = Calculator.add(10, 5)
#     print(f"The sum is: {sum_result}")

#     # Using the class method
#     product_result = Calculator.multiply(10, 5)
#     print(f"The product is: {product_result}")

# if __name__ == "__main__":
#     main()
# Expected Output:
# When you run main.py, it should produce the following output, which includes the printed message from the class method and the results of the calculations:

# The sum is: 15
# Calculation type: Arithmetic Operations
# The product is: 50
# Note for you:
# Understand the use of @staticmethod for functions that perform a task in isolation, without needing access to class or instance-specific data.
# Grasp the concept of @classmethod for functions that need to access class attributes or methods and understand how the cls parameter allows access to class-level attributes.
# This task underscores the distinction between class methods and static methods in Python, providing clarity on their appropriate use cases and advantages.
# Repo:

# GitHub repository: alx_be_python
# Directory: oop
# File: class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")          

if __name__ == "__main__":      
    main()
# Expected Output:
# The sum is: 15            
# Calculation type: Arithmetic Operations
# The product is: 50
# Note for you:
# Understand the use of @staticmethod for functions that perform a task in isolation, without needing access to class or instance-specific data.
# Grasp the concept of @classmethod for functions that need to access class attributes or methods and understand how the cls parameter allows access to class-level attributes.
# This task underscores the distinction between class methods and static methods in Python, providing clarity on their appropriate use cases
# and advantages.
# Repo: alx_be_python   
# Directory: oop    
# File: class_static_methods_demo.py
# If this script is run directly, it will execute the main function
# If imported, the main function will not run automatically     
# This allows for testing the Calculator class without executing the main function
# This script demonstrates the use of class methods and static methods in Python.
# The Calculator class includes a static method for addition and a class method for multiplication,
# showcasing the differences between the two decorators.
# The main function tests these methods, providing a clear example of their functionality and output.
# The Calculator class is now complete with the required static and class methods.
# The main function demonstrates the functionality of the Calculator class.                 