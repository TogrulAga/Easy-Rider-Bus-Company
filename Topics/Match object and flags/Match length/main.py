import re

template = r'are you ready??.?.?'

match = re.match(template, input())

if match:
    print(len(match.group()))
else:
    print(0)
