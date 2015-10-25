#!/usr/bin/python
import calendar
'''
calendar.month(year,month,w=2,l=1)

Returns a multiline string with a calendar for month month of year year, one line per week plus two header
lines. w is the width in characters of each date; each line has length 7*w+6. l is the number of lines for each
week.

'''
cal=calendar.month(2008,2,6,2)
print "Here is the calendar: "
print cal;
cal1=calendar.prcal(2008,2,1,6)
'''
in the above code we don't required to use the print statement 
like print calendar.calendar(year,w,l,c)
'''

cal2=calendar.prmonth(2012,6,2,1)
#print cal2;

'''
Like print calendar.month(year,month,w,l).
'''
