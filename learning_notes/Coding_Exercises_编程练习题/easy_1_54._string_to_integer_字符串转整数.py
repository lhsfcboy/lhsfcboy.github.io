class Solution:
    """
    字符串转整数 (atoi) 的实现
    
    规则：
    1. 忽略前导空格
    2. 处理可选的正负号
    3. 处理数字字符，直到遇到非数字字符
    4. 处理溢出情况，返回 INT_MAX 或 INT_MIN
    
    @param str: 输入字符串
    @return: 转换后的整数
    """
    def atoi(self, str):
        # 定义整数的最大值和最小值
        INT_MAX =  2147483647    # 2^31 - 1
        INT_MIN = -2147483648    # -2^31
        sum = 0                  # 累积结果
        sign = 1                 # 符号，1表示正数，-1表示负数
        i = 0                    # 字符串索引
        
        # 处理空字符串
        if str == '':
            return 0
        
        # 去除前导和尾部空格
        str = str.strip()
        l = len(str)
        
        # 处理空字符串（去除空格后）
        if l == 0:
            return 0
            
        # 处理符号
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            i += 1
            sign = -1
            
        # 处理数字
        while i < l:
            s = str[i]
            # 遇到非数字字符就停止
            if not s.isdigit():
                break
                
            digit = int(s)
            
            # 检查乘10是否会溢出
            if sum > INT_MAX // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            # 检查加digit是否会溢出
            if INT_MAX - sum * 10 >= digit:
                sum = sum * 10 + digit
            else:
                return INT_MAX if sign == 1 else INT_MIN
                
            i += 1               
                
        return sum * sign


def run_tests():
    s = Solution()
    
    # 测试1：基本数字转换
    assert s.atoi("123") == 123, "基本数字转换失败"
    assert s.atoi("-123") == -123, "负数转换失败"
    
    # 测试2：处理空格
    assert s.atoi("   123") == 123, "前导空格处理失败"
    assert s.atoi("123   ") == 123, "尾部空格处理失败"
    assert s.atoi("   123   ") == 123, "前后空格处理失败"
    
    # 测试3：正负号处理
    assert s.atoi("+123") == 123, "正号处理失败"
    assert s.atoi("-123") == -123, "负号处理失败"
    
    # 测试4：非法字符处理
    assert s.atoi("123abc") == 123, "非法后缀处理失败"
    assert s.atoi("abc123") == 0, "非法前缀处理失败"
    
    # 测试5：边界值处理
    assert s.atoi("2147483647") == 2147483647, "最大值处理失败"
    assert s.atoi("-2147483648") == -2147483648, "最小值处理失败"
    assert s.atoi("2147483648") == 2147483647, "最大值溢出处理失败"
    assert s.atoi("-2147483649") == -2147483648, "最小值溢出处理失败"
    
    # 测试6：特殊输入
    assert s.atoi("") == 0, "空字符串处理失败"
    assert s.atoi("  ") == 0, "纯空格字符串处理失败"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    run_tests()