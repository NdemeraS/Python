

s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"

max_width = 4

i = 0

empty_string = ""

for item in s:
    empty_string = empty_string + item
    # print(item)
    i = i + 1
    if i == max_width:
        print(empty_string)
        # print("Reset")
        empty_string = ""
        i = 0
        # print(empty_string)
        # print(i)

print(empty_string)



import textwrap

def wrap(string, max_width):

    i = 0

    empty_string = ""

    for item in string:
        empty_string = empty_string + item
        # print(item)
        i = i + 1
        if i == max_width:
            print(empty_string)
            # print("Reset")
            empty_string = ""
            i = 0
            # print(empty_string)
            # print(i)
    return

if __name__ == '__main__':
