'''The method fileno() returns the integer file descriptor that is used by the underlying implementation to request I/O
operations from the operating system.'''
#!/usr/bin/python
# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
fid = fo.fileno()
print "File Descriptor: ", fid
# Close opened file
fo.close()