# Jupyter Notebook 速查表

## 快捷键

Comment out lines: CMD + /

## 基础设置

- 创建配置文件

```bash
jupyter notebook --generate-config.
#This writes a file to C:\Users\username\.jupyter\jupyter_notebook_config.py
```

## pass

- 在指定目录下启动Jupyter Notebook

如果配置文件中没有滴定启动目录的话, Jupyter 会从当前目录启动.

Windows下, 在该目录下, Alt + D定位到地址栏, `cmd` 命令启动命令行, `jupyter notebook` 在该目录下启动

- 修改默认的启动目录
  - Windows 7
    - 修改配置文件 `jupyter_notebook_config.py`

    ```python
    c.NotebookApp.notebook_dir = u'D:\\GitHubWorkSpace'
    ```