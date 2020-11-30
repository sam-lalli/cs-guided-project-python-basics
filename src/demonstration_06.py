"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""

# input string, output boolean depening on number of x's and o's
# condtitional logic based on our count of x's and o's
def XO(txt):
    num_x = 0
    num_o = 0

    # looping through string
    # dont forget about case sensitivity, making everything lower case with lower() method
    for letter in txt.lower():
        if letter == "x":
            num_x += 1

        # does not need to be 'elif' because you will never get a letter that is an x and a o
        if letter == "o":
            num_o += 1

    return num_o == num_x

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))


