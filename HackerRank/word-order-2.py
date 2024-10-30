# https://www.hackerrank.com/challenges/word-order/problem

# Usesing Dictionaries


names = ["bcdef", "abcdefg", "bcde", "bcdef"]


d = {}
for item in names:
    if item in d.keys():
        d[item] = d[item] + 1
    else:
        d[item] = 1

print(d)

k = list(d.values())

print(k)