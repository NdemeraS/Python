# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
#
#



x = 1
y = 1
z = 2
n = 3



#
# This does the thing using loops   
#

list_of_lists = []


for item_x in range(x + 1):
    for item_y in range (y + 1):
        for item_z in range(z + 1):
            if sum([item_x, item_y, item_z]) != n:  ## checking if number adds up to n:
                    if [item_x, item_y, item_z] not in list_of_lists:       ## check for duplicates
                        list_of_lists.append([item_x, item_y, item_z])      ## append  to list


print(list_of_lists)


#
# list comprehensions
#

new_list= []



print([[xx, yy, zz] for xx in range(x+1) for yy in range(y+1) for zz in range(z+1) if xx+yy+zz != n])