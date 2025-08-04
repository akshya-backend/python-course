# Python Functions is a block of statements that does a specific task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

# Benefits of Using Functions
# Code Reuse
# Reduced code length
#  Increased redability of code

# Python Function Declaration
# The syntax to declare a function is:

# Python Functions
# Syntax of Python Function Declaration
# Types of Functions in Python

# Built-in library function: These are Standard functions in Python that are available to use.
# User-defined function: We can create our own functions based on our requirements.
# Creating a Function in Python
# We can define a function in Python, using the def keyword. We can add any type of functionalities and properties to it as we require.

# What is def ?
# The def keyword stands for define. It is used to create a user-defined function. It marks the beginning of a function block and allows you to group a set of statements so they can be reused when the function is called.

# Syntax:

# def function_name(parameters):

#     # function body

# Explanation:

# def: Starts the function definition.
# function_name: Name of the function.
# parameters: Inputs passed to the function (inside ()), optional.
# : : Indicates the start of the function body.
# Indented code: The function body that runs when called.
# Example: Let’s understand this with a simple example. Here, we define a function using def that prints a welcome message when called.




def fun():
    print("Welcome to GFG")

fun()


# Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.
def evenOdd(x: int) ->str:
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))




# Types of Python Function Arguments
# Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following function argument types in Python:

# Default argument
# Keyword arguments (named arguments)
# Positional arguments
# Arbitrary arguments (variable-length arguments *args and **kwargs)
# Let's discuss each type in detail. 

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(10)



# 2
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# 3
# Positional Arguments
# We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age. By changing the position, or if you forget the order of the positions,
#  the values can be used in the wrong places, as shown in the Case-2 example below, where 27 is assigned to the name and Suraj is assigned to the age.

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")



# Arbitrary Keyword  Arguments
# In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
def myFun(*arg):
    for a in arg:
        print(a)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')



def myFun(**kwargs):
    print("Inside myFun, kwargs is a dictionary:")
    print(kwargs)
    print("----------")

    for key, value in kwargs.items():
        print("Current key:", key)
        print("Current value:", value)
        print("Formatted output:", "%s == %s" % (key, value))
        print("----------")

# Calling the function with keyword arguments
myFun(name="Akshya", age="25", city="Delhi")


# Python Function within Functions
# A function that is defined inside another function is known as the inner function or nested function.
# Nested functions can access variables of the enclosing scope. Inner functions are used so that they can be protected from everything happening outside the function.

def f1():
    s = 'I love GeeksforGeeks'
    
    def f2():
        print(s)
        
    f2()

f1()

# Anonymous Functions in Python
# In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.




def cube(x): return x*x*x   # without lambda

cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))



# Return Statement in Python Function
# The return statement in Python is used to exit a function and send a value back to the caller. It can return any data type, and if multiple values are separated by commas,
# they are automatically packed into a tuple. If no value is specified, the function returns None by default.

# return_types_demo.py

def return_integer():
    return 42  # int

def return_float():
    return 3.14  # float

def return_string():
    return "Akshya Bal"  # str

def return_list():
    return [1, 2, 3, 4]  # list

def return_dict():
    return {"name": "Akshya", "age": 21}  # dict

def return_tuple():
    return ("apple", "banana")  # tuple

def return_boolean():
    return True  # bool

def return_none():
    return  # no value, returns None

# ---------- OUTPUT ----------
print("Integer:", return_integer())
print("Float:", return_float())
print("String:", return_string())
print("List:", return_list())
print("Dictionary:", return_dict())
print("Tuple:", return_tuple())
print("Boolean:", return_boolean())
print("None:", return_none())


