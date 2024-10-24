# Enter your code here. Read input from STDIN. Print output to STDOUT

# M = {2, 4, 5, 9}

# N = {2, 4, 11, 12}

M = set()
N = set()

t1 = int(input())
while t1 > 0:
    t2 = int(input())
    M.add(t2)
    t1 = t1 -1

t1 = int(input())
while t1 > 0:
    t2 = int(input())
    N.add(t2)
    t1 = t1 -1

print(M)
print(N)


a = list(M.difference(N))
b = list(N.difference(M))

# print(a)
# print(b)

newS = set()
# newS.update(a)
# newS.update(b)

for item in a:
    newS.add(item)

for item in b:
    newS.add(item)

# print(sorted(newS))

newlist = list(sorted(newS))

for item in newlist:
    print(item)