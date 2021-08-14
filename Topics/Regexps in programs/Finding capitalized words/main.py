import re

string = input()
# your code here
cap_words = r"[A-Z][a-zA-Z]+"
digits = r"\d+"

match_words = re.findall(cap_words, string)
match_digits = re.findall(digits, string)
print(f"Capitalized words:  {', '.join(match_words)}")
print(f"Digits:  {', '.join(match_digits)}")
