"""
65. Median of two Sorted Arrays

1, 

2, 使用二分法来加快

3, 通过m, n的数值, 通过调整比例,来加快
"""


class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def get_median(self, number_list):
        list_len = len(number_list)
        index = int(list_len/2)

        if list_len % 2 == 0:
            return (number_list[index] + number_list[index -1])/2
        else:
            return number_list[index]

    def findMedianSortedArrays(self, A, B):
        # 直接操作数组
        # 在这个解法中, 我们依次从左右两端扣除元素

        len_A = len(A)
        len_B = len(B)

        if len_A == len_B == 0:
            return None

        if len_A == 0:
            return self.get_median(B)
        if len_B == 0:
            return self.get_median(A)

        if len_A == len_B == 1:
            A.extend(B)
            return self.get_median(A)

        while True:
            if not A:
                B.pop(0)
            elif not B:
                A.pop(0)
            elif A[0] <= B[0]:
                A.pop(0)
            else:
                B.pop(0)

            if not A:
                B.pop(-1)
            elif not B:
                A.pop(-1)
            elif A[-1] <= B[-1]:
                B.pop(-1)
            else:
                A.pop(-1)

            if len(A) + len(B) <= 2:

                return self.get_median(A+B)




s = Solution()
answer = s.findMedianSortedArrays([1,2,3,4,5,6],[2,3,4,5])
print(answer)