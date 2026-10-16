
# toolbox.py

# Function 1: Return a number multiplied by 2
def double(number):
    return number * 2


# Function 2: Check whether a learner has passed
def is_pass(score):
    return score >= 50


# Function 3: Greet a person using a default greeting
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"


# Test the functions
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))
