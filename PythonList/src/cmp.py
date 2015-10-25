

#this works in python2 only not in python3

#!/usr/bin/python
list1, list2 = [123, 'xyz'], [456, 'abc']
a=cmp(list1, list2)
print (a)
print cmp(list2, list1);
list3 = list2 + [786];
print cmp(list2, list3);