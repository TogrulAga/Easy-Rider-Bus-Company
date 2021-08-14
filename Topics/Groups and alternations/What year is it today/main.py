import re


# put your regex in the variable template
template = r"\d{1,2}/\d{1,2}/(\d{4})|\d{1,2}\.\d{1,2}\.(\d{4})"
string = input()
# compare the string and the template
match = re.match(template, string)

if match is not None:
    print(match.group(1) if match.group(1) is not None else match.group(2))
else:
    print("None")
