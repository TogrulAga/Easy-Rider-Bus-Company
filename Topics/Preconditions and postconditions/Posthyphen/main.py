import re

string = input()
# your code here
template = r"(?<=-)\w+\b"

print(re.search(template, string).group())
