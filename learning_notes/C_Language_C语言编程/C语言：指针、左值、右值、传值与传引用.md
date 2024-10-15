## 前言

C 语言中的函数有传值和传引用（传指针）的区别。本篇将列出讨论大纲。

通过学习，我们将认识到，C 语言中所谓的传引用实际上是通过传递指针的值来实现的。


## 前置知识的复习与内存概念的引入

```c
int a; // 声明变量 a
a = 1; // 将值 1 赋给变量 a
```

等号 `=` 在 C 语言中代表赋值操作，其效果是把等号右边的值，赋给等号左边的变量。这里我们将引入对左值和右值的初步理解：

- **左值**：等号左边的，或者说允许出现在等号左边的，通常都是具名对象，也就是变量名。
- **右值**：不是左值的就是右值，右值是一个具体的值，比如数字 `10`，或者表达式的临时结果，例如 `a + 5`。

下面我们从内存的角度再看一次上述代码的含义。

第一行，我们声明了变量以后，计算机会给这个变量分配一片相应的内存空间，并在符号表中记录这个内存空间的具体地址。

> **注意**：符号表是真实存在的，不是为了方便理解创造的概念。当然这里对于具体细节进行了大幅度的简化。

### 符号表部分

| 标识符 | 类型 | 内存地址           |
| ------ | ------ | ------------------ |
| a      | int    | 0x7FFC1234ABCD   |
| ...... | ...... | ......           |
| ...... | ...... | ......           |

注意：内存地址是示意性的，每次运行程序时可能会变化。

### 变量值部分

| 内存地址          | 值             |
| ----------------- | -------------- |
| ......            | ......         |
| 0x7FFC1234ABCD    | (尚未初始化)    |
| ......            | ......         |
| ......            | ......         |

这里我们升级一下对左值的认识：

- **左值**代表了一片内存空间，有自己的内存地址。例如，变量名都是左值。
这个对象在内存中有一个具体的位置（地址），程序可以通过这个地址来访问或修改对象的值。例如，变量就是典型的左值，它们在内存中有一定的地址，可以被修改和重新赋值。
```c
int a = 1;   // a 是左值
int b;
b = a;       // b 是左值，a 是右值
```

这里 `a` 是个变量，可是一会在左边当左值，一会在右边当右值，为什么？

当变量出现在右边的时候有一个隐式的转换过程，左值到右值转换（lvalue-to-rvalue conversion）。

- `a` 出现在左边时，表示的是一片内存区域，用伪代码表示为：

  ```
  MemorySpace(a)
  ```

- `a` 出现在右边时，表示的是对应内存区域内的值，有一个隐式的转换过程，用伪代码表示为：

  ```
  ValueOf(MemorySpace(a))
  ```

## 内存角度来看简单的传值引用
```c
#include <stdio.h>

int sum(int x, int y) {
    return x + y;
}

int main() {
    int a = 3;
    int b = 4;
    int result = sum(a, b);
    
    printf("The sum of %d and %d is: %d\n", a, b, result);
    
    return 0;
}
```

调用函数 `sum` 之前
- 符号表
| 标识符 | 类型 | 内存地址           |
| ------ | ------ | ------------------ |
| a      | int    | 0x7FFC1234ABCD   |
| b      | int    | 0x7FFC1234ABCE   |
| ...... | ...... | ......           |

- 变量值部分

| 内存地址编号       | 内存的内容      |
| ----------------- | -------------- |
| ......            | ......         |
| 0x7FFC1234ABCD    | 3              |
| 0x7FFC1234ABCE    | 4              |
| ......            | ......         |


调用函数 `sum` 的过程
- 符号表
这里的示意图与实际情况不符合

| 标识符          | 类型   | 内存地址           |
| ------          | ------ | ---------------- |
| a               | int    | 0x7FFC1234ABCD   |
| b               | int    | 0x7FFC1234ABCE   |
| ......          | ...... | ......           |
| x of sum()      | int    | 0xABCDEFGH1234   |
| y of sum()      | int    | 0xABCDEFGH1235   |
| return of sum() | int    | 0xABCDEFGH1236   |
- 变量值部分

