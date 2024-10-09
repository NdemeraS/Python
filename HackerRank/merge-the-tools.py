# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true




def merge_the_tools(string, k):

    print(string, k)

    new_work = []
    sub_string = []

    i = 0
    t = 0

    for letter in string:

        sub_string.append(letter)
        t = t + 1

        if t == k:
            t = 0
            sub_string = list(dict.fromkeys(sub_string))
            new_work.append(''.join(sub_string))
            sub_string = []

    for item in new_work:
        print(item)






merge_the_tools('AABCAAADA', 3)