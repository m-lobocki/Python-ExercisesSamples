# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print
# the company name of a given email address. Both user names and company names are composed of letters only.

import re

email = input()
regex = re.match(r'(\w+)@(\w+)\.+(com)', email)
print(regex.group(2))