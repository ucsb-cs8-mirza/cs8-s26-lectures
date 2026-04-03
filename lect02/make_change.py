# make_change.py
 
# We are working towards an algorithm to convert input (total amount in cents)
# to output no. of dollars, quarters, nickels, dimes, pennies

# Write your step by step process (algorithm)

# Input is an amount - total_amount
# Step 0: Get the input (total_amount)
# total_amount = 99
total_amount = int(input("Enter an amount (integer): ")) # "287" convert 287
# Step 1: Calculate the number of dollars that fits into total_amount
# Step 2: Store that value (num_dollars)
num_dollars = total_amount // 100
# Step 3: Calculate the number of quarters that fits into the remaining amount (left over)
# Step 4: Store the value we calculated (num_quarters)
remaining = total_amount % 100
num_quarters = remaining // 25
# num_quarters = (total_amount % 100) // 25 (also works!!)
# Step 5: Calculate the remaining amount 
remaining = remaining % 25
# Step 6: Store the number of dimes (num_dimes) that fits into the remaining amount
num_dimes =  remaining // 10
# Step 7: Calculate the number of nickels that fits into the remaining amount (left over)
# Step 8: Store the value we calculated num_nickels
remaining = remaining % 10 # remaining is 6
num_nickels = remaining // 5
# Step 9: The remaining left over value is the number of pennies (num_pennies), store that value
num_pennies = remaining  % 5
# Step 10: Output is (num_dollars, num_quarters, num_dimes, num_nickels,  num_pennies)  
print(f"({num_dollars}, {num_quarters}, {num_dimes}, {num_nickels}, {num_pennies} )")