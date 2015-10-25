#!/usr/bin/python
str2 = "this is string example....wow!!!";
suffix = "wow!!!";
print (str2.endswith(suffix));
print (str2.endswith(suffix,20));
print (str2.endswith(suffix,32));
suffix = "is";
print (str2.endswith(suffix, 2, 4));
print (str2.endswith(suffix, 2, 6));