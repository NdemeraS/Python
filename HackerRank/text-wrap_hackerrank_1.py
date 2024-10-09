##------

# st = input().split()
# n = int(st[0])
# m = int(st[1])

# print(st)

# x=1
# for i in range(n):
#     a = n//2
#     if i < a:
#         print(('.|.'*x).center(m,'-'))
#         x+=2
#     if i==a:
#         print('WELCOME'.center(m,'-'))
#     if i > a:
#         x-=2
#         print(('.|.'*x).center(m,'-'))

##------

n = 7
m = 21

pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

print("string".center(3, 'w'))

