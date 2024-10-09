# https://leetcode.com/problems/plus-one/

digits = [1,2,3]


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # print(type(digits))
        newlist = []

        for item in digits:
            newlist.append(str(item))

        # print(newlist)

        digits = ''.join(newlist)
        digits = int(digits)
        digits = digits + 1
        digits = str(digits)
        digits = list(digits)

        final = []
        for item in digits:
            final.append(int(item))


        print(final)


test = Solution()

test.plusOne(digits)