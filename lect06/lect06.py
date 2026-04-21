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

item    = 'spam'
grocery = ['spam', 'milk', 'eggs', 'apple']
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


def print_each_element(lst):
    '''Print each element of list lst on its own line.'''
    # TODO


# Concept Test — trace this by hand before running:
#   for x in [1, 2, 3]:
#       print('Hello' * x)
# What prints?  A. 1 2 3   B. 'Hello' 3 times   C. Hello / HelloHello / HelloHelloHello   D. Other


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


def countOddNumbers(lst):
    '''Return the number of odd numbers in lst.'''
    # TODO


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
# def containsOddNumber(lst):
#     for x in lst:
#         if (x % 2 == 1):
#             return True
#         else:
#             return False
#
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
