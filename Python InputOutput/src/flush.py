#!/usr/bin/python
# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
# Here it does nothing, but you can call it with read operation.
fo.flush()
# Close opened file
fo.close()
'''
The method flush() flushes the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.
Python automatically flushes the files when closing them. But you may want to flush the data before closing any
file.
'''