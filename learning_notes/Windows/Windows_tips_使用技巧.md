# Windows 命令行

## 系统变量

- 逐行显示path变量
```batch
echo %path:;=&echo(%
setx PATH "%PATH%;C:\your\new\path"
echo %path:;=&echo(%
```


## 磁盘管理

- 创建指定大小的随机文件
  - fsutil file createnew E:/myfile 1048576000000
- 擦除硬盘剩余空间
  - cipher /w:E


- 命令行窗口时，用文件浏览器打开当前目录 `start .`
- Windows 11 快速打开Terminal窗口 `Alt + X, i`
- 在文件浏览器中用终端打开当前路径 `右键` 或 `Shift + 右键`
