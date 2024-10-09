s = "1 2 2 3 4 5 6 7 8  9"



s = s.split()

t = []
i = 0

while i < len(s):
    t.append(s[i].capitalize())
    i = i + 1

t = ' '.join(item for item in t)
# s = s.capitalize()

# print(s)
print(t)



# def solve(s):
#     List=s.split(' ')
#     newlist = []
#     for i in List:
#         newlist.append(i.capitalize())
    
#     return " ".join(newlist)