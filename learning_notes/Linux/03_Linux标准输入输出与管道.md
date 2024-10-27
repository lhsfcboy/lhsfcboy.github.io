# Linux标准输入输出与管道

## 标准输入输出通道

Linux为进程提供三个I/O通道：

- 标准输入 (0): 键盘
- 标准输出 (1): 终端窗口
- 标准错误 (2): 终端窗口

查看标准I/O设备链接：

```bash
ls -l /dev/std*
lrwxrwxrwx 1 root root 4 Sep  4 11:14 /dev/stderr -> fd/2
lrwxrwxrwx 1 root root 4 Sep  4 11:14 /dev/stdin -> fd/0
lrwxrwxrwx 1 root root 4 Sep  4 11:14 /dev/stdout -> fd/1
```

## 输入输出重定向

### 基本重定向操作

- `cal > text1.txt`     # 覆盖写入
- `cal >> text1.txt`    # 追加写入

> **注意**：1或2表示标准输出时，与其后的大于号之间没有空格

### 标准输出和错误输出重定向

- `ls 1> text1.txt`     # 仅重定向标准输出
- `ls > text1.txt`      # 默认重定向标准输出
- `ls 2> text1.txt`     # 仅重定向标准错误输出
- `[command] 2> errs.txt 1> output.txt`  # 分别重定向错误和正常输出
- `[command] > text1.txt 2>&1`           # 标准输出和错误输出都重定向到同一文件
- `[command] &> text2.txt`               # &表示所有输出都重定向到text2.txt
- `>/dev/null 2>&1`                      # 丢弃所有输出

## 管道

管道用于将一个命令的输出作为另一个命令的输入。

常用管道命令示例：

- `ls -Rl /etc | more`               # 分页显示目录内容
- `cat /etc/passwd | wc`             # 统计文件行数
- `cat /etc/passwd | grep username`  # 查找用户信息
- `dmesg | grep eth0`                # 显示网卡设备信息
- `ls -l | grep "^d"`                # 只列出目录
- `ps -ef | grep tomcat`             # 查看tomcat进程信息

## 详细说明

### 输出重定向

输出重定向将命令的输出写入到文件而不是显示在屏幕上。

基本语法：

```bash
命令 > 文件名     # 覆盖写入
命令 >> 文件名    # 追加写入
```

示例：

```bash
ls > directory.out          # 将ls命令输出保存到文件
ls /usr/tmp 2> err.file    # 将错误信息重定向到文件
ls /usr/tmp &> output.file # 同时重定向标准输出和错误输出
```

### 输入重定向

输入重定向允许命令从文件而不是键盘读取输入。

基本语法：

```bash
命令 < 文件名
```

示例：

```bash
wc < /etc/passwd    # 统计文件的行数、词数和字符数
```

输入重定向主要用于：

- 命令不接受文件名作为输入参数时
- 需要的输入内容存在于文件中时
