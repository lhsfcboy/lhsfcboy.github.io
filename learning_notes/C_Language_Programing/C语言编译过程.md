# pass

## gcc

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
