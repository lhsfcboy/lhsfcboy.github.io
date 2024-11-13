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
