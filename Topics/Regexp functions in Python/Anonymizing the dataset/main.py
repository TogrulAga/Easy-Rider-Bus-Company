import re

string = input()
# your code
template = r"(@[\w]+)"

string = re.sub(template, "<AUTHOR>", string, 1)
string = re.sub(template, "<HANDLE>", string)
print(string)