| 内存地址          | 值             |
| ----------------- | -------------- |
| ......            | ......         |
| 0x7FFC1234ABCD    | 3              |
| 0x7FFC1234ABCE    | 4              |
| ......            | ......         |
| 0xABCDEFGH1234    | 3              |
| 0xABCDEFGH1235    | 4              |
| 0xABCDEFGH1236    | 7              |

## 修改参数的第一次尝试

```c
#include <stdio.h>
void sub(int p);  // 更好的名字是subtract()
int main()
{
    int a = 1;
    sub(a);
    printf("Value of a: %d\n", a);
}
void sub(int p) // 伪代码来说, 这里相当于执行了p = ValueOf(a);
{
    p = p - 1;
}
```

从内存的角度分析，如上程序的执行，并认识到函数的调用是复制了参数的值。

- 符号表的示意图

| 标识符          | 类型   | 内存地址           |
| ------          | ------ | ---------------- |
| a               | int    | 0x7FFC1234ABCD   |
| ......          | ...... | ......           |
| p of sub()      | int    | 0xABCDEFGH1234   |

注意这里没有`return of sub()`, 想想为什么.

- 变量值部分
`subb()`的调用开始时:

| 内存地址          | 值             |
| ----------------- | -------------- |
| ......            | ......         |
| 0x7FFC1234ABCD    | 1              |
| ......            | ......         |
| 0xABCDEFGH1234    | 1              |

`subb()`的调用过程中:

| 内存地址          | 值             |
| ----------------- | -------------- |
| ......            | ......         |
| 0x7FFC1234ABCD    | 1              |
| ......            | ......         |
| 0xABCDEFGH1234    | 0              |

# 指针的介绍

- **一元解引用操作符 `*`**：需要一个右值参数，返回一个左值结果。
- **一元取地址操作符 `&`**：需要一个左值参数，返回一个右值。

解引用指针代表了一个内存区域，也是左值

```c
int x = 10;
int y;
y = x + 5; // x 是左值，但在表达式中被转换为右值；x + 5 的结果是右值
int *p = &x; // &x 取地址操作，需要左值，x 是左值
```


# 通过传指针实现对参数的修改

```c
#include <stdio.h>

void my_func(int* p)
{
    printf("\nmy_func() is running!!!\n");
    printf("Argument value: %p\n\n", p);
    *p = -1; // 把右端的值赋给左端，*的意思是从指针类型的变量 p 的值所指向的内存区域
    p = NULL;
}

int main()
{
    int a = 1;
    int* p; // 这里定义了一个指针变量 p，注意变量的名字是 p，而不是 *p
    p = &a; // & 符号这里表示取变量的内存地址
    printf("Value of a:          %d\n", a);
    printf("Memory Address of a: %p\n", &a);
    printf("Value of p:          %p\n", p);
    printf("Value of *p:         %d\n", *p);

    my_func(&a); // 等价于 my_func(p); 吗？
    printf("Value of a:          %d\n", a);
    printf("Memory Address of a: %p\n", &a);
    printf("Value of p:          %p\n", p);
    printf("Value of *p:         %d\n", *p);
}
```

**某一次执行的结果**

```
Value of a:          1
Memory Address of a: 0000006CBBDCF7E4
Value of p:          0000006CBBDCF7E4
Value of *p:         1

my_func() is running!!!
Argument value: 0000006CBBDCF7E4

Value of a:          -1
Memory Address of a: 0000006CBBDCF7E4
Value of p:          0000006CBBDCF7E4
Value of *p:         -1
```


# 课后习题

**(1) 下面我们试着用函数来实现自增，模仿 `a++` 的效果，请用内存示意图解释这个过程**

```c
#include <stdio.h>
int APlusPlus(int* a) {
    int original_value = *a; // 保存当前的值
    (*a) = original_value + 1; // 递增变量的值
    return original_value; // 返回原始值
}
int main() {
    int x = 5;
    printf("Before: %d\n", x);
    int result = APlusPlus(&x);
    printf("Result: %d\n", result); // 返回原始值
    printf("After:  %d\n", x); // 打印递增后的值
    return 0;
}
```

**(2) 请实现一个函数 `int PlusPlusA()` 要求能实现 `++a` 的效果**
