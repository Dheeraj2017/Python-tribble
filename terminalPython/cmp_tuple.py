#!/usr/bin/python
#NOTE that this code will run only in python2 interpreter
# but this is not run in the python 3
#so be careful while running 
tuple1, tuple2 = (123, 'xyz'), (456, 'abc')
print (cmp(tuple1,tuple2));
print (cmp(tuple2,tuple1));
tuple3 = tuple2 +(786,);
print (cmp(tuple2,tuple3));

