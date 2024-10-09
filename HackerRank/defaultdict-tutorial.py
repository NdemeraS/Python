# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true


# n, m = list(map(int, input().split()))

# A = list(map(str, input().split()))



def check_index(list1, key):
    # print(list1)
    # print(key)
    newlist = []
    for index, item in enumerate(list1):
        if item == key:
            newlist.append(index + 1)
    print(newlist)




A = ['a', 'a', 'b', 'a', 'b']
B = ['a', 'b']


B_pos = []

# index = 0

A_pos = list(set(A))

for item in A_pos:
    if item in B:
        check_index(A, item)
    else:
        print("-1")


