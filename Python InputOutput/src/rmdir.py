#!/usr/bin/python
import os
# This would remove "/tmp/test" directory.
os.rmdir( "/tmp/test" )   
'''
The rmdir() method deletes the directory, which is passed as an argument in the method.
Before removing a directory, all the contents in it should be removed.
'''