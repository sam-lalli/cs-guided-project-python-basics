"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes):
    # Input: int, Output: int, no type conversion
    # 60 seconds in a minute
    return minutes * 60

#Examples
print(convert(5))
print(convert(3))
print(convert(2))


