# Lecture 4 Topics (zybook 2.8 - 2.14 )
# Boolean Expressions and how to use them to write programs that make decisions!
# While you are waiting, go ahead and get the starter code for today's lecture from Canvas!
# boolean expressions: evaluate to True or False
# Lesson plan : examples of Boolean expressions, what is True or False?, 
# writing functions that retern bool type
# Game!!! 

# Relational operators: !=, == , <, > <=, >=
print("Boolean expressions using relational operators")
a = 3
# print(f"{a} != 3", a != 3) #
# print(f"{a} == 3", a == 3) #
# print(f"2 <= {a}", 2 <= a) #
# print(f"6 <= {a}", 6 <= a) #
# print(f"2 >= {a}", 2 >= a) #
# print(f"3 >= {a}", 3 >= a) #

# 0 is always bool False, every other number is bool True
# Empty string is False, every other string is bool True!

print("bool(x)")
print(f"bool({a})", bool(a)) # True
print(f"bool({a - 3})", bool(a - 3)) # False
print(f"{a} % 3 ", a % 3 ) # 0 


# Write a function that returns True if a is divisible by 3, otherwise returns False
# Stub of the function
def isDivisible(num : int) -> bool:
    ''' returns True if num is divisible by 3, False otherwise'''
    return (num % 3) == 0 # boolean expression
a = 171
print(f"isDivisible(5) = {isDivisible(5)}")
print(f"Is {a} divisible by 3?", isDivisible(a))
print(f"Is {4} divisible by 3?", isDivisible(4))

print("Boolean expressions involving strings")
empty_string = '' 
s1 = "wet"
s2 = "stay"
s3 = "dry"

print(f"{s3} == {s1} ", s3 == s1) # False
print(f"{s3} <= {s1} ", s3 <= s1) # Alphabetical
print("bool('')", bool(empty_string)) # False
print(f"bool({s1}) ", bool(s1)) # True
print(f"bool({s2})", bool(s2)) # True
print(f"bool({s3}) ", bool(s3)) # True

# print("Does the string contain the letter 'a'?")
# keyword in checks for membership in a sequence
# string type is a sequence of characters
# 
# empty_string = '' 
# s1 = "wet"
# s2 = "stay"
# s3 = "dry"
print(f"Is 'a' in {s1}?")
print(f"Is 'e' in {s1}?")
print(f"Is 'a' in {s2}?")
print(f"Is 'a' in {s3}?")

# word = "erudite"
# print("Boolean expressions using logical operators")
# # logical operators: and, or, not
# print(f"Is {a} between 0 and 10?")

# Logical operators: Connect boolean expressions into more complex Boolean expressions
# Logical operators are: and, or, not!

# Which Boolean expression evaluates to True if word contains the letter 'a' or 'e'?
# A. "a" or "e" in word
# B. "a" in word or "e" in word # Right usage 
# C. Both A and B are correct

# print(f"Does {word} contain the letter 'a' or 'e'?")


# Which a function that returns True if word contains a vowel, False otherwise
# print(f"Does {word} contain a vowel?")

def containsVowel(word: str) -> bool:
    '''returns True if word contains a vowel'''
    return 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word

print(f"containsVowel(zoo) = {containsVowel("zoo")}")
print(f"containsVowel(xyz) = {containsVowel("xyz")}")


# # Write a function to find the minimum of two numbers

# # Write a function to find the minimum of three numbers (zyLab 2.16)

def minOfThree(num1:int, num2: int, num3: int) -> int:
    '''returns the minuimum of 3 numbers'''
    if num1 < num2  and num1 < num3: # num1 <num2 < num3 same as num1 < num2 and num2 <num3
        # body of if statement
        return num1
    elif num2 <num1  and num2 < num3:
        # body of the elif
        return num2
    else:
        # body of the else
        return num3
print(f"minOfThree(3, 1, 5) = {minOfThree(3, 1, 5)}")
print(f"minOfThree(1, 3, 5) = {minOfThree(1, 3, 5)}")
print(f"minOfThree(5, 3, 1) = {minOfThree(5, 3, 1)}")
# # Work to finish on your own zybook 2.8 - 2.17
