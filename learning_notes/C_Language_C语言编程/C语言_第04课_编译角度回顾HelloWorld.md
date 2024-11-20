# 再次思考hello world

一个典型的`hello, world` C语言程序中在第一行引用了`stdio.h`头文件。

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

## stdio.h头文件在哪里

stdio.h提供了:

- 基本的输入输出函数(printf、scanf等)
- 文件操作函数(fopen、fclose等)
- 流控制函数(fflush等)
- 各种输入输出相关的宏定义和类型定义

在Linux系统中，标准C库头文件stdio.h通常位于/usr/include/stdio.h路径下。这个文件包含了标准输入输出函数的声明，如printf、scanf等。其他路径下的stdio.h文件可能是特定于某些库或编译器版本的实现。

- macOS: 可能在Xcode工具链中
- Windows: 通常在编译器安装目录

那么我的系统中有哪些`stdio.h`

```shell
# - 使用locate命令查找文件
sudo updatedb # 更新Linux系统的文件信息数据库
locate stdio.h

# - 使用find命令
sudo find /usr -name stdio.h # 或者更精确一点, 在/user/include/路径下查找
```

这其中我们尤其想知道的是gcc编译时用的哪个头文件:

```shell
gcc -print-file-name=include
```

### gcc如何决定头文件的搜索路径

显然我们肯定有办法指定gcc所需要搜索的具体路径。

编译器在编译C程序时, 会根据默认搜索路径、`-I` 选项、环境变量和其他选项来决定去哪里找头文件.

```shell
# 1. 使用-I选项
gcc -I/path/to/headers program.c

# 2. 设置环境变量
export C_INCLUDE_PATH=/path/to/headers

# 3. 在源文件中使用相对路径
#include "../include/myheader.h"
```

这里只介绍默认搜索路径。

### 默认搜索路径

gcc 编译器有一组默认的头文件搜索路径，这些路径通常包括系统的标准头文件目录。你可以使用以下命令查看 gcc 的默认头文件搜索路径和输出示例：

```shell
echo | gcc -E -v -
# 通过echo生成一个空输入，并将其传递给gcc进行预处理，
# 同时输出详细的编译器信息。
# 这样可以查看gcc的预处理器如何处理输入
# 以及使用的默认搜索路径和宏定义等信息

# 输出示例: ##########################

#include "..." search starts here:
#include <...> search starts here:
 /usr/local/include
 /usr/lib/gcc/x86_64-linux-gnu/9/include
 /usr/include/x86_64-linux-gnu
 /usr/include
End of search list.
```

## printf函数的的实现细节

在上述的头文件中， 我们可以看到类似如下函数声明

```c
extern int printf (const char *__restrict __format, ...);
```

- `extern` - 表示这是一个外部函数
- `__restrict` - 是一个C语言关键字,表示指针所指向的内容只能通过该指针访问
- `...` - 表示这是一个可变参数函数

`printf` 函数的源代码通常位于C标准库的实现中。不同的操作系统和编译器可能会有不同的实现。在GNU C库（glibc）中，`printf` 的源代码可以在glibc的源代码仓库中找到。

在glibc中，`printf` 的实现位于 `stdio-common` 目录下的 `printf.c` 文件中。你可以在glibc的源代码仓库中找到这个文件。

例如，你可以在GitHub上查看glibc的源代码仓库：

[https://github.com/bminor/glibc/blob/master/stdio-common/printf.c](https://github.com/bminor/glibc/blob/master/stdio-common/printf.c)

## 编译链接过程详解

在编译和运行一个包含`printf`函数的Hello World程序时，`gcc`的处理过程如下：

### 预处理阶段

`gcc`将源代码（如`hello.c`）预处理，替换掉宏定义、包含文件、注释等

```shell
# 生成预处理后的文件
gcc -E hello.c -o hello.i
```

示例输出:

```c
// hello.i 内容片段
extern int printf (const char *__restrict __format, ...);

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### 编译阶段

`gcc`将源代码（如`hello.c`）编译成目标文件（如`hello.o`）。在这个阶段，`printf`函数的调用会被编译成对`printf`函数的外部引用

```shell
# 生成汇编代码
gcc -S hello.i -o hello.s
```

```asm
# hello.s
    .file   "hello.c"
    .text
    .section    .rodata
.LC0:
    .string "Hello, World!"
    .text
    .globl  main
    .type   main, @function
main:
    pushq   %rbp
    movq    %rsp, %rbp
    leaq    .LC0(%rip), %rdi
    call    printf@PLT
    movl    $0, %eax
    popq    %rbp
    ret
```

- PLT (Procedure Linkage Table) 用于动态链接
- 实际的printf函数地址在运行时解析

### 汇编阶段

```shell
# 生成目标文件
gcc -c hello.s -o hello.o
```

目标文件包含:

- 机器码
- 符号表
- 重定位信息

查看目标文件信息:

```obj
# 查看符号表
nm hello.o

# 输出示例
                 U printf
0000000000000000 T main
```

- U表示未定义符号,需要在链接时解析

### 链接阶段

`gcc`会将目标文件（如`hello.o`）与标准库（如`libc.a`或`libc.so`）链接。在这个阶段，`printf`函数的外部引用会被解析为标准库中的`printf`函数的实现（通常在`libc.a`或`libc.so`中）

```shell
# 生成可执行文件
gcc hello.o -o hello
```

链接器的主要工作:

- 符号解析
  - 将printf的引用与libc中的实现关联
  - 处理其他外部符号引用
- 代码重定位
  - 确定各段的最终地址
  - 修正地址相关的指令

查看动态链接库依赖

```shell
ldd hello

# 输出示例
linux-vdso.so.1
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
/lib64/ld-linux-x86-64.so.2
```

### 运行阶段

当程序运行时，操作系统会加载可执行文件，并将`printf`函数的调用解析为标准库中的实际实现

- 程序加载阶段: 可执行文件 -> 内存映射 -> 动态链接器初始化
- 程序执行阶段: 应用程序 -> PLT/GOT -> libc.so中的printf实现

### 总结

因此，`gcc`在编译和链接阶段并不会直接访问`printf`的源代码，而是通过链接标准库中的预编译目标文件（如`printf.o`）来实现`printf`函数的调用。

```shell
# 显示编译详细信息
gcc -v hello.c -o hello

# 显示链接库搜索路径
gcc -print-search-dirs

# 显示链接的库
gcc -print-files

# 使用strace跟踪系统调用
strace ./hello

# 使用ltrace跟踪库调用
ltrace ./hello
```
