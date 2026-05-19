# Lecture 11 - Recursion
# zyBook 6.1 - 6.3
#
# Learning Objectives:
#   1. Understand recursion as self-reference
#   2. Apply the 3-step recipe: simplest input, base case, recursive case
#   3. Implement factorial, countdown, and Tower of Hanoi

# Tower of Hanoi: https://www.mathsisfun.com/games/towerofhanoi.html
# Try it with 3 disks. Can you describe the strategy in English?
# Could you write a loop to solve it for any n?


# ============================================================
# PART 1: Warm-up — function calling another function
# ============================================================

def happy(message):
    print(message)

def sing(P, msg):
    happy(msg)
    happy(msg)
    print("Happy Birthday dear " + P + "!")
    happy(msg)

# Concept Test — what is the output of sing("Fred", "Happy Birthday to you!")?
# A. Happy Birthday to you!
# B. Happy Birthday dear Fred!
# C. Happy Birthday to you!
#    Happy Birthday to you!
# D. Happy Birthday to you!
#    Happy Birthday to you!
#    Happy Birthday dear Fred!
#    Happy Birthday to you!
# E. Error: cannot call happy() inside sing()

# sing("Fred", "Happy Birthday to you!")


# ============================================================
# PART 2: Factorial
# ============================================================
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!          <- self-reference!
#
# Recursive function design:
#   1. Handle the base case           (simplest input)
#   2. Trust recursion to do the rest (assume fac(n-1) already works)
#   3. You do ONE step of progress    (multiply by n)
#
# Human: base case + 1 step.   Computer: everything else.

def fac(n):
    '''Return n factorial.'''
    # TODO: base case
    # TODO: let fac(n-1) do the heavy lifting, you just multiply by n
    pass

print(fac(1))   # 1
print(fac(5))   # 120


# ============================================================
# PART 3: Countdown
# ============================================================
# countdown(3)  prints:  3 2 1 Go!
#
# Apply the same 3-step recipe:
#   1. Simplest input?
#   2. Base case?
#   3. Recursive case?

def countdown(n):
    '''Print n, n-1, ... 1, Go!'''
    # TODO
    pass

countdown(3)   # 3 2 1 Go!
countdown(1)   # 1 Go!

# Part 4: Tower of Hanoi!

# ============================================================
# PRACTICE
# ============================================================
# ispalindrome(word) — returns True if word reads the same forwards and backwards
#
# Apply the 3-step recipe:
#   1. Simplest input?
#   2. Base case?
#   3. Recursive case — hint: check first and last letter, then recurse on the middle
#
# palindromes: civic, kayak, level, madam, racecar
# not palindromes: minimum, sardines, cake
