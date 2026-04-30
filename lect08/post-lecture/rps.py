# Lecture 6 - Rock Paper Scissors
# Topics: Problem Decomposition, Testing, what is a module? and how to write one? if __name__ == "__main__"
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
# player's choice: string
#
# What is the output?
# Result of the game! 


# ============================================================
# STEP 2: Write the main program as comments first
# ============================================================
# Before writing any functions, sketch out what the program needs to DO.
# This tells us what functions we'll need.
import random
# Figure out the subproblems --> functions that I will write
def is_valid_choice(player_choice : str) -> bool:
    ''' returns True if the player_choice is one of rock, paper, or sciessors, 
    otherwise return false'''
    if player_choice == 'rock' or player_choice == 'scissors' or player_choice == 'paper':
        return True
    else:
        return False

def computer_choice()-> str:
    '''returns a str that randomly selected among the three options '''
    result = random.randint(1, 3)
    if result == 1:
        return "rock"
    elif result == 2:
        return "scissors"
    else:
        return "paper"
    

def determine_winner(player: str, computer: str) -> str:
    ''' return one of the following: "Computer Wins!" or "You win!" or
    "Its a tie" based on inputs'''
    if player == computer:
        return "Its a Tie"
    elif computer == "rock" and player == "scissors" \
        or computer == "scissors" and player == "paper" \
        or computer == "paper" and player == "rock":
        return "Computer Wins!"
    else:
        return "You Win!"

# Main logic 
# print("__name__ = ", __name__)

if __name__ == "__main__":
    # Step 1: get the player's choice
    player = input("Enter your choice (rock, paper, scissors): ")
    # Step 2: if the choice is not valid , then print an error message and end the program
    # Step 3: Else if the player's choice is valid, computer picks a choice
    if not is_valid_choice(player): # input: str, returns a boolean
        print("Not a valid choice, try again! Inputs are case-sensitive!")
    else: 
        computer = computer_choice();
        # Step 4: Print the choice that computer picked
        print("Computer picked", computer)

        # Step 5: Determine the winner and print the winner
        result = determine_winner(player, computer)
        print(result)

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
