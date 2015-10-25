#!/usr/bin/python
import re

file = """ 
Domain ID:D4397233-AFIN^M
Domain Name:ARYACOLLEGE.IN^M
Created On:13-Aug-2010 15:10:18 UTC^M
Last Updated On:31-Jul-2015 09:18:09 UTC^M
Expiration Date:13-Aug-2016 15:10:18 UTC^M
Sponsoring Registrar:GoDaddy.com, LLC (R101-AFIN)^M
Status:CLIENT DELETE PROHIBITED^M
Status:CLIENT RENEW PROHIBITED^M
Status:CLIENT TRANSFER PROHIBITED^M
Status:CLIENT UPDATE PROHIBITED^M
Registrant ID:CR160949096^M
Registrant Name:Akhil Pandey^M
Registrant Organization:ARYA College of Engineering & I.T.^M
Registrant Street1:SP-42, Kukas Industrial Area^M
Registrant Street2:RIICO^M
Registrant Street3:^M
Registrant City:Jaipur^M
Registrant State/Province:Rajasthan^M
Registrant Postal Code:302028^M
Registrant Country:IN^M
Registrant Phone:+91.1426227176^M
Registrant Phone Ext.:^M
Registrant FAX:^M
Registrant FAX Ext.:^M
Registrant Email:akhil@aryacollege.in^M
Admin ID:CR160949100^M
Admin Name:Akhil Pandey^M
Admin Organization:ARYA College of Engineering & I.T.^M
Admin Street1:SP-42, Kukas Industrial Area^M
Admin Street2:RIICO^M
Admin Street3:^M
Admin City:Jaipur^M
Admin State/Province:Rajasthan^M
Admin Postal Code:302028^M
Admin Country:IN^M
Admin Phone:+91.1426227176^M
Admin Phone Ext.:^M
Admin FAX:^M
Admin FAX Ext.:^M
Admin Email:akhil@aryacollege.in^M
Tech ID:CR160949098^M
Tech Name:Akhil Pandey^M
Tech Organization:ARYA College of Engineering & I.T.^M
Tech Street1:SP-42, Kukas Industrial Area^M
Tech Street2:RIICO^M
Tech Street3:^M
Tech City:Jaipur^M
Tech State/Province:Rajasthan^M
Tech Postal Code:302028^M
Tech Country:IN^M
Tech Phone:+91.1426227176^M
Tech Phone Ext.:^M
Tech FAX:^M
Tech FAX Ext.:^M
Tech Email:akhil@aryacollege.in^M
Name Server:NS1.AGBARGAINHOSTING.COM^M
Name Server:NS2.AGBARGAINHOSTING.COM^M
"""
#list = re.findall("'[^'Admin]*M", file)
#regex = "(A\w+)"
#regex= "[A]\w+"

m=file.readlines("Admin Name")
if m:
	print m
else :
	print "not found"

'''list = re.findall(regex,file)
for x in list:
    print (x)
'''
print "thanks for using"
