# Task Description:
# Create a Python script named temp_conversion_tool.py. This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

# Requirements:
# Define Global Conversion Factors:

# At the top of your script, define two global variables FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR to store the conversion factors (e.g., (5/9) for F to C and (9/5) for C to F, respectively).
# Implement Conversion Functions:

# Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
# Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
# Inside each function, use the respective global conversion factor to perform the conversion.
# User Interaction:

# Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
# Based on the user’s input, call the appropriate conversion function and display the converted temperature.
# If the user entered a wrong input,raise an error “Invalid temperature. Please enter a numeric value.”
# Guidance:
# Remember to access global variables using the global keyword if you need to modify them inside functions. However, for this task, you’ll only be reading their values.
# Use input validation to ensure that the user enters a valid temperature and unit.
# Example Output (Hypothetical):
# Enter the temperature to convert: 100
# Is this temperature in Celsius or Fahrenheit? (C/F): F
# 100.0°F is 37.77777777777778°C
# Or:

# Enter the temperature to convert: 0
# Is this temperature in Celsius or Fahrenheit? (C/F): C
# 0.0°C is 32.0°F
# Repo:

# GitHub repository: alx_be_python
# Directory: fns_and_dsa
# File: temp_conversion_tool.py

# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature_input = input("Enter the temperature to convert: ")
        temperature = float(temperature_input)  # Validate numeric input

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Invalid temperature. Please enter a numeric value. Error: {e}")

if __name__ == "__main__":
    main()
