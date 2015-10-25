#!/usr/bin/python
# Open a file
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");
# Close opened file
fo.close()
'''
The above method would create foo.txt file and would write given content in that file and finally it would close that
file. If you would open this file, it would have following content:
'''

'''
The    
   write()    
   Method:    
  
The write() method writes any string to an open file. It is important to note that Python strings can have binary
data and not just text.
The write() method does not add a newline character ('\n') to the end of the string:
'''