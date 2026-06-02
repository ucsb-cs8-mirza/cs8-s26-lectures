# Lecture 12 - More Recursion
# zyBook 6.1 - 6.3
#
# Refined 3-step recipe:
#   1. Base case: handle the simplest input
#   2. Trust recursion to solve a SMALLER version of the problem
#      (not necessarily n-1 — could be lst[1:] or word[1:-1])
#   3. You do ONE step of progress toward the base case
#
# Human: base case + 1 step.   Computer: everything else.


# ============================================================
# PART 1: ispalindrome
# ============================================================
# A word is a palindrome if it reads the same forwards and backwards.
# civic, kayak, racecar  ->  True
# sardines, cake         ->  False
#
# Apply the recipe:
#   1. Base case?       (simplest input)
#   2. Smaller problem? (what do you pass to the recursive call)
#   3. One step?        (what do YOU check before handing off)

def ispalindrome(word):
    '''Return True if word is a palindrome.'''
    # Base case(s): Simplest input(s) for which I know the answer
    # if empty string or one letter word then return True
    if len(word) == 0:
        return True
    if len(word) == 1:
        return True
    # If the first letter does not match the last letter in word return False
    if word[0] != word[-1]:
        return False
    # If I have reached this point in my code that means the first and last letter match up
    return ispalindrome(word[1:-1]) # Recusive step
    
# example:  ispalindrome("ava")
# ----         ispalindrome("v") return True

palindromes = ["civic", "kayak", "level", "madam", "racecar"]
other       = ["minimum", "sardines", "cake"]
for word in palindromes:
    print(f"{word:12}: {ispalindrome(word)}")
for word in other:
    print(f"{word:12}: {ispalindrome(word)}")


# ============================================================
# PART 2: max of a list
# ============================================================
# max_list([3, 1, 4, 1, 5, 9])  ->  9
#
# Apply the recipe:
#   1. Base case?       (simplest list)
#   2. Smaller problem? (what is the smaller list)
#   3. One step?        (what do YOU compare)

def max_list(lst: list)->int:
    '''Return the largest element in lst. input must have atleast one element'''
    # Base case: simplest possible input:  which is list of length 1, return single element in the list
    if len(lst) == 1:
        return lst[0]
    # Recursive case: Any input with more than one element. Any list of size 2 or more
    # [3, 1, 4, 1, 5, 9]
    # lst[0] is 3
    # lst[1:] is [1, 4, 1, 5, 9]
    # step 2 of recursive funciton design says: trust that your function works on a simpler input
    # max_list([1, 4, 1, 5, 9]) return the max element (9)
    # Think of the one step computation
    # lets assume the input is of size 2, [5, 9]
    max_rest_of_the_list = max_list(lst[1:])
    if lst[0] > max_rest_of_the_list:
        return lst[0]
    else:
        return max_rest_of_the_list

print(max_list([3]))           # 3
print(max_list([3, 1, 4]))     # 4
print(max_list([3, 1, 4, 1, 5, 9]))  # 9


# ============================================================
# PART 3: print_num_pattern  [lab discussion]
# ============================================================
# print_num_pattern(12, 3) prints: 12 9 6 3 0 -3 0 3 6 9 12
# print_num_pattern(9, 3) prints:     9 6 3 0 -3 0 3 6 9
# Key question: what if you print n both BEFORE and AFTER the recursive call?
#
# Trace it:
#   print 12
#   recurse(9, 3)
#     print 9
#     recurse(6, 3)
#       ...
#         base case: just print -3
#       ...
#     print 9
#   print 12
#
# Apply the recipe:
#   1. Base case?   when does the "going down" stop?
#   2. Smaller problem?
#   3. One step?

def print_num_pattern(n, step):
    '''Print n down to first negative by step, then back up to n.'''
    # TODO
    pass

# print_num_pattern(12, 3)
# expected: 12 9 6 3 0 -3 0 3 6 9 12
