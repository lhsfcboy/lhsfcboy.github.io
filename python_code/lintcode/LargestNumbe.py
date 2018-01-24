import time


class Solution:
    """
    @param: nums: A list of non negative integers
    @return: A string
    """

    def largestNumber(self, nums):
        # write your code here
        pass

    def sp_compare(a, b):
        a, b = str(a), str(b)

        count = 0

        for (sx, sy) in zip(a, b):
            x, y = int(sx), int(sy)
            if x == y:
                continue
            else:
                return x > y
        return len(a) < len(b)


if __name__ == '__main__':
    print(Solution.sp_compare(4, 20))
