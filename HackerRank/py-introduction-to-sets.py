# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    # print(array)
    # print(sum(array))
    # print(len(array))
    # print(set(array))
    array = list(set(array))
    return sum(array)/len(array)


arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]

average(arr)

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)