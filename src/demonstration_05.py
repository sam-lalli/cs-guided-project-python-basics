"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""

# Input: list of strings
# Output: list of strings sorted by length in ascending order
# shortest words come first to longest words

# need to iterate through each element (for)?
# can we use sort method?

def sort_by_length(lst):
    lst.sort(key= lambda x: len(x)) # callback function (lambda function), sorting based off length

    return lst
    

print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length(["may", "april", "september", "august"]))
print(sort_by_length([]))

