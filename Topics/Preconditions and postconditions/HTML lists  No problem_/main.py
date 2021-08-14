import re

string = input()
# your code here
template = r"(?<=<li>)[\w -]*(?=</li>)"

print(*re.findall(template, string), sep="\n")
