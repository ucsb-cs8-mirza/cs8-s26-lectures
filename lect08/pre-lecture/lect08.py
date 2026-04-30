# Lecture 8 - While Loops and List Comprehension
# zyBooks 4.4-4.5, 4.10
#
# Learning Objectives:
# By the end of this lecture you should be able to:
#   1. Write a while loop and explain when to prefer it over for
#   2. Recognize common while loop patterns (sentinel, flag, while True/break)
#   3. Build a new list using the accumulator pattern with a for loop
#   4. Rewrite that accumulator as a list comprehension


# ============================================================
# PART 1: While loops — motivation and syntax
# ============================================================
# for loop  → use when you know the collection / number of iterations up front
# while loop → use when you repeat until some condition changes
#
# Syntax:
#   while <condition>:
#       # body
#       # MUST update something that affects the condition — or infinite loop!

# Concept Test A — what does this print?
#   x = 6
#   while x > 4:
#       print(x)
#       x = x - 1
# A. 6 5   B. 6 5 4   C. 5 4   D. 5 4 3   E. 6 5 4 3

# Concept Test B — swap print and update. What prints now?
#   x = 6
#   while x > 4:
#       x = x - 1
#       print(x)
# A. 6 5   B. 6 5 4   C. 5 4   D. 5 4 3   E. 6 5 4 3

# Concept Test C — tricky loop with conditional inside
#   n = 3
#   while n > 0:
#       if n == 5:
#           n = -99
#       print(n)
#       n = n + 1
# A. 3 4   B. 3 4 5   C. 3 4 -99   D. 3 4 5 -99


# ============================================================
# PART 2: Common while loop patterns
# ============================================================

# --- Pattern 1: flag variable ---
def get_valid_input():
    '''Keep asking until the player enters rock, paper, or scissors.'''
    # valid = False
    # while not valid:
    #     ...
    # TODO
    pass


# --- Pattern 2: while True / break ---
def get_valid_input_v2():
    '''Same behavior as get_valid_input, using while True and break.'''
    # TODO
    pass


# Concept Test D — password validation
# Which of these loops until the user enters a 5-char password starting with 'xy'?
#
# A.  valid = False
#     while not valid:
#         s = input("Enter a password: ")
#         valid = len(s) == 5 and s[:2] == 'xy'
#
# B.  while True:
#         s = input("Enter a password: ")
#         if len(s) == 5 and s[:2] == 'xy':
#             break
#
# C. Both are correct
# D. None is correct


# --- Pattern 3: continue — skip the rest of the body for this iteration ---
# Use continue when you want to skip some iterations but keep looping.
# Common use: skip invalid/unwanted values without deeply nesting if/else.
#
# Example: print only the odd numbers from 1 to 10, skipping evens
#
#   x = 0
#   while x < 10:
#       x += 1
#       if x % 2 == 0:
#           continue        # skip the print, go back to the while check
#       print(x)
#
# contrast with break: break exits the loop entirely
#                      continue just skips to the next iteration
#
# Concept Test E — what does this print?
#   x = 0
#   while x < 5:
#       x += 1
#       if x == 3:
#           continue
#       print(x)
# A. 1 2 3 4 5
# B. 1 2 4 5
# C. 1 2
# D. 3 4 5


# ============================================================
# PART 3: RPS revisit — open rps.py
# ============================================================
# Two improvements to discuss live in rps.py:
#
# 1. computer_choice() — replace randint + if/elif/else with:
#       choices = ['rock', 'paper', 'scissors']
#       return random.choice(choices)
#
# 2. Main block — wrap in a while loop so the game repeats:
#       player = input("Enter your choice (or 'quit'): ")
#       while player != 'quit':
#           ... (play one round)
#           player = input("Enter your choice (or 'quit'): ")


# ============================================================
# PART 4: Building lists — accumulator pattern with append
# ============================================================
# So far accumulators built a number or string.
# You can also accumulate into a list using list.append().

def get_evens(lst):
    '''Return a new list containing only the even numbers from lst.
    Example: get_evens([1, 2, 3, 4, 5]) -> [2, 4]
    '''
    result = []
    # TODO: loop over lst, append even numbers to result
    return result


def double_all(lst):
    '''Return a new list where every element is doubled.
    Example: double_all([1, 2, 3]) -> [2, 4, 6]
    '''
    result = []
    # TODO
    return result


# ============================================================
# PART 5: List comprehension — shorthand for the above
# ============================================================
# Pattern:
#   new_list = [<expression> for <var> in <iterable>]
# With filter:
#   new_list = [<expression> for <var> in <iterable> if <condition>]

def get_evens_lc(lst):
    '''Same as get_evens, written as a list comprehension.'''
    # TODO
    pass

def double_all_lc(lst):
    '''Same as double_all, written as a list comprehension.'''
    # TODO
    pass


# Concept Test F — which produces the same result as ['.', '.', '.']?
# A. ['.'] * 3
# B. ['.' for i in range(3)]
# C. result = []
#    for i in range(3): result.append('.')
# D. All of the above
# E. None of the above

# Concept Test G — which correctly initializes an empty 3x3 board?
# (goal: [['.','.','.'], ['.','.','.'], ['.','.','.']] with independent rows)
#
# row = ['.', '.', '.']
# A. board = [row] * 3                     <- aliased! all rows are the same object
# B. board = [row[:]] * 3                  <- still aliased!
# C. board = [row[:] for i in range(3)]    <- correct: fresh copy each time
# D. All of the above
# E. None of the above


# ============================================================
# SUMMARY — loop pattern cheat sheet
# ============================================================
# Pattern                    When to use                    Example
# -------                    -----------                    -------
# for x in lst               only need value                print each element
# for i in range(len(lst))   only need index                update a cell, fencepost
# for i,x in enumerate(lst)  need both                      skip last divider
# while <condition>          don't know # of iterations     play again, validate input
# [expr for x in lst]        build a new list               double_all, get_evens


# ============================================================
# PRACTICE
# ============================================================
# 1. Write get_long_words(sentence, n) using a for loop, then rewrite
#    it as a list comprehension. Return all words longer than n chars.
#
# 2. Add a score tracker to the RPS while loop in rps.py — count wins,
#    losses, and ties, and print the totals when the player quits.
#
# 3. Write make_board(n) that returns an n×n board of '.' using list comprehension.
