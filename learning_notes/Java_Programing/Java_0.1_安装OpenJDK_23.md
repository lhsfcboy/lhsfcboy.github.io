# 准备安装JDK环境

## 下载msi格式的安装包

- [Windows x64 MSI Installer](https://www.oracle.com/java/technologies/downloads/)
- 默认路径一般是`C:\Program Files\Java\jdk-版本号`

## 环境变量

- 系统变量 `JAVA_HOME`
  - 变量值设置为 Java 的安装路径，例如 C:\Program Files\Java\jdk-版本号
- 系统变量 `Path`
  - 添加 Java 的二进制文件路径`%JAVA_HOME%\bin`

验证

- CMD

```cmd
echo %JAVA_HOME%
echo %Path:;=&echo.%
where java
```

- PowerShell

```powershell
$Env:Path -split ';'
```

## javapath

较新版本的JDK安装后, 可能会看到系统的 Path 环境变量中包含以下路径

```powershell
> dir "C:\Program Files\Common Files\Oracle\Java\javapath"
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2024/9/30      8:13         715864 java.exe
-a----         2024/9/30      8:13         715864 javac.exe
-a----         2024/9/30      8:13         715872 javaw.exe
-a----         2024/9/30      8:13         715864 jshell.exe

> dir "C:\Program Files\Common Files\Oracle\Java"
 Volume in drive C is Windows
 Volume Serial Number is 4CE0-0E01

 Directory of C:\Program Files\Common Files\Oracle\Java

2024/10/27  10:23    <DIR>          .
2024/10/27  10:23    <DIR>          ..
2024/10/27  10:23    <JUNCTION>     javapath [C:\Program Files\Common Files\Oracle\Java\javapath_target_302825171]
2024/10/27  10:23    <DIR>          javapath_target_302825171
               0 File(s)              0 bytes
```

这是由安装程序自动设置. 使用这个路径的目的是方便 Java 更新。当安装了新的 Java 版本时，这些快捷方式会自动更新，不需要每次更新时手动修改 Path.


```powershell
> Get-Item "C:\Program Files\Common Files\Oracle\Java\javapath\java.exe" | Select-Object Name,Target

Name     Target
----     ------
java.exe {C:\Program Files\Common Files\Oracle\Java\javapath_target_302825171\java.exe}
```

## 验证 Java 版本是否正确

```shell
java -version
javac -version
```
