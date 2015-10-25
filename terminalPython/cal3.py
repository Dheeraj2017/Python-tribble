#!/usr/bin/python
import calendar
while 1 :
     a=int(raw_input("Enter the year to check leap year or not !!\n"))
     cal=calendar.isleap(a)
     if cal :
	print "leap year"
	break 
     else :
	print "not leap year"
print "\nthanks !!"
