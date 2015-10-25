'''
The    
   input    
   Function:    
  
The input([prompt]) function is equivalent to raw_input, except that it assumes the input is a valid Python
expression and returns the evaluated result to you.
'''
#!/usr/bin/python
str1 = input("Enter your input: ");
print "Received input is : ", str1


'''
Output :
Enter your input: [x*5 for x in range(2,10,2)]
Received input is :  [10, 20, 30, 40]
'''