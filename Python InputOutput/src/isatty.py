#!/usr/bin/python
# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
ret = fo.isatty()
print "Return value : ", ret
# Close opened file
fo.close()
'''
The method isatty() returns True if the file is connected (is associated with a terminal device) to a tty(-like) device,
else False.
'''