from functools import cmp_to_key

class Solution:
    """
    @param: nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        if not any(nums):
            return "0"
            
        nums = [str(num) for num in nums]
        sorted_nums = sorted(nums, key=cmp_to_key(self.sp_compare), reverse=True)
        return "".join(sorted_nums)
    
    def sp_compare(self, a, b):
        if a + b == b + a:
            return 0
        return -1 if a + b < b + a else 1
    
def test():
    s = Solution()
    tests = [
        ([4, 20], "420"),
        ([3, 30, 34, 5, 9], "9534330"),
        ([0, 0, 0], "0"),
        ([121, 12], "12121"),
        ([1, 10, 100], "110100")
    ]
    for nums, expected in tests:
        result = s.largestNumber(nums)
        print(f"{nums} -> {result} {'✓' if result == expected else '✗'}")

if __name__ == '__main__':
    test()