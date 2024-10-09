# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
#

N = 4

e = 0
i = 0

list = []

cmd_list = [list.append(i), print(list), list.remove(i), list.insert(e, i), list.sort(), list.pop(i), list.sort(reverse=True)]


for item in range(N):
    print(item)
    cmd_list[item]



print(cmd_list)