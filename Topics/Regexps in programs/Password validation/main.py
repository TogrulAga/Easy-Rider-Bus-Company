import re

password = input()
# your code here
template = r"[^ ][a-zA-Z\d]{6,15}$"

match = re.match(template, password)

if match:
    print("Thank you!")
else:
    print("Error!")
