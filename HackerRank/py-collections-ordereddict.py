#
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# 


from collections import OrderedDict

supermarket = OrderedDict()

N = int(input())

item = 0

while item < N:
#     item_name, _, net_price = input().rpartition(' ')
#     print(type(item_name))
#     supermarket[item_name] = net_price
    
    *item_name_parts, net_price = input().split(' ')
    item_name = ' '.join(item_name_parts)
    supermarket[item_name] = net_price
    item = item + 1
# print(supermarket)

for thing in supermarket:
    print(thing + " " + supermarket[thing])


# from collections import OrderedDict
# N = int(input())

# dict = OrderedDict()
# for _ in range(N):
#     item_name, net_price = input().rsplit(' ', 1)
#     price = dict.get(item_name, 0)
#     dict[item_name] = int(net_price) + price
        
# for key, value in dict.items():
#     print(key, value)

