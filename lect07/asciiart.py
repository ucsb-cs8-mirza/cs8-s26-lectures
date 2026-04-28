# Lecture 7 - Nested Loops and Nested Lists
# Part 1: ASCII Art
# Topics: nested loops, accumulator pattern with strings

# ============================================================
# PART 1: getRectangle — introducing nested loops
# ============================================================
# getRectangle(width: int, height: int) -> str returns a string
# representing a rectangle with given width and height

# Concept Test — getRectangle(3, 4) should return which of these?
#
# A.  ***          B. "***\n***\n***\n***\n"
#     ***
#     ***          C. "****\n****\n****\n"
#     ***
#                  D.  ****
#                      ****
#                      ****

def getRectangle(width, height):
    '''Return a string representing a rectangle of *s with 
       given width and height.'''
    # Outer loop: one iteration per ROW    -> range(height)
    # Inner loop: one iteration per COLUMN -> range(width)
    # TODO
    return ""

print(getRectangle(3, 4))
print(getRectangle(4, 5))
print(getRectangle(10, 5))


# ============================================================
# PART 2: getC — adding a condition inside the inner loop
# ============================================================
# getC(3, 4) should produce:
#   ***
#   *
#   *
#   ***
#
# Concept Test — given the getRectangle code, which block do we modify?
#
#   result = ""                   <- block A (initialization)
#   for i in range(height):
#     for j in range(width):
#       result += "*"             <- block B (inner loop body)
#     result += "\n"
#   return result
#
# A. Block A    B. Block B    C. Both    D. Neither

def getC(width, height):
    '''Return a string representing the letter C using *s with 
       given width and height.
       Top row and bottom row are full width; 
       middle rows have only the leftmost *.'''
    # Hint: copy the getRectangle structure, 
    # then add an if/else inside the inner loop
    # When should a * be printed vs a space?
    # TODO
    return ""

print(getC(3, 4))
print(getC(5, 6))
