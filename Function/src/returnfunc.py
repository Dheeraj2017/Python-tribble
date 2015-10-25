#!/usr/bin/python
# Function definition is here
def sum1( arg1, arg2 ):
# Add both the parameters and return them."
    total = arg1 + arg2
    print ("Inside the function : ", total)
    return total;
# Now you can call sum1 function
total = sum1( 10, 20 );
print ("Outside the function : ", total)