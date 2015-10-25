#!/usr/bin/python
# Open a file
fo = open("foo.txt", "r+")
str1= fo.read(10);
print "Read String is : ", str1
# Close opened file
fo.close()
'''
The    
   read()    
   Method:    
  
The read() method reads a string from an open file. It is important to note that Python strings can have binary data
and not just text.

Here, passed parameter is the number of bytes to be read from the opened file. This method starts reading from
the beginning of the file and if count is missing, then it tries to read as much as possible, maybe until the end of
file
'''