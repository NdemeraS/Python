# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
#


stamp = set()

N = int(input())

counter = 0

while counter < N:
    A = input()
    stamp.add(str(A))
    counter += 1

# print(N)
# print(stamp)
print(len(stamp))


# print(len(set([str(input()) for x in range(int(input()))])))