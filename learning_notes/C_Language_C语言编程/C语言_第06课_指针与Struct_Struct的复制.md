# 当复制一个结构体时

## 预备知识: C语言中的数据类型三大类

- 基本数据类型（Primitive Data Types）
  - 整数类型：如 int、short、long、char 等。
  - 浮点类型：如 float 和 double。
  - 字符类型：char（虽然它也可以用于整数表示）。
- 复合数据类型（Compound Data Types）是由基本数据类型组合或构造而成
  - 结构体（struct）：用于组合不同类型的变量。
  - 联合体（union）：与结构体类似，但成员共用内存空间。
  - 枚举（enum）：一种将整数值关联到符号常量的类型。
- 派生类型（Derived Data Type）要依赖于基本数据类型或其他复合类型
  - 数组：如 int arr[10] 是 int 类型的数组。
  - 指针：例如 int *ptr; 是指向 int 类型的指针。

## 复制一个结构体: 用等号

```c
#include <stdio.h>
#include <string.h>

struct Person
{
    char name[50];
    int age;
    float height;
};

void main()
{
    struct Person person1 = {"Alice", 30, 5.5};
    struct Person person2;

    person2 = person1;
    printf("person2 ==> Name: %s, Age: %d, Height: %.2f\n", person2.name, person2.age, person2.height);
    strcpy(person1.name, "Bob");  // 修改 name 字段为 "Bob"
    // 验证复制是否成功
    printf("person2 ==> Name: %s, Age: %d, Height: %.2f\n", person2.name, person2.age, person2.height);
}
```

在 C 语言中，当你将一个结构体变量赋值给另一个结构体变量时，编译器会对结构体的每个成员进行值拷贝。
对于基本类型（如 int、float）和数组类型（如 char name[50]），都会逐个字节地复制。
因此，person2 中的 name 数组是 person1.name 的一个独立副本。

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Person
{
    char *name;
    int age;
    float height;
};

void main()
{
    struct Person person1 = {"Alice", 30, 5.5};
    struct Person person2;

    // 直接赋值
    person2 = person1;

    // 验证复制是否成功
    printf("person2 ==> Name: %-6s, Age: %d, Height: %.2f\n", person2.name, person2.age, person2.height);

    // 修改 person1 的 name 字段改为 "Bob"
    person1.name = malloc(strlen("Bob") + 1);
    strcpy(person1.name, "Bob");
    printf("person1 ==> Name: %-6s, Age: %d, Height: %.2f\n", person1.name, person1.age, person1.height);
    printf("person2 ==> Name: %-6s, Age: %d, Height: %.2f\n", person2.name, person2.age, person2.height);
}
```
