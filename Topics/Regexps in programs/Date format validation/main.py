import re

string = input()
# your code here
template = r"([0-2][1-9]|[3][01])/(0[1-9]|1[0-2])/[\d]{4}"

match = re.match(template, string)

print(match is not None)
