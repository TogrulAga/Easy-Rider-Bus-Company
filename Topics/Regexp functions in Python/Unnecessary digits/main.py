import re       
names = input()
# your code here
template = r"\d+"

print(re.split(template, names))
