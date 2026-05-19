# ============================================================
# PART 4: Tower of Hanoi
# ============================================================
# Pegs: A (source), B (auxiliary), C (target)
# Rules: move all disks from A to C; never place a larger disk on a smaller one

# Approach in plain English
# Step 1: Write the base case, if n = 1, move disk 1 from source to target
# Step 2: Trust that hanoi(n - 1, any source, any target, any aux) works!
#          hanoi(n - 1, "A", "B", "C") 
# Step 3: Is figure out the one step to finish the problem 
def hanoi(n, source, target, aux):
    '''Print the moves to solve Tower of Hanoi for n disks.'''
    if n == 1:
        print("Move disk 1 from", source, "to", target)
    else:
        # Move the  n - 1 disk from source to aux using target as the spare
        hanoi(n - 1, source, aux, target)
        print("Move disk", n , "from", source, "to", target)
         # Move the  n - 1 disk from aux to  target using source as the spare
        hanoi( n - 1, aux, target, source)


hanoi(3, 'A', 'C', 'B')
