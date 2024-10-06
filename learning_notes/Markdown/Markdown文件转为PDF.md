# 讨论如何把Markdown文件转换为PDF格式

## Pandoc工具 与 pypandoc包

Pandoc 是一个独立的工具，而不是 Python 包。
它是一个通用的文档转换工具，可以将多种格式（如 Markdown、HTML、LaTeX、Word 等）转换成其他格式（如 PDF、DOCX、HTML 等）。

我们当然可以在 Python 中通过subprocess模块调用 Pandoc 来实现文档格式转换。
```python
import subprocess

# 运行 pandoc 命令，将 example.md 转换为 output.pdf
subprocess.run(['pandoc', 'example.md', '-o', 'output.pdf'])
```

也可以使用 pypandoc，它是一个 Python 包装器，可以在 Python 中使用 Pandoc 的功能：

```python
# pip install pypandoc
import pypandoc

# 转换 Markdown 文件为 PDF
output = pypandoc.convert_file('example.md', 'pdf', outputfile="output.pdf")
print("PDF 文件已生成:", output)
```

## Pandoc的安装 与 MiKTex

- 通过scoop安装Pandoc
- Pandoc处理PDF文件时依赖LaTex类软件，这里选择MiKTex
```bash
scoop install pandoc
scoop search tex  # 查看有哪些可以通过scoop安装的tex相关软件
scoop install MiKTex
pandoc .\LaTeX.md -o a.pdf
```
### 配置MiKTex
启用按需下载包：
- 在 MiKTeX 控制台中，点击“Settings”。
- 在“General”选项卡中，确保“Install missing packages on-the-fly”

### 执行
> 
