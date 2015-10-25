#!/usr/bin/python
import calendar
a=int(raw_input("Enter the first year: "))
b=int(raw_input("\nEnter the second year: "))
'''
calendar.leapdays(y1,y2)
Returns the total number of leap days in the years within range(y1,y2)

'''
cal=calendar.leapdays(a,b)
print cal
