#
#  https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=python
#
import string


    N = 10


    # This bit calculates the width of the rangoli. This is needed to work where the mid of each line will be
    #
    T = (N + (N-1))
    T = T + (T-1)

    # print(T)

    alpha = string.ascii_lowercase[0:N]
    dash = "-"
    # print(alpha)

    # final = ""

    # int = 0
    # for letter in alpha:
    #     final = final + "-" + letter

    # print(final)

    newFinal = ""
    sidStr = ""
    newStr = "-"


    while N > 1:
        N = N - 1
        # print(N)

        # newStr = alpha[N]
        # print(alpha[N])
        # print((newStr + alpha[N] + newStr[::-1]).center(17,"-"))

        # sidStr = sidStr + newStr + "-"
        newFinal = newFinal + (newStr + alpha[N] + newStr[::-1]).center(T,"-") + "\n"
        
        newStr = newStr + alpha[N] + "-"


        # print(newStr)
        # print(newStr.center(20,"-"))
        # newFinal = newFinal + newStr.center(20,"-") + "\n"


    # print(newFinal)


    # craete the middle line by running through the string from the alphabet. Converts the resulting list into a string and reverse it
    pattern = ''.join([item + "-" for item in alpha])[::-1]

    #Snipping the begging of the string
    pattern = pattern[1:]
    # print(pattern)


    pattern = pattern[0:-1] + pattern[::-1]
    # print(pattern)


    newFinal = newFinal + pattern + newFinal[::-1]
    print(newFinal)