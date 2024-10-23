```
154. Regular Expression Matching 

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(string s, string p)
Have you met this question in a real interview? Yes
Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

```


```python
class Solution:
    """
    @param s: 输入字符串
    @param p: 包含 "." 和 "*" 的模式串
    @return: 返回是否匹配
    """
    def isMatch(self, s, p):
        # 创建dp表格，大小为 (len(s)+1) x (len(p)+1)
        # dp[i][j] 表示 s 的前 i 个字符是否匹配 p 的前 j 个字符
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # 空字符串匹配空模式
        dp[0][0] = True
        
        # 处理 s为空，而p以 x* 形式开始的情况
        # 比如 s="" 可以匹配 p="a*"
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # 填充dp表格
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    # 当前字符匹配（相同字符或者是点号）
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # 处理星号的情况，分两种情况：
                    # 1. 不使用星号和它前面的字符，比如 ab 匹配 abc*
                    # 2. 使用星号，且前一个字符可以匹配当前字符，比如 aaa 匹配 a*
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == '.' or p[j-2] == s[i-1]))
                    
        return dp[len(s)][len(p)]


def run_tests():
    solution = Solution()
    
    # 测试用例1: 基本字符匹配
    assert not solution.isMatch("aa", "a"), "测试1失败：aa 不应该匹配 a"
    assert solution.isMatch("aa", "aa"), "测试2失败：aa 应该匹配 aa"
    assert not solution.isMatch("aaa", "aa"), "测试3失败：aaa 不应该匹配 aa"
    
    # 测试用例2: 星号匹配
    assert solution.isMatch("aa", "a*"), "测试4失败：aa 应该匹配 a*"
    assert solution.isMatch("aaa", "a*"), "测试5失败：aaa 应该匹配 a*"
    assert solution.isMatch("", "a*"), "测试6失败：空字符串应该匹配 a*"
    
    # 测试用例3: 点号匹配
    assert solution.isMatch("aa", ".."), "测试7失败：aa 应该匹配 .."
    assert solution.isMatch("ab", ".."), "测试8失败：ab 应该匹配 .."
    
    # 测试用例4: 点号和星号组合
    assert solution.isMatch("aa", ".*"), "测试9失败：aa 应该匹配 .*"
    assert solution.isMatch("ab", ".*"), "测试10失败：ab 应该匹配 .*"
    assert solution.isMatch("aab", "c*a*b"), "测试11失败：aab 应该匹配 c*a*b"
    
    # 测试用例5: 复杂组合
    assert solution.isMatch("aaa", "ab*ac*a"), "测试12失败：aaa 应该匹配 ab*ac*a"
    assert solution.isMatch("aaa", ".*a"), "测试13失败：aaa 应该匹配 .*a"
    assert not solution.isMatch("ab", ".*c"), "测试14失败：ab 不应该匹配 .*c"
    
    # 测试用例6: 边界情况
    assert solution.isMatch("", ""), "测试15失败：空字符串应该匹配空模式"
    assert not solution.isMatch("", "a"), "测试16失败：空字符串不应该匹配 a"
    assert solution.isMatch("", "a*"), "测试17失败：空字符串应该匹配 a*"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    run_tests()
```