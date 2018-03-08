# 编写一个简单的解释器(1)

## 个位数加法器

需求:

 - 只允许输入个位数
 - 此时支持的唯一一个运算符是加法
 - 输入中不允许有任何的空格符号

用例:
```
$ python calc1.py
calc> 3+4
7
calc> 3+5
8
calc> 3+9
12
calc>
```


```python
# 标记类型
#
# EOF （end-of-file 文件末尾）标记是用来表示所有输入都解析完成
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token 类型: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        # token 值: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', 或 None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()
        
class Interpreter(object):
    def __init__(self, text):
        # 用户输入字符串, 例如 "3+5"
        self.text = text
        # self.pos 是 self.text 的索引
        self.pos = 0
        # 当前标记实例
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """词法分析器（也说成扫描器或者标记器）

        该方法负责把一个句子分成若干个标记。每次处理一个标记
        """
        text = self.text

        # self.pos 索引到达了 self.text 的末尾吗？
        # 如果到了，就返回 EOF 标记，因为没有更多的
        # 能转换成标记的输入了
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # 从 self.pos 位置获取当前的字符，
        # 基于单个字符判断要生成哪种标记
        current_char = text[self.pos]
        # 如果字符是一个数字，就把他转换成一个整数，生成一个 INTEGER # 标记，累加 self.pos 索引，指向数字后面的下一个字符，
        # 并返回 INTEGER 标记
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        # 将当前的标记类型与传入的标记类型作比较，如果他们相匹配，就
        # “eat” 掉当前的标记并将下一个标记赋给 self.current_token，
        # 否则抛出一个异常
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # 将输入中的第一个标记设置成当前标记
        self.current_token = self.get_next_token()

        # 我们期望当前标记是个位数。
        left = self.current_token
        self.eat(INTEGER)

        # 期望当前标记是 ‘+’ 号
        op = self.current_token
        self.eat(PLUS)

        # 我们期望当前标记是个位数。
        right = self.current_token
        self.eat(INTEGER)

        # 上述操作完成后，self.current_token 被设成 EOF 标记
        # 这时成功找到 INTEGER PLUS INTEGER 标记序列
        # 这个方法就可以返回两个整数相加的结果了，
        # 即高效的解释了用户输入
        result = left.value + right.value
        return result
```
