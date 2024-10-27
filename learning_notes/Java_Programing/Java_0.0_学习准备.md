# Java 学习准备

## 学习资源

- 廖雪峰的Java教程
  - https://liaoxuefeng.com/books/java/introduction/index.html

## 版本历史

- 目前还在生命周期内的LTS版本
- 最新的GA版本
- 下一个计划发布的LTS版本
- [Oracle Java SE Support Roadmap](https://www.oracle.com/cn/java/technologies/java-se-support-roadmap.html)

| Release      | GA Date | 内部版本号 | Extended Support |
|--------------|---------|------------|------------------|
| 8 (LTS)      | 2014    | 1..8       | 2030             |
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
# java -version of Java 18
java version "1.8.0_371"
Java(TM) SE Runtime Environment (build 1.8.0_371-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.371-b11, mixed mode)
================================================================================
# java -version of Java 23
java version "23.0.1" 2024-10-15
Java(TM) SE Runtime Environment (build 23.0.1+11-39)
Java HotSpot(TM) 64-Bit Server VM (build 23.0.1+11-39, mixed mode, sharing)
```

## OepnJDK vs Oracle JDK vs Other

[OepnJDK](https://openjdk.org/projects/jdk/)是社区开发的Java实现。
Oracle 是 OpenJDK 的主要贡献者之一, Oracle有官方的OpenJDK发布页面[Oracle OpenJDK Releases](https://jdk.java.net/),
或者[Java Downloads](https://www.oracle.com/java/technologies/downloads/)
