# 讨论如何通过命令行环境在本体把Markdown文件转换为PDF格式

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
- (?)安装中文需要的ctex包

### 执行
使用支持UTF-8的xelatex来编译
> pandoc .\LaTeX.md -o a.pdf --pdf-engine=xelatex

默认的字体可能是英文字体，会导致非英文文档报错。
> [WARNING] Missing character: There is no 标 (U+6807) in font [lmroman12-bold]:mapping=tex-text;!

这里先用微软雅黑对付一下。
> pandoc input.md -o output.pdf --pdf-engine=xelatex -V mainfont="Microsoft YaHei"

默认的页边距设置有点太夸张了，设置使用纸面的80%区域显示
> pandoc input.md -o output.pdf --pdf-engine=xelatex -V mainfont="Microsoft YaHei"  -V geometry=scale=0.8

### 碰到的问题

中文的等宽字体
- 原始文本的代码部分默认是用等宽字体显示的，而默认的等宽字体是英文字体。
- 如果其中包含中文，比如注释部分。会导致默认调用的等宽字体无法显示。有如下报错：
> [WARNING] Missing character: There is no 使 (U+4F7F) in font [lmmono10-italic]:!
- 安装中文等宽字体，例如Source Han Mono, 并指定其为编译时使用的中文字体
> pandoc input.md -o output.pdf -f markdown-raw_tex --pdf-engine=xelatex -V mainfont="Microsoft YaHei" -V monofont="Source Han Mono"
