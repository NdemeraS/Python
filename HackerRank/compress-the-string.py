# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

# incomplete


N = 1222311

N1 = str(N)

N2 = N1[:]

print(N2)


F = []

x1 = 0
x2 = 1

while x1 < len(N1):

    k = 1

    if N1[x1] == N2[x2]:

        while x2 < len(N2):
            if N1[x1] == N2[x2]:
                k = k + 1
                x2 = x2 + 1
            else:
                F.append((k, N1[x1]))
                x2 = x2 + 1
                x1 = x2
                break
    else:
        F.append((k, N1[x1]))
        x1 = x1 + 1
        x2 = x2 + 1

    F.append((k, N1[x1]))
    x2 = x2 + 1
    x1 = x2
                


print(*F)


# s = (1, 2)

# L = [(2, 1), (4, 3)]

# print(*L)-