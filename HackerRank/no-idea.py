#
# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
#
import random

happy = 0

# Set n
# Set m

# n = [1, 5, 3]

# A = {3, 1}
# B = {5, 7}

n, m = input().split()
# n, m = int(input().split())
# m = int(float(input()))

n = int(n)
m = int(m)

nicelist = input().split()
# print(type(nicelist))

A = set(input().split())
B = set(input().split())

# print(nicelist)
# print(A)
# print(B)

for item in nicelist:
    if item in A:
        happy = happy + 1
    if item in B:
        happy = happy - 1

print(happy)

# n, m = input().split()

# sc_ar = input().split()

# A = set(input().split())
# B = set(input().split())
# print(sum([(i in A) - (i in B) for i in sc_ar]))