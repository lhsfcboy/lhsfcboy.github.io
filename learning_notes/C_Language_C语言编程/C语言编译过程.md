# C语言编译过程

## `main`函数怎么找到`rot`函数定义的?

看下面的简单程序

1. **`main.c`**: 调用了 `rot()` 函数
2. **`rot18.h`**: 只声明了 `rot(char str[])` 函数
3. **`rot18.c`**: 包含了 `rot()` 函数的基本实现

```c
### 文件1: `main.c`
#include "rot18.h"

int main(void) {
    char str[] = "Hello, World!";
    rot(str);
    return 0;
}
```

```c
### 文件2: `rot18.h`
void rot(char str[]);
```

```c
### 文件3: `rot18.c`
#include "rot18.h"

void rot(char str[]) {
    printf("Rot function called with: %s\n", str);
}
```

上述源文件可以生成一个可执行文件`main.out`
```bash
gcc main.c rot18.c -o main.out
```

`main.c`只包含了`rot18.h`, `rot18.h`也不过只有一句声明, 那么程序是怎么找到`rot18()`函数的具体实现的?

### 编译链接到执行
```bash
gcc -c main.c -o main.o
gcc -c rot18.c -o rot18.o
```
编译（compilation）：当你编译 main.c 时，编译器会找到 #include "rot18.h"，并通过头文件知道有一个叫做 rot() 的函数，它的具体实现可能在别的文件中。
编译器会检查 main.c 文件中是否有语法错误，并生成目标文件（main.o），但此时还不会关心 rot() 的具体实现。

同时，rot18.c 也会被编译，生成它的目标文件（rot18.o）。这时候，rot() 的实现已经在 rot18.o 中了。

```bash
gcc main.o rot18.o -o main.out
```
链接（linking）：在编译生成所有目标文件之后，链接器负责把这些目标文件（如 main.o 和 rot18.o）组合在一起，生成最终的可执行文件。
在链接的过程中，链接器会查找所有编译生成的目标文件（包括 rot18.o），并寻找 rot() 函数的实现。
由于 rot18.o 文件实现了 rot() 函数，链接器就会将 main.o 中的 rot() 函数调用链接到 rot18.o 中的 rot() 函数上。

另外, rot18.h 是一个头文件，它不需要单独编译或链接。头文件的作用是为源文件提供函数声明和包含必要的库。
在编译过程中，头文件会通过 #include "rot18.h" 被包含到 .c 文件中，编译器在处理 .c 文件时会自动引入相关的头文件内容。
因此，编译和链接命令并不需要专门提及 rot18.h 文件。
只需要确保在 .c 文件所在的目录中有 rot18.h 文件，编译器就会自动处理它。

## 编译步骤

help.h

```c
//This is a header file.


char* p = "Mike";
int i = 0;
```

main.c

```c
#include "help.h"

// Begin to define macro

#define GREETING "Hello world!"
#define INC(x) x++

// End

int main(){
    p = GREETING;
    INC(i);
    return 0;
}
```

```bash
## 注意不要反复执行某一步骤
rm *.i *.s *.o *.out

## 预处理器
gcc -E main.c -o main.i

## 编译器
gcc -S main.i -o main.s

## 汇编器
## 输入汇编代码
## 输出二进制目标文件
gcc -c main.s -o main.o

## 链接器
## 输入目标文件
## 输出可执行文件
gcc main.o -o main.out

./main.out
```

## 链接

静态链接适合小型程序

### 静态链接

链接器在链接时, 将库的内容直接加入到可执行程序. 程序内部已经包含了库的内容, 运行时不依赖库文件的存在.

Linux下静态库的创建和使用:

slib.c

```c
char* name(){
    return "Static Lib";
}

int add(int a, int b){
    return a + b;
}

```

main.c

```c
#include <stdio.h>

extern char* name();
extern int add(int a, int b);

int main(){
    printf("Name: %s\n", name());
    printf("Result: %d\n", add(2, 3));
}
```

创建和使用

```bash
## 编译静态库原码, 生成目标文件
gcc -c slib.c -o slib.o

## 生成静态库文件
ar -q slib.a slib.o

## 使用静态库编译
gcc main.c slib.a -o main.out
```

### 动态链接

程序运行时才会加载库, 库的内容不进入可执行程序当中.
关键的系统调用:

- dlopen
- dlsym
- dlclose

dlib.c

```c
char* name(){
    return "Dynamic Lib";
}

int add(int a, int b){
    return a + b;
}
```

main.c

```c
#include <stdio.h>
#include <dlfcn.h>

int main() {
    void* pdlib = dlopen("./dlib.so", RTLD_LAZY);

    char* (*pname)();
    int (*padd)(int, int);

    if (pdlib != NULL){
        pname = dlsym(pdlib, "name");
        padd = dlsym(pdlib, "add");

        if((pname != NULL) && (padd != NULL)){
            printf("Name: %s\n", pname());
            printf("Result: %d\n", padd(2, 3));
        }

        dlclose(pdlib);
    } else {
        printf("Cannot open lib. \n");
    }

    return 0;
}
```

```bash
## 编译动态库原码
gcc -fPIC -shared dlib.c -o dlib.so

##
gcc main.c -ldl -o main.out
```
