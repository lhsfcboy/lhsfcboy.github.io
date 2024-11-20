# CMake

CMake是一种跨平台的构建工具，主要用于管理和简化软件的编译过程，特别是对于跨平台的C/C++项目。它通过提供一种通用的配置文件（`CMakeLists.txt`），生成适合目标平台的构建文件（如Makefile、Visual Studio工程文件等），从而使项目在不同操作系统和开发环境下更容易编译和构建。

CMake的主要功能包括：

1. **跨平台支持**：CMake支持Windows、Linux、macOS等主流平台。它生成的构建文件适应平台特定的构建工具，使项目能够在多个平台上方便地编译。

2. **自动化依赖管理**：CMake会根据`CMakeLists.txt`文件中的设置自动查找和配置项目依赖的库和头文件，省去了手动管理依赖的繁琐工作。

3. **配置和生成构建文件**：CMake根据配置文件生成适合的构建文件（如Unix的Makefile、Windows的Visual Studio Solution文件、Ninja等），开发者可以选择不同的构建工具。

4. **项目配置和编译选项**：CMake允许开发者在`CMakeLists.txt`文件中配置编译选项、链接选项、优化选项等，使得项目的构建过程更加灵活和定制化。

5. **模块和包管理**：CMake支持模块化管理，能够定义、导入和使用外部库包，同时支持CMake的Find模块，可以自动查找和导入常用库的配置。

CMake常用于大型C/C++项目中，因为它可以解决跨平台编译和复杂依赖管理的问题，减少在不同开发环境中手动配置的时间，并确保项目的构建流程一致和高效。

以下是一个简单的C语言项目示例，该项目包含一个源文件和一个`CMakeLists.txt`文件，使其能够在Linux、Windows和macOS上使用GCC编译。

## 项目结构

创建一个包含以下文件和文件夹的项目结构：

```text
MyProject/
├── src/
│   └── main.c
└── CMakeLists.txt
```

## `main.c` 文件

在`src`文件夹中，编写一个简单的`main.c`程序：

```c
#include <stdio.h>

int main() {
    printf("Hello, cross-platform C program!\n");
    return 0;
}
```

## `CMakeLists.txt` 文件

在项目根目录下的`CMakeLists.txt`文件中添加以下内容：

```cmake
# 指定CMake的最低版本
cmake_minimum_required(VERSION 3.0)

# 设置项目名称和版本
project(MyProject VERSION 1.0)

# 设置C标准，确保兼容性
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED True)

# 指定源文件目录
add_executable(MyProject src/main.c)

# 适应Windows平台
if (WIN32)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -D_WIN32")
endif()

# 适应macOS平台
if (APPLE)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -D_MAC")
endif()

# 适应Linux平台
if (UNIX AND NOT APPLE)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -D_LINUX")
endif()
```

## 构建和编译项目

在不同平台上，使用以下命令编译项目：

1. **在Linux和macOS上：**

   打开终端，进入项目目录，然后运行：

   ```bash
   mkdir build
   cd build
   cmake ..
   make
   ```

2. **在Windows上（使用MSYS2或MinGW）**：

   打开命令行，进入项目目录，然后运行：

   ```bash
   mkdir build
   cd build
   cmake -G "MinGW Makefiles" ..
   mingw32-make
   ```

成功构建后，生成的可执行文件会在`build`文件夹中，运行该文件可以看到输出`Hello, cross-platform C program!`。

这个例子通过`CMakeLists.txt`的简单配置，使得项目可以在不同平台的GCC编译器下进行构建。
