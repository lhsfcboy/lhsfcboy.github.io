
# VIM 通用指南

这份指南涵盖了一些常用的VIM操作，包括移动屏幕、移动光标以及多文件操作。对于初学者和需要快速参考的用户，这将是一个便捷的参考。

## 代码格式化
basic indent code 
```
gg=G
```
gg goes to the top of the file,= is a command to fix the indentation and G tells it to perform the operation to the end of the file

## 3. 多文件操作 总述

在VIM中，你可以通过以下命令在当前会话中打开一个新的文件：

```vim
:open file2.txt
:e file2.txt
```


## 4. 多文件操作 启动篇

VIM 支持分屏操作。你可以通过以下方式在打开多个文件时选择分屏显示的方式：

- **垂直分屏**：使用大写的 `O` 参数

```bash
vim -On file1 file2 ...
```

- **水平分屏**：使用小写的 `o` 参数

```bash
vim -on file1 file2 ...
```


## 5. 多文件操作 操作篇

在操作多个文件时，VIM 提供了一些实用命令来切换和操作缓冲区：

| 命令             | 效果                          |
|------------------|-------------------------------|
| `:ls`            | 列出所有缓冲区                |
| `:buffers`       | 列出所有缓冲区（与 `:ls` 等效）|
| `:bn[ext]`       | 切换到下一个缓冲区             |
| `:bp[revious]`   | 切换到上一个缓冲区             |
| `:b {number}`    | 跳转到指定编号的缓冲区         |


通过这些命令，您可以在多个文件之间快速切换，提高工作效率。如果您正在处理多个文件，使用VIM的缓冲区管理功能将非常有用。
