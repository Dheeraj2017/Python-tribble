#!/usr/bin/python
total = 0; # This is global variable.
# Function definition is here
def sum2( arg1, arg2 ):
# Add both the parameters and return them."    
    total = arg1 + arg2; # Here total is local variable.
    print ("Inside the function local total : ", total)
    return total;
# Now you can call sum2 function
sum2( 10, 20 );
print ("Outside the function global total : ", total)