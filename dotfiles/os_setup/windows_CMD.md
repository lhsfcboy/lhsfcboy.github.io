# Windows 命令行

## 系统变量

- 逐行显示path变量
```batch
@echo off
for %i in ("%PATH:;=" "%") do echo %i
```

```wincmd
@echo off
for %i in ("%PATH:;=" "%") do echo %i
```
## 磁盘管理

- 创建指定大小的随机文件
  - fsutil file createnew E:/myfile 1048576000000
- 擦除硬盘剩余空间
  - cipher /w:E
