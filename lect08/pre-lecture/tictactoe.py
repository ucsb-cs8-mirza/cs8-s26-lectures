# Lecture 7 - Nested Loops and Nested Lists
# Part 2: Tic Tac Toe
# Topics: nested lists, index-based loops, enumerate, fencepost problem

# ============================================================
# PART 1: Data representation — how do we store the board?
# ============================================================
# Concept Test — which representation is easiest to UPDATE?
# (Hint: try putting an X in the middle cell of each one)
#
# A. board = 'X-O\nO--\n--X'
# B. board = 'X-O, O--, --X'
# C. board = ['X-O', 'O--', '--X']
# D. board = [['X', ' ', 'O'],
#              ['O', ' ', ' '],
#              [' ', ' ', 'X']]
# E. All of the above
print("tic tac toe board as a string")
board_1 = 'X-O\nO--\n--X' 
# board_1[5] = "X"
print(board_1)
# If we choose a string representation, we can't modify the individual elements in the string
# because string is an immutable type (indivisible!)
# where a list is a mutable type

print("\ntic tac toe board as a nested list")
board = [['X', ' ', 'O'], ['O', ' ', ' '], [' ', ' ', 'X']]

#print(board)


# ============================================================
# PART 2: Nested list indexing
# ============================================================
matrix = [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]

# Try in the shell:
#   matrix[0]       -> [1, 2, 3]
#   matrix[0][0]    -> 1    (row 0, col 0)
#   matrix[1][2]    -> 6    (row 1, col 2)
#   matrix[2][1]    -> 8    (row 2, col 1)
#   matrix[2][1] = 80       (mutation: lists are mutable!)

# Concept Test — which has the same output as:
#   row = matrix[2]
#   print(row[1])
#
# A. print(matrix[1][2])
# B. print(matrix[2][1])
# C. Both
# D. Neither


# ============================================================
# PART 3: print_board — simple for loop (v0)
# ============================================================
board = [['X', ' ', 'O'],
         ['O', ' ', ' '],
         [' ', ' ', 'X']]

def print_board_v0(board):
    '''Print the board using a plain for loop.
    Expected output:
     X | . | O
    ---+---+---
     O | . | .
    ---+---+---
     . | . | X
    (use . for empty cells)
    Problem: prints a divider after the LAST row too — can we fix that?
    '''
    # TODO: loop over rows, print each row, always print divider after

    for row in board:
        for elem in row:
            print("", elem, "|", end ="")
        print("\n---+---+---")

    return

board[1][1] ="X"


# ============================================================
# PART 4: print_board — fencepost problem + enumerate
# ============================================================
# The fencepost problem: n rows need only (n-1) dividers, not n.
#
# enumerate(collection) gives (index, value) pairs:
#   for (i, row) in enumerate(board):
#       print(f"row {i}: {row}")

def print_board(board):
    '''Print the board using enumerate to skip the trailing divider.
    Expected output:
     X | . | O
    ---+---+---
     O | . | .
    ---+---+---
     . | . | X
    '''
    # TODO: use enumerate — only print "---+---+---" when i < len(board) - 1
    return


print("--- v0 ---")
print_board_v0(board)
# print("--- fixed ---")
# print_board(board)
