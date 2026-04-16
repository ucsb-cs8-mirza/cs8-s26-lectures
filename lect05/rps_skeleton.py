# Lecture 6 - Rock Paper Scissors
# Topics: Problem Decomposition, Testing, if __name__ == "__main__"
#
# Learning Objectives:
# By the end of this lecture you should be able to:
#   1. Break a problem into focused subproblems, each solved by its own function
#   2. Write and run tests for individual functions before the full program is complete
#   3. Explain what __name__ is and why  if __name__ == "__main__"  is useful
#   4. Distinguish between functions that are easy to test (deterministic)
#      and functions that are harder to test (random)


# ============================================================
# STEP 1: Understand the problem
# ============================================================
# The player enters their choice (rock, paper, or scissors).
# The computer randomly picks one of the three options.
# The program determines who wins, or if it's a tie.
#
# Rules:
#   Rock beats Scissors
#   Scissors beats Paper
#   Paper beats Rock
#   Same choice = Tie
#
# What are the inputs?
#
# What is the output?


# ============================================================
# STEP 2: Write the main program as comments first
# ============================================================
# Before writing any functions, sketch out what the program needs to DO.
# This tells us what functions we'll need.



# ============================================================
# STEP 3: Identify the function stubs from the comments above
# ============================================================
# Each action in the comments above that is non-trivial becomes a function.
# Write the stub (signature + docstring) for each one here.


# ============================================================
# STEP 4: Test each function as you implement it
# ============================================================
# Open a new file test_rps.py alongside this file.
# For each function: write a test, run it, then implement the function.
#
# Key question: why can test_rps.py import this file without triggering input()?


# ============================================================
# STEP 5: Fill in the main program
# ============================================================
# Replace the comments in the main  block with real code.
# Wrap it in a if __name__ == "__main__" clause to avoid triggering 
# keyboard input when you are testing individual functions


# ============================================================
# CHECK YOUR UNDERSTANDING
# ============================================================
# 1. What is the value of __name__ when you RUN a file directly?
#
# 2. What is the value of __name__ when you IMPORT a file?
#
# 3. Why do we test determine_winner() with fixed inputs like
#    determine_winner("rock", "scissors") instead of using computer_choice()?
#
# 4. What would happen if you removed the  if __name__ == "__main__"  guard
#    and then ran test_rps.py?
#
# 5. Write two test cases for determine_winner()
#    Do you think the function handles them correctly? How would you verify?


# ============================================================
# PRACTICE
# ============================================================
# 1. The current game only plays one round. What would you need to change
#    to let the player play again after each round?
#    (Hint: think about what would need to repeat.)
#
# 2. Add a function is_tie(player, computer) that returns True if both
#    choices are the same. Write at least two test cases for it.
#
# 3. Right now computer_choice() uses random.randint(). Rewrite it using
#    random.choice(["rock", "paper", "scissors"]) -- does the behavior change?
