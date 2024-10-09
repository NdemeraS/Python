N = 99
M = 297

dash = "-"
middle_string = ".|."
welcome = "WELCOME"

line = ""
half = N // 2

mark = ((M - 3) / 2) + 1 # This is how to mark the start of the dash

dash_mult = 1




for i in range(half):
    j = 1
    while j <= M:
        if j == mark:
            line = line + (middle_string * dash_mult) #specified the number of middle strings to print. Start at 1
            j = j + (3 * dash_mult) #the number of white spaces to jump on the line after adding the middle_string
        else:
            line = line + dash
            j = j + 1
    dash_mult = dash_mult + 2 # add to the number of middlle strings to print
    
    print(line)
    line = ""


# print( (int(M-7)/2))
# print(int(7.0) * dash)

print( int((M-7)/2) * dash + welcome + int((M-7)/2)*dash)


# print(mark)
# print(dash_mult)

mark = 4
dash_mult = dash_mult - 2

for i in range(half):
    j = 1
    while j <= M:
        if j == mark:
            line = line + (middle_string * dash_mult) #specified the number of middle strings to print. Start at 1
            j = j + (3 * dash_mult) #the number of white spaces to jump on the line after adding the middle_string
        else:
            line = line + dash
            j = j + 1
    mark = mark + 3 # set mark for next line
    dash_mult = dash_mult - 2 # add to the number of middlle strings to print
    print(line)
    line = ""