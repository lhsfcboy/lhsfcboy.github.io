class Solution:
    """
    寻找两个有序数组的中位数
    
    提供三种实现方法：
    1. 直接操作数组法（从两端逐步删除元素）
    2. 二分查找法
    3. 比例调整法
    
    @param A: 有序数组A
    @param B: 有序数组B
    @return: 中位数
    """
    def get_median(self, number_list):
        """计算单个数组的中位数"""
        list_len = len(number_list)
        index = list_len // 2

        if list_len % 2 == 0:
            return (number_list[index] + number_list[index - 1]) / 2
        else:
            return number_list[index]

    def findMedianSortedArrays(self, A, B):
        """方法1：直接操作数组（从两端逐步删除元素）"""
        len_A = len(A)
        len_B = len(B)

        # 处理边界情况
        if len_A == len_B == 0:
            return None

        if len_A == 0:
            return self.get_median(B)
        if len_B == 0:
            return self.get_median(A)

        if len_A == len_B == 1:
            return (A[0] + B[0]) / 2

        # 主循环：从两端逐步删除元素
        while True:
            # 从左端删除较小的元素
            if not A:
                B.pop(0)
            elif not B:
                A.pop(0)
            elif A[0] <= B[0]:
                A.pop(0)
            else:
                B.pop(0)

            # 从右端删除较大的元素
            if not A:
                B.pop(-1)
            elif not B:
                A.pop(-1)
            elif A[-1] <= B[-1]:
                B.pop(-1)
            else:
                A.pop(-1)

            # 当剩余元素不超过2个时，计算中位数
            if len(A) + len(B) <= 2:
                return self.get_median(A + B)

    def findMedianSortedArrays2(self, A, B):
        """方法2：二分查找法"""
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        
        imin, imax = 0, m
        half_len = (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            if i < m and B[j-1] > A[i]:
                # i 太小，需要增大
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i 太大，需要减小
                imax = i - 1
            else:
                # i 刚好
                if i == 0:
                    max_left = B[j-1]
                elif j == 0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])
                    
                if (m + n) % 2 == 1:
                    return max_left
                    
                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])
                    
                return (max_left + min_right) / 2

    def findMedianSortedArrays3(self, A, B):
        """方法3：比例调整法"""
        m, n = len(A), len(B)
        total = m + n
        
        # 确保 A 是较短的数组
        if m > n:
            A, B, m, n = B, A, n, m
            
        # 如果较短的数组为空
        if m == 0:
            return self.get_median(B)
            
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (total + 1) // 2 - i
            
            # 处理边界情况
            A_left = float('-inf') if i == 0 else A[i-1]
            A_right = float('inf') if i == m else A[i]
            B_left = float('-inf') if j == 0 else B[j-1]
            B_right = float('inf') if j == n else B[j]
            
            if A_left > B_right:
                right = i - 1
            elif B_left > A_right:
                left = i + 1
            else:
                # 找到正确的分割
                if total % 2:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                    
        return 0.0


def run_tests():
    s = Solution()
    
    # 测试1：基本情况
    assert s.findMedianSortedArrays([1,2,3], [4,5,6]) == 3.5, "基本情况测试失败"
    assert s.findMedianSortedArrays2([1,2,3], [4,5,6]) == 3.5, "基本情况测试失败(方法2)"
    assert s.findMedianSortedArrays3([1,2,3], [4,5,6]) == 3.5, "基本情况测试失败(方法3)"
    
    # 测试2：数组长度不同
    assert s.findMedianSortedArrays([1,2,3,4,5,6], [2,3,4,5]) == 3.5, "不同长度测试失败"
    assert s.findMedianSortedArrays2([1,2,3,4,5,6], [2,3,4,5]) == 3.5, "不同长度测试失败(方法2)"
    assert s.findMedianSortedArrays3([1,2,3,4,5,6], [2,3,4,5]) == 3.5, "不同长度测试失败(方法3)"
    
    # 测试3：空数组
    assert s.findMedianSortedArrays([], [1]) == 1, "空数组测试失败"
    assert s.findMedianSortedArrays2([], [1]) == 1, "空数组测试失败(方法2)"
    assert s.findMedianSortedArrays3([], [1]) == 1, "空数组测试失败(方法3)"
    
    # 测试4：重叠范围
    assert s.findMedianSortedArrays([1,2], [1,2]) == 1.5, "重叠范围测试失败"
    assert s.findMedianSortedArrays2([1,2], [1,2]) == 1.5, "重叠范围测试失败(方法2)"
    assert s.findMedianSortedArrays3([1,2], [1,2]) == 1.5, "重叠范围测试失败(方法3)"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    run_tests()