#!/usr/bin/python
var1 = 'Hello World!'
var2 = "Python Programming"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#format specifier in the python string and how to access them
print ("My name is %s and weight is %d kg!" % ('Zara', 21))


#print in the triple quote format so whatever the style we like to print it will print same as we give input 
#and it has contain escaping character and formfeed tab to show its functionality inside the triple quote

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

#simple string dislay
print ('C:\\nowhere')  # but there is a problem with this because this will not display the desired result
# raw string 

print (r'C:\\nowhere')

#unicode string
print (u'Hello, world!')


