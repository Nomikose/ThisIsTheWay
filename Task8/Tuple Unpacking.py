# Tuples can be used to output multiple values from a function.
# You need to make a function called calc(), that will take the side length of a square as its argument
# and return the perimeter and area using a tuple.
# The perimeter is the sum of all sides, while the area is the square of the side length.

def calc(x):
    p = 0
    a = 0
    p = 4*x
    a = x**2
    return p, a

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))