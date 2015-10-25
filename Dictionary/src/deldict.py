#!/usr/bin/python
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
del dict1['Name']; # remove entry with key 'Name'
dict1.clear();
# remove all entries in dict1
del dict1 ;
# delete entire dictionary
print ("dict1['Age']: ", dict1['Age']);
print ("dict1['School']: ", dict1['School']);

#This will produce the following result. Note an exception raised, this is because after del dict dictionary does not
#exist any more: