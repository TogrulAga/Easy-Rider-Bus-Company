import re

string = input()
# your code here
template = r"(?<=\$)\d+"

print(f"This week you have spent:  {sum(map(int, re.findall(template, string)))} dollars")
