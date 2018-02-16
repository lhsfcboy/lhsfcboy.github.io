class Solution:
    """
    @param: str: A string
    @return: An integer
    """
    def atoi(self, str):
        
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        sum = 0
        sign = 1
        i = 0
        if str == '':
            return 0
        
        # 处理空格
        str = str.strip()
        l = len(str)
        
        # 处理正负号
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            i += 1
            sign = -1
            
        while i < l:
            # 处理非数字字符
            s = str[i]
            if not s.isdigit():
                break
            digit = int(s)
            
            # 处理当前溢出        
            if sum/10 > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN
                
            if INT_MAX - sum * 10 >= digit:
                sum = sum * 10 + digit
            else:
                return INT_MAX if sign == 1 else INT_MIN
                
            i += 1               
                
        return sum * sign


s = Solution()
print(s.atoi("-2147483649"))