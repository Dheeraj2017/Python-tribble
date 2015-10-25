#!/usr/bin/env python  -tt
num1 = input("Input a number: ")
num2 = input("Input another number: ")


for x in range(num1,num2):
    prime = True
    for i in range(2,x):
        if (x%i==0):
            prime = False
    if prime == True:
       print x,


