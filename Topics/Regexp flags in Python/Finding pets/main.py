import re 

pets = input()
# your code here
template = r"(dog|cat|parrot|hamster)"
print(re.findall(template, pets, flags=re.I))
