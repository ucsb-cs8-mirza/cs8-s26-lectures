# Lecture 6 - Storing Sequences: Strings, Lists, and Tuples
# Topics: Lists, for loops, accumulator pattern, loops + conditionals, range()
#
# Learning Objectives:
# By the end of this lecture you should be able to:
#   1. Create lists and access elements using indexing and slicing
#   2. Distinguish between strings, lists, and tuples
#   3. Write a for loop to iterate over any collection
#   4. Apply the accumulator pattern to count or sum things
#   5. Combine loops with conditionals to filter elements
#   6. Use range() to repeat code a fixed number of times


# ============================================================
# PART 1: Sequences — strings, lists, tuples
# ============================================================
# Run each line below in the Python shell and observe type() and len()

item    = 'spam' # string : sequenec of characters
grocery = ['spam', 'milk', 'eggs', 'apple'] # list : sequence of any type
stu1    = ('John', 'Doe', 67024847)
stu2    = [('John', 'Doe', 67024847), 3.8]

# Try in the shell:
#   type(item)      len(item)
#   type(grocery)   len(grocery)
#   type(stu1)      len(stu1)
#   type(stu2)      len(stu2)


# ============================================================
# PART 2: List indexing and slicing
# ============================================================
cone_snails = ['purple', 'blue', 'green']

# Evaluate each expression — what do you expect?
#   cone_snails[0]
#   cone_snails[2]
#   cone_snails[0:2]
#   cone_snails[-1]
#   cone_snails[:]
#   cone_snails[:-1]

# Lists are MUTABLE — you can change an element by index:
#   cone_snails[1] = 'orange'

# Useful list operations:
#   len(cone_snails)
#   cone_snails + ['red']
#   min([3, 1, 2])   max([3, 1, 2])   sum([3, 1, 2])
#   cone_snails.index('green')
#   cone_snails.count('purple')


# ============================================================
# PART 3: for loops — iterating over collections
# ============================================================
# Syntax:
#   for item in some_collection:
#       # code

def print_each_char(s):
    '''Print each character of string s on its own line.'''
    # TODO


def print_each_element(lst : list):
    '''Print each element of list lst on its own line.'''
    # Loop through the elements
    for element in lst:
        # body of the for loop
        print(element, "| ", end="")
    print("\nEnd of for loop")
    print("******\n******\n*******")


print_each_element(grocery)

# Concept Test — trace this by hand before running:
for x in [1, 2, 3]: # x is the loop variable
    print('Hello' * x) # We can use the loop variable inside the for loop in any expression

# What prints?  
# A. 1 2 3   
# B. 'Hello' 3 times  
# C. Hello  
#    HelloHello 
#    HelloHelloHello   
# D. Other


# ============================================================
# PART 4: Accumulator pattern
# ============================================================
# Template:
#   result = <starting value>       # initialize
#   for item in collection:
#       result = result + ...       # update
#   return result

def countElements(lst):
    '''Return the number of elements in lst (without using len()).'''
    # TODO
    if type(lst)!= list:
        print("Invalid input type")
        return 0
    result = 0
    for element in lst:
        result +=1
    return result

# print(grocery)
# print("My grocery list has", countElements(grocery), "items")
# print("My grocery list has", countElements(10), "items")

def countOddNumbers(lst):
    '''Return the number of odd numbers in lst.'''
    # TODO
    result = 0 # Initialize variable outside the loop
    for element in lst:
        if element % 2 != 0:
            result += 1 # result +=1 is just a shorthand for result = result + 1 , accumulating
    return result # return the answer
# Accumulator pattern: 
nums = [10, 15, 2, 3, 3, 3, 3, 3, 3]
print(nums, "has", countOddNumbers(nums), "odd numbers")
print(nums, "has", countOddNumbers([]), "odd numbers")


def sumOddNumbers(lst):
    '''Return the sum of all the odd numbers in lst.'''
    # TODO
    result = 0 # Initialize variable outside the loop
    for element in lst:
        if element % 2 != 0:
            result += element # result +=1 is just a shorthand for result = result + 1 , accumulating
    return result # return the answer
# Accumulator pattern: 
nums = [10, 1, 3, 2]
print(nums, "Sum:", sumOddNumbers(nums))
print(nums, "Sum:", sumOddNumbers([]))
print(nums, "Sum:", sumOddNumbers([2, 4, 6, 8]))


def count(name, letter):
    '''Return the number of times letter appears in name (upper or lower case).'''
    # TODO


# ============================================================
# PART 5: Loops and conditionals
# ============================================================

def containsOddNumber(lst):
    '''Return True if ANY element in lst is odd, otherwise return False.'''
    # TODO


def isListOfNumbers(lst):
    '''Return True if ALL elements in lst are numbers (int or float),
    otherwise return False.'''
    # TODO


# Concept Test — find the bug:
#
def containsOddNumber(lst):
    '''returns True if the lst contains an odd number, False otherwise'''
    # lst = [1, 3, 5] 
    for x in lst:
        # Bug is that the funtion terminates too early when it shouldn't
        if (x % 2 == 1):
            return True
        else:
            return False

# Correct version of the code!
def containsOddNumber(lst):
    '''returns True if the lst contains an odd number, False otherwise'''
    # lst = [2, 4, 6, 8, 10]

    for x in lst:
        # Bug is that the funtion terminates too early when it shouldn't
        if (x % 2 == 1):
            return True        
    return False
# No lecture on Thursday! Watch the 
# Expected!
# [2, 4, 6, 5] --> True
# [2, 4, 6, 8, 10] --> False
# [1, 3, 5] --> True
# For which input does this return the RIGHT answer?
# A. [2, 4, 6, 5] -->False    B. [2, 4, 6, 8, 10] -->False (happend to be the right answer!)   
# C. [1, 3, 5] ---> True! Correct

# For which input does this return the WRONG answer?
#   A. [1, 2, 3, 4]   B. [2, 3, 4, 1]   C. [3, 4, 1, 2]   D. [3, 3, 3, 3]


# ============================================================
# PART 6: range()
# ============================================================
# range(5)        → [0, 1, 2, 3, 4]
# range(1, 5)     → [1, 2, 3, 4]
# range(0, 10, 2) → [0, 2, 4, 6, 8]

def print_hello_n_times(n):
    '''Print 'Hello' exactly n times using range().'''
    # TODO


# Concept Test — trace by hand before running:
#   for x in range(1, 4, 2):
#       print(2**x, end=" ")
# What prints?  A. 1 4 2   B. 2 16 4   C. 2 8 16   D. 2 8   E. Other


# ============================================================
# PART 7: More accumulator examples
# ============================================================

def countWords(sentence):
    '''Return the number of words in sentence.'''
    # TODO


# ============================================================
# CHECK YOUR UNDERSTANDING
# ============================================================
# 1. What is the difference between a list and a tuple?
#    Which one is mutable?
#
# 2. What does cone_snails[-1] return?
#
# 3. In the accumulator pattern, what two things must you do BEFORE the loop?
#
# 4. Why does the buggy containsOddNumber() above fail on [2, 3, 4, 1]?
#
# 5. What does range(2, 10, 3) produce?


# ============================================================
# PRACTICE
# ============================================================
# 1. Write sumList(lst) — returns the sum of all numbers in lst
#    without using the built-in sum().
#
# 2. Write allPositive(lst) — returns True if every number in lst
#    is greater than zero, False otherwise.
#
# 3. Write countVowels(s) — returns the number of vowel characters
#    (a, e, i, o, u — upper or lower case) in string s.
#
# 4. Write buildEvenList(n) — returns a list of all even numbers
#    from 0 up to (but not including) n, using range().
