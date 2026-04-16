# Lecture 3: Functions
import math
# In math 
# y = f(x)
# Functions : Programming construct
# Idea is to abstract out the details of your code

# Step 1: How do I make or write a function? Define the function
# Stub of a function: skeleton of the definition of the function
def area_of_circle(radius): # radius is a parameter
    ''' returns the area of a circle given the input radius
        float -> float
    '''
    # Body of the function
    result = math.pi * radius ** 2 ## radius and result are local variables
    # Local variables only exist within the body of the function
    return result

# Step 2: How do I use the function to compute? Call the function
y = area_of_circle(10) # calling the function

print(y)
# print(f"area_of_circle(10) = {area_of_circle(10)}")
# print("area_of_circle(5) = ", area_of_circle(5))
# print("area_of_circle(2) = ", area_of_circle(2))
# print("hello) # syntax error

# x = 3
# y = "Hello " + x + " world"
# print(y)

