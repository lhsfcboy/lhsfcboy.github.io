# 标记三个以上重复的字符

代码框架:
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

// 函数声明
char* markConsecutiveChars(const char *input);

int main() {
    // 测试用例
    assert(strcmp(markConsecutiveChars("AABBBCCCCDDEEEEE"), "0011111110011111") == 0);
    assert(strcmp(markConsecutiveChars("AAABBBCCC"), "111111111") == 0);
    assert(strcmp(markConsecutiveChars("AB"), "00") == 0);
    assert(strcmp(markConsecutiveChars("AAAABBBCC"), "111111100") == 0);
    printf("All tests passed!\n");
    return 0;
}

// 函数实现
char* markConsecutiveChars(const char *input) {
    int length = strlen(input);
    char *output = malloc(length + 1);  // 分配内存，C 语言中，malloc 返回 void *，直接赋值给 char * 不需要类型转换
    memset(output, '0', length); // 初始化 output  省略了 sizeof(char)，因为 sizeof(char) 始终为 1
    output[length] = '\0'; // 添加字符串结束符

    // 核心逻辑：标记连续字符


    // 打印当前的结果（仅用于调试）
    printf("Input:  %s\nOutput: %s\n", input, output);

    return output;
}

```

## 简单实现

```c
    int count = 1; // 初始化计数器
    for (int i = 1; i <= length; i++) {
        if (input[i] == input[i - 1]) {
            count++; // 连续相同字符，计数器加一
        } else {
            if (count >= 3) {
                // 将连续相同字符的位置标记为 '1'
                for (int j = i - count; j < i; j++) {
                    output[j] = '1';
                }
            }
            count = 1; // 重置计数器
        }
    }
    // 检查字符串末尾是否有未处理的序列
    if (count >= 3) {
        for (int j = length - count; j < length; j++) {
            output[j] = '1';
        }
    }
```

## 避开对最后一个字母的判断

处理最后一个数字的部分有些ugly, 是不是可以考虑先读入第一个字符, 然后开始循环, 比较 `i-1` 和 `i`
或者合并逻辑.

```c
    int count = 1;  // 用于计数连续字符
    for (int i = 0; i < length; i++) {
        if (i < length - 1 && input[i] == input[i + 1]) {
            count++;  // 如果当前字符与下一个字符相同，增加计数
        } else {
            // 如果当前字符与下一个字符不同或已到字符串末尾
            if (count > 1) {
                memset(output + (i - count + 1), '1', count);  // 标记为 '1'
            } else {
                output[i] = '0';  // 标记为 '0'
            }
            count = 1;  // 重置计数
        }
    }
```    

## 通过数组来暂存还没有结束匹配的字符

考虑用一个数组把已经开始匹配但是还没有结束的字符记录下来, 然后继续处理

```c
    int index_of_unfinished_match[length];  // 用于存储尚未结束匹配的索引
    int top = -1;  // 栈顶指针
    int count = 1;  // 用于计数连续字符

    for (int i = 0; i < length; i++) {
        if (i < length - 1 && input[i] == input[i + 1]) {
            if (top == -1 || index_of_unfinished_match[top] != i) {
                index_of_unfinished_match[++top] = i;  // 入栈，记录起始索引
            }
            count++;  // 增加计数
        } else {
            // 如果当前字符与下一个字符不同或已到字符串末尾
            if (top != -1) {
                // 标记所有记录的索引为 '1'
                for (int j = 0; j <= top; j++) {
                    output[index_of_unfinished_match[j]] = '1';
                }
                top = -1;  // 重置栈
            }
            output[i] = (count > 1) ? '1' : '0';  // 标记当前字符
            count = 1;  // 重置计数
        }
    }

    // 处理最后一组连续字符
    if (top != -1) {
        for (int j = 0; j <= top; j++) {
            output[index_of_unfinished_match[j]] = '1';
        }
    }
```    

对数组的操作:
- 只对数组尾部的数据感兴趣
  - 没有通过数组下标访问尾部以外的任何值
  - 添加元素每次都是在最右边
  - 删除元素每次都是在最右边

## WIP

WIP

```c
void markConsecutiveChars(char *input, char *output) {
    int length = strlen(input);
    memset(output, '0', length);  // 初始化 output，将所有字符标记为 '0'
    output[length] = '\0';  // 确保输出是一个有效的字符串

    int unmatched_index_array[length];  // 用于存储连续字符的起始索引
    int unmatched_index_size = 0;  

    for (int i = 0; i < length-1; i++) {
        // 如果当前字符和下一个字符相同，将当前索引入栈
        if (input[i] == input[i + 1]) {
            if (unmatched_index_size == 0 || unmatched_index_array[unmatched_index_size - 1] != i) {
                unmatched_index_array[unmatched_index_size] = i;  // 入栈，记录起始索引
                unmatched_index_size++;
            }
        } else {
            // 如果连续字符结束，处理栈中的所有元素
            if (unmatched_index_size >= 2) {  // 判断栈中是否有至少三个连续字符
                for (int j = 0; j < unmatched_index_size; j++) {
                    output[unmatched_index_array[j]] = '1';  // 标记栈中的所有索引为 '1'
                }
                output[i] = '1';  // 标记当前字符为 '1'
            } else {
                for (int j = 0; j < unmatched_index_size; j++) {
                    output[unmatched_index_array[j]] = '0';  // 如果不超过三个连续字符，标记为 '0'
                }
            }
            memset(unmatched_index_array, 0, sizeof(unmatched_index_array));  // 清空栈
            unmatched_index_size = 0;  // 重置栈顶指针
        }
    }

    // 处理最后一个字符（如果它是连续字符的一部分）
    if (unmatched_index_size >= 2) {  // 判断栈中是否有至少三个连续字符
        for (int j = 0; j < unmatched_index_size; j++) {
            output[unmatched_index_array[j]] = '1';  // 标记栈中的所有索引为 '1'
        }
        output[length - 1] = '1';  // 标记最后一个字符为 '1'
    } else {
        for (int j = 0; j < unmatched_index_size; j++) {
            output[unmatched_index_array[j]] = '0';  // 如果不超过三个连续字符，标记为 '0'
        }
    }

    // 打印当前的结果
    printf("Input:  %s\nOutput: %s\n", input, output);
}
```
