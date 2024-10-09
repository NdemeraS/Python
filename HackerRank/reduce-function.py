# https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true


from functools import reduce
from fractions import Fraction
from math import gcd



print(reduce(lambda x, y: y+x, [2,4,8], 3))


print (Fraction(11, 35))


print(reduce(gcd, [2,4,8], 3))
