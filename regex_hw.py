# Write a function that takes a list of names and verifies names that are valid names using regex pattern and match. print the name if its valid, print invalid name if not
import re
def name_validator(names):
    pattern = re.compile(r"^[A-Z][a-z]* [A-Z][a-z]*( [A-Z[a-z]*)*$")
    for name in names:
        if pattern.match(name):
            print(name)
        else:
            print("Invalid name")
    return names
  
  

  
  
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]
name_validator(names)