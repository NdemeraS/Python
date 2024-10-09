import string
alpha = string.ascii_lowercase

# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))


listing = ["e-d-c-b-a-b-c-d-e",	"--e-d-c-b-c-d-e--","----e-d-c-d-e----","------e-d-e------", "--------e--------"]

# print(listing)


# print("this is a sentence"[:0:-1])

print('\n'.join("this is a test"))

# print('\n'.join(listing[:0:-1] + listing))