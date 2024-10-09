# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

from itertools import product

list = []

a = product([1,2,3],repeat = 2)

print(list[a])