#!/usr/bin/python
# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name  #Returns name of the file.
print "Closed or not : ", fo.closed #Returns true if file is closed, false otherwise.
print "Opening mode : ", fo.mode  #Returns access mode with which file was opened.
print "Softspace flag : ", fo.softspace  #Returns false if space explicitly required with print, true otherwise
