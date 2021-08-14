import re

string = input()
# your code here
template = r"^b[\w \\n]*l$"
match = re.match(template, string, flags=re.I | re.M)
print(match.group() if match else "No match")
