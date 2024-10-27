# Java 学习准备

## 学习资源

- 廖雪峰的Java教程
  - https://liaoxuefeng.com/books/java/introduction/index.html

## 版本历史

Java 首先是一个规范(标准),具体包括:

- Java语言规范(JLS - Java Language Specification)
- Java虚拟机规范(JVMS - Java Virtual Machine Specification)
- Java API规范

各个不同厂家由不同实现, 最主要的两个实现:

### OpenJDK

[OepnJDK](https://openjdk.org/projects/jdk/)是社区开发的Java实现。
Oracle 是 OpenJDK 的主要贡献者之一, Oracle有官方的OpenJDK发布页面[Oracle OpenJDK Releases](https://jdk.java.net/),
或者[Java Downloads](https://www.oracle.com/java/technologies/downloads/)

OpenJDK是大多数其他JDK发行版的基础

### Oracle JDK

由Oracle公司开发维护, 基于OpenJDK构建, 包含一些闭源组件和商业特性
从Java 11开始用于商业用途 需要商业许可证

### Other

其他常见的JDK发行版:

- AdoptOpenJDK(现在的Adoptium)
- Amazon Corretto
- Azul Zulu
- Red Hat OpenJDK

这些都是基于OpenJDK的实现,但可能会添加一些特定的优化和工具。它们都遵循相同的Java规范,所以用这些JDK编写的Java代码都是兼容的。

## 版本生命周期

Java SE(Java平台标准版)的版本更新计划由Oracle主导, 定期发布新版本，其中某些版本被指定为LTS版本, 这为整个Java生态系统提供了一个参考基准

不同的JDK提供商可以自行决定对哪些版本提供长期支持, 支持时间和支持方式也可能不同.

对OpenJDK而言, 可以说没有LTS这个概念, 具体的商业支持由各个厂家决定.

近期的主要版本和Oracle JDK的商业支持时间[Oracle Java SE Support Roadmap](https://www.oracle.com/cn/java/technologies/java-se-support-roadmap.html)

- 目前还在生命周期内的LTS版本
- 最新的GA版本
- 下一个计划发布的LTS版本 

| Release      | GA Date | 内部版本号 | Extended Support |
|--------------|---------|------------|------------------|
| 8 (LTS)      | 2014    | 1.8        | 2030             |
| 11 (LTS)     | 2018    | 11         | 2032             |
| 17 (LTS)     | 2021    | 17         | 2029             |
| 21 (LTS)     | 2023    | 21         | 2031             |
| 23 (non-LTS) | 2024    | 23         | Not Available    |
| 25 (LTS)     | 2025    | 25         | 2033             |

### 有关版本号

- 早期版本命名：在 Java 的早期版本（如 1.0、1.1、1.2）中，版本号采用的是 1.x 的形式。
- 品牌命名的变化：从 Java 5 到 Java 8，Sun （后被 Oracle 收购）将版本号简化为整数形式，例如：
- 统一版本号：从 Java 9 开始，内部版本号和产品名称统一，直接使用整数版本号，如 Java 9、Java 10。

这本来是一个非常没有用的过时知识, 但是因为Java 8的广泛使用, 初学者可能会疑惑java命令行的version信息输出.

运行`java -version`命令时，显示的版本号通常是内部版本号，例如 1.8.0_371。

```shell
# java -version of Java 8
java version "1.8.0_371"
Java(TM) SE Runtime Environment (build 1.8.0_371-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.371-b11, mixed mode)
================================================================================
# java -version of Java 23
java version "23.0.1" 2024-10-15
Java(TM) SE Runtime Environment (build 23.0.1+11-39)
Java HotSpot(TM) 64-Bit Server VM (build 23.0.1+11-39, mixed mode, sharing)
```

## 参考资料

- [OpenJDKと各種JDKディストリビューションの情報源まとめ](https://qiita.com/yamadamn/items/2dd26a014791b9557199)
