# Welcome to Python: A Beginner's Guide

print("Hello, world!")

name = "Alice"
age = 25

for i in range(5):
    print("Hello, Python!")

x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Example 1: Working with Lists

# Define a list of fruits
fruits = ["apple", "banana", "orange", "grape", "pineapple"]

# Print each fruit in the list
for fruit in fruits:
    print(fruit)


# This code defines a list of fruits and then iterates over each fruit in the list, printing it out one by one.

# Example 2: Using Functions

# Define a function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area


# Call the function with specific values for length and width
result = calculate_area(5, 3)
print("The area of the rectangle is:", result)
# This code defines a function called calculate_area that takes two parameters, length and width, and returns the area of a rectangle. It then calls the function with specific values for length and width and prints out the result.

# Example 3: Working with Strings

# Define a string
sentence = "Python programming is fun!"

# Print the length of the string
print("Length of the string:", len(sentence))

# Print the string in uppercase
print("Uppercase:", sentence.upper())

# Print the string in lowercase
print("Lowercase:", sentence.lower())

# Check if the string contains a specific substring
if "programming" in sentence:
    print("The string contains 'programming'")
else:
    print("The string does not contain 'programming'")
# ous operations that can be performed on strings, such as finding the length, converting to uppercase and lowercase, and checking for the presence of a substring.


# Example 4: Working with Dictionaries

# Define a dictionary of student names and their corresponding ages
students = {"Alice": 20, "Bob": 22, "Charlie": 21, "David": 23}

# Accessing values in the dictionary
print("Bob's age:", students["Bob"])

# Adding a new student to the dictionary
students["Eve"] = 19

# Iterating over dictionary keys and values
for name, age in students.items():
    print(name, "is", age, "years old")
# This code demonstrates how to work with dictionaries in Python, including accessing values, adding new key-value pairs, and iterating over keys and values.

# Example 5: Using List Comprehensions

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension to create a new list containing squares of each number
squares = [x ** 2 for x in numbers]

print("Original list:", numbers)
print("List of squares:", squares)
# This example showcases list comprehensions, a concise and powerful way to create lists in Python by applying an expression to each item in an existing list.

# Example 6: Handling Errors with Try-Except Blocks

# Ask the user to enter a number
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter a valid number")
# Here, a try-except block is used to handle potential errors that may occur when asking the user to enter a number and performing division.

# Example 7: Working with Sets

# Define two sets of numbers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference of sets
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)
# This example demonstrates various set operations in Python, including union, intersection, and difference.

# Example 8: Reading and Writing Files


# Write data to a file
with open("data.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Python is awesome!")

# Read data from the file
with open("data.txt", "r") as file:
    data = file.read()
    print("Data read from file:")
    print(data)


# Here, we write some data to a file and then read it back. This illustrates basic file handling operations in Python.

# Example 9: Working with Classes and Objects


# Define a class representing a Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Car:", self.year, self.make, self.model)


# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Display information about the car
my_car.display_info()


# This example introduces classes and objects in Python. We define a Car class with attributes and a method to display information about the car.

# Example 10: Using Generators

# Define a generator function to generate Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Create a generator object
fib_gen = fibonacci()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))
# This example demonstrates the use of generators in Python to generate Fibonacci numbers lazily.

# Example 11: Working with Modules

# Import the math module
import math

# Calculate the square root of a number
num = 25
sqrt_num = math.sqrt(num)
print("Square root of", num, "is", sqrt_num)

# Calculate the factorial of a number
fact_num = 5
factorial = math.factorial(fact_num)
print("Factorial of", fact_num, "is", factorial)


# Here, we import the math module and use its functions to perform mathematical calculations like finding square roots and factorials.

# Example 12: Using Decorators

# Define a decorator function
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


# Apply the decorator to a function
@uppercase_decorator
def greet(name):
    return "Hello, " + name


# Call the decorated function
print(greet("Alice"))
# This example showcases the use of decorators in Python, which allow you to modify or enhance the behavior of functions dynamically.

# Example 13: Working with Lambda Functions


# Define a lambda function to calculate the square of a number
square = lambda x: x ** 2

# Call the lambda function
result = square(5)
print("Square of 5 is:", result)
# This example demonstrates the use of lambda functions, which are small anonymous functions that can be defined inline.

# Example 14: Using the zip Function

# Define two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Use the zip function to pair elements from both lists
for name, age in zip(names, ages):
    print(name, "is", age, "years old")
# Here, we use the zip function to combine elements from two lists into pairs, which are then iterated over in a loop.

# Example 15: Handling Dates and Times

# Import the datetime module
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# Extract and display the date separately
current_date = current_datetime.date()
print("Current date:", current_date)

# Extract and display the time separately
current_time = current_datetime.time()
print("Current time:", current_time)
# This example showcases how to work with dates and times using the datetime module in Python.

