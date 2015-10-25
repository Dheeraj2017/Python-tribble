#!/usr/bin/python
import random
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())
# It will generate same random number
random.seed( 20 )
print ("Random number with seed 10 : ", random.random())
# It will generate same random number
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())
random.seed( 20 )
print ("Random number with seed 10 : ", random.random())
random.seed(20)
print ("Random number with seed 10 : ", random.random())