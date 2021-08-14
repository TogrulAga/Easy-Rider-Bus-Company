import re

string = input()
# your code
template = r"<START>(.*)<END>"

match = re.search(template, string, flags=re.DOTALL)

print(match.group(1))