# Example 16: Using List Slicing

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get a slice of the list
slice1 = numbers[2:6]  # Elements from index 2 to 5 (exclusive)
slice2 = numbers[:5]  # Elements from the beginning to index 4
slice3 = numbers[7:]  # Elements from index 7 to the end

print("Slice 1:", slice1)
print("Slice 2:", slice2)
print("Slice 3:", slice3)
# This example demonstrates how to use list slicing to extract specific portions of a list.

# Example 17: Using the enumerate Function

# Define a list of fruits
fruits = ["apple", "banana", "orange", "grape"]

# Enumerate over the list and print both index and value
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)
# Here, we use the enumerate function to iterate over a list while also accessing the index of each element.

# Example 18: Working with JSON Data

# Import the json module
import json

# Define a dictionary representing JSON data
person_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Convert the dictionary to JSON string
json_string = json.dumps(person_data)

# Print the JSON string
print("JSON string:", json_string)

# Convert JSON string back to dictionary
data_dict = json.loads(json_string)
print("Name:", data_dict["name"])
print("Age:", data_dict["age"])
print("City:", data_dict["city"])
# This example illustrates how to work with JSON data in Python using the json module to serialize and deserialize data.
# Example 19: Using the map Function

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]


# Define a function to square a number
def square(x):
    return x ** 2


# Use the map function to apply the square function to each element in the list
squared_numbers = list(map(square, numbers))

print("Original list:", numbers)
print("Squared list:", squared_numbers)
# This example demonstrates how to use the map function to apply a function to each element of a list.

# Example 20: Using List Comprehensions with Conditional Statements

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a list comprehension to create a new list containing only even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print("Original list:", numbers)
print("Even numbers:", even_numbers)
# Here, we use a list comprehension with a conditional statement to filter out even numbers from a list.

# Example 21: Working with Files and Context Managers

# Open a file in write mode using a context manager
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a sample file.")

# Open the file in read mode using a context manager
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
# This example showcases how to work with files using context managers, ensuring that the file is properly closed after use.
# Example 22: Working with Tuples

# Define a tuple of coordinates
point = (3, 7)

# Unpack the tuple into separate variables
x, y = point

print("Coordinates:", point)
print("X coordinate:", x)
print("Y coordinate:", y)
# This example demonstrates how to work with tuples in Python, including unpacking tuple elements into separate variables.

# Example 23: Using the any and all Functions

# Define a list of boolean values
bool_list = [True, False, True, True]

# Check if any element in the list is True
any_true = any(bool_list)

# Check if all elements in the list are True
all_true = all(bool_list)

print("List of boolean values:", bool_list)
print("Any True:", any_true)
print("All True:", all_true)
# Here, we use the any and all functions to check if any or all elements in a list evaluate to True.

# Example 24: Using the filter Function

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]


# Define a function to filter even numbers
def is_even(x):
    return x % 2 == 0


# Use the filter function to filter even numbers from the list
even_numbers = list(filter(is_even, numbers))

print("Original list:", numbers)
print("Even numbers:", even_numbers)
# This example demonstrates how to use the filter function to filter elements from a list based on a given condition.

# Example 25: Working with Sets

# Define two sets of numbers
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Calculate the intersection of the two sets
intersection = set1.intersection(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection:", intersection)
# Here, we calculate the intersection of two sets of numbers using the intersection method.

# Example 26: Using Python's os Module for File Operations

import os

# Get the current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# List files and directories in the current directory
file_list = os.listdir(current_dir)
print("Files and directories in current directory:", file_list)
# This example demonstrates how to use Python's os module for common file operations, such as getting the current working directory and listing files and directories.

# Example 27: Working with Regular Expressions

import re

# Define a sample string
text = "Hello, my email is example@email.com."

# Define a regular expression pattern to match email addresses
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Search for email addresses in the text
matches = re.findall(pattern, text)

print("Text:", text)
print("Email addresses found:", matches)
# This example demonstrates how to use Python's re module for working with regular expressions to find email addresses in a piece of text.

# Example 28: Using Python's random Module

import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)

print("Random number between 1 and 10:", random_number)
# Here, we use Python's random module to generate a random integer between 1 and 10.

# Example 29: Using Python's datetime Module for Date and Time Operations

import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

print("Current date and time:", current_datetime)
print("Current year:", current_datetime.year)
print("Current month:", current_datetime.month)
print("Current day:", current_datetime.day)


# This example demonstrates how to use Python's datetime module to work with dates and times, including accessing various components such as year, month, and day.

# Example 30: Implementing Recursion

# Define a recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Calculate factorial of 5
result = factorial(5)
print("Factorial of 5:", result)
# Here, we implement a recursive function to calculate the factorial of a number.
