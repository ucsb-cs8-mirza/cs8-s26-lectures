## Print vs Return
def tip_return(bill, percent):
    ''' float, int --> float '''
    x = 5 # local variable
    return bill * percent / 100 

def tip_print(bill, percent):
    '''float, int --> None'''
    print(bill * percent / 100)
    
y = tip_return(100, 15) # y is a float (number)
z = tip_print(100, 15)  # z is a None (NoneType)

print(y + 10)
#print(z + 10) # TypeError: Errors related to mismatched types