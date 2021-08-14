import re

template = r'... Jude'

match = re.match(template, input())

if match:
    print(match.group())
else:
    print(None)
