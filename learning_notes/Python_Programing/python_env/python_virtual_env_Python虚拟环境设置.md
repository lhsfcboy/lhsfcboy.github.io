# linux下配置jupyter环境

## 所谓全局环境

## 安装

venv --- 创建虚拟环境

https://docs.python.org/zh-cn/3.12/library/venv.html

## Windows下的一种安装方式

- 无特殊需求的话，不再安装任何Python2版本。
- 安装所需要的版本到独立目录，例如
  - Python3.12 -> "C:\Python312\python.exe"
  - Python3.11 -> "C:\Python311\python.exe"
  - Python3.10 -> "C:\Python310\python.exe"
- 构建单独的venv环境
  ```cmd
  "C:\Python312\python.exe" -m venv D:\venv312-base
  "C:\Python312\python.exe" -m venv D:\venv312-project-A
  "C:\Python312\python.exe" -m venv D:\venv312-project-B
  ```
- 激活并检查
  ```cmd
  D:\venv312-base\Scripts\activate.bat
  python --version
  pip install numpy
  ```
