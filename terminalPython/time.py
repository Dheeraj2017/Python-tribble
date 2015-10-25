#!/usr/bin/python
import time
print "time.time(): %f " % time.time()
print time.localtime( time.time() )
print time.asctime( time.localtime(time.time()) )

#this code will only run in the python2 
