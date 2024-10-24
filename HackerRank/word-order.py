
# names = ["bcdef", "abcdefg", "bcde", "bcdef"]

names = []

k = int(input())

l = 0

while l < k:
    names.append("")
    names[l] = input()
    l += 1

# print(names)
# total = []

y = 0

for item in names:
    total.append(0)

print(total)

x = 0 #where to start checking names in the list# Enter your code here. Read input from STDIN. Print output to STDOUT

# names = ["bcdef", "abcdefg", "bcde", "bcdef"]

names = []

k = int(input())

l = 0

while l < k:
    names.append("")
    names[l] = input()
    l += 1

# print(names)
total = []

y = 0

for item in names:
    total.append(0)

# print(total)

x = 0 #where to start checking names in the list



while x < len(names) - 1:
    temp = 0 #total number of occurrances for a name

    for item in names:
        if item == names[x]:
            temp = temp + 1
            total[x] = temp
          

    x = x + 1

z = 0

while z < len(names):
    if total[z] == 0:
        total.pop(z)

    z = z + 1

print(len(total))
print(*total)



while x < len(names) - 1:
    temp = 0 #total number of occurrances for a name

    for item in names:
        if item == names[x]:
            temp = temp + 1
            total[x] = temp
          

    x = x + 1

z = 0

while z < len(names):
    if total[z] == 0:
        total.pop(z)

    z = z + 1

for item in total:
    print(item)