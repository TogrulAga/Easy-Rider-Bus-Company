import re


match = re.match(r"[a-zA-Z]", input())

if match:
    print("Thank you!")
else:
    print("Oops! The username has to start with a letter.")
