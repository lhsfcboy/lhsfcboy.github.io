# 再次思考hello world



hello, world 程序中引用了

`#include <stdio.h>`



在Linux系统中，标准C库头文件stdio.h通常位于/usr/include/stdio.h路径下。这个文件包含了标准输入输出函数的声明，如printf、scanf等。其他路径下的stdio.h文件可能是特定于某些库或编译器版本的实现。




我的系统中有哪些stdio.h



```shell

# - 使用locate命令查找文件

sudo updatedb # 更新Linux系统的文件信息数据库

locate stdio.h



# - 使用find命令

sudo find /usr -name stdio.h

# 或者更精确一点, 在/user/include/路径下查找

# TODO: 编译时如何确定头文件的path

```



我们真正想知道的： gcc用的哪个头文件



```shell

gcc -print-file-name=include

```



## gcc如何决定头文件的搜索路径



显然我们肯定有办法指定gcc所需要搜索的具体路径。

编译器在编译C程序时, 会根据默认搜索路径、`-I` 选项、环境变量和其他选项来决定去哪里找头文件.

这里只介绍默认搜索路径。



### 默认搜索路径

gcc 编译器有一组默认的头文件搜索路径，这些路径通常包括系统的标准头文件目录。你可以使用以下命令查看 gcc 的默认头文件搜索路径和输出示例：



```shell

echo | gcc -E -v -

# 通过echo生成一个空输入，并将其传递给gcc进行预处理，

# 同时输出详细的编译器信息。

# 这样可以查看gcc的预处理器如何处理输入

# 以及使用的默认搜索路径和宏定义等信息



#include "..." search starts here:

#include <...> search starts here:

 /usr/local/include

 /usr/lib/gcc/x86_64-linux-gnu/9/include

 /usr/include/x86_64-linux-gnu

 /usr/include

End of search list.

```



## printf函数的代码



在上述的头文件中， 我们可以看到类似如下函数声明



```shell

extern int printf (const char *__restrict __format, ...);

```



`printf` 函数的源代码通常位于C标准库的实现中。不同的操作系统和编译器可能会有不同的实现。在GNU C库（glibc）中，`printf` 的源代码可以在glibc的源代码仓库中找到。



在glibc中，`printf` 的实现位于 `stdio-common` 目录下的 `printf.c` 文件中。你可以在glibc的源代码仓库中找到这个文件。



例如，你可以在GitHub上查看glibc的源代码仓库：

[https://github.com/bminor/glibc/blob/master/stdio-common/printf.c](https://github.com/bminor/glibc/blob/master/stdio-common/printf.c)



## 编译的时候具体



在编译和运行一个包含`printf`函数的Hello World程序时，`gcc`的处理过程如下：



1. **编译阶段**：`gcc`将源代码（如`hello.c`）编译成目标文件（如`hello.o`）。在这个阶段，`printf`函数的调用会被编译成对`printf`函数的外部引用。



2. **链接阶段**：`gcc`会将目标文件（如`hello.o`）与标准库（如`libc.a`或`libc.so`）链接。在这个阶段，`printf`函数的外部引用会被解析为标准库中的`printf`函数的实现（通常在`libc.a`或`libc.so`中）。



3. **运行阶段**：当程序运行时，操作系统会加载可执行文件，并将`printf`函数的调用解析为标准库中的实际实现。



因此，`gcc`在编译和链接阶段并不会直接访问`printf`的源代码，而是通过链接标准库中的预编译目标文件（如`printf.o`）来实现`printf`函数的调用。




# 编译过程概览



https://blog.csdn.net/weixin_44966641/article/details/120042638



# Make的Make： CMake

https://www.google.com/url?sa=i&url=https%3A%2F%2Fjuejin.cn%2Fpost%2F7273646418208145463&psig=AOvVaw0hp-5sDS9eWJeSGho0NLZ0&ust=1731373833851000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCJCG1ayM04kDFQAAAAAdAAAAABAN



# 程序为什么出错 数学模型 到 编程实践



现实世界的“整数”与C程序的int有什么区别？
