def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

## Functions can have inputs/functionality/output -----------------------------------------------------
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc. --------------------

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)
    
# print(calculate(multiply, 5, 3))

# Nested Functions --------------------------------------------------------------------------

def outer_function():
    print("I'm outer")

    # This inner function cannot be called from outside the outer_function()
    # Unless it is returned
    def nested_function():
        print("I'm inner")

    return nested_function

# inner_function = outer_function() # Activates outer_function() which also saves the nested_function to inner_function
# inner_function() # Activates the nested function

# --------------------------- DECORATOR FUNCTIONS ----------------------------------

import time

# A Function that executes another, after a delay
def delay_decorator(function):    
    def wrapper_function():

        time.sleep(2)         
        # 👆 --- Code to be executed before the function call
        
        function()
        
        # 👇 --- Code to be executed after the function call
        
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")
    
def say_bye():
    print("Bye")
    
def say_greeting():
    print("How are you?")
    
say_hello()
say_greeting()

# ---------------------- FUNCTION SPEED TEST -------------------------

def speed_calc_decorator(function):
    def wrapper():
        
        start_time = time.time()
        # 👆 --- Code to be executed before the function call
        function()
        # 👇 --- Code to be executed after the function call
        finish_time = time.time()
        diff = finish_time - start_time
        
        print(f"{function.__name__ } run speed: {diff}") # function.__name__ returns the name of the function
        
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()