# test_rps.py
# Test each of the functions in rps.py
import rps

print("Test is_valid_choice function ")
print(f"{rps.is_valid_choice('rock') = }")# True
print(f"{rps.is_valid_choice('scissors') = }")# True
print(f"{rps.is_valid_choice('lizard') = }")# False
print(f"{rps.is_valid_choice('Rock') = }")# False

print("test computer choice")
choice = rps.computer_choice()
print(f"{choice = }")
print(f"{rps.is_valid_choice(choice)= }") # True

print("test determine_winner")
print(f"{choice = }")
print(f"{rps.determine_winner('paper', choice) = }")
print(f"{rps.determine_winner('scissors', choice) = }")
print(f"{rps.determine_winner('rock', choice) = }")