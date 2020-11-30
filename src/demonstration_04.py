"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""

    # Input, Output both int, no type conversion
    # length and width of a rectangle, 4 sides, 2 length, 2 width
    # Perimeter is the sum of all the sides.

    # Expand: no negative values can be passed in
    # if length < 0 or width < 0:
    #    return 0 

def find_perimeter(length, width):
    return (2 * length) + (2 * width)

#Examples
print(find_perimeter(6, 7))
print(find_perimeter(20, 10))
print(find_perimeter(2, 9))


