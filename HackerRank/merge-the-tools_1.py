# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true


# S, N = input(), int(input()) 
S = 'AABCAAADA'
N = 3

for part in zip(*[iter(S)] * N):
    print(part)
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))



print(zip(*[iter(S)] * 3))


x = [1, 2, 3, 8]

y = [4, 5, 6, 0]

zipped = zip(x, y)

print(list(zipped))
# def merge_the_tools(string, k):

#     print(string, k)

#     new_work = []
#     sub_string = []

#     i = 0
#     t = 0

#     for letter in string:

#         sub_string.append(letter)
#         t = t + 1

#         if t == k:
#             t = 0
#             sub_string = list(dict.fromkeys(sub_string))
#             new_work.append(''.join(sub_string))
#             sub_string = []

#     for item in new_work:
#         print(item)






# merge_the_tools('AABCAAADA', 3)