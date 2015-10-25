#!/usr/bin/python
number=input("enter the numeric value of which you want to display the table: ")
endnumber=input("enter the numeric number upto which you want to display the table: ")
endnumber=endnumber*number
tableof=1
for i in range(number,endnumber+1,number) :
	print "%d * %d = %d" % (number,tableof,i)
	tableof+=1	
