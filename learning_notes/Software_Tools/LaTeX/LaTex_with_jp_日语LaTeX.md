# 日文 LaTeX

## 最快方案: 使用网络服务 Cloud Latex

- https://cloudlatex.io/ja

## 搭建本地环境

- https://zhuanlan.zhihu.com/p/19910110
- https://zhuanlan.zhihu.com/p/19912674

## 常见的TeX引擎

以CloudLateX为例, 该网站提供了一下五种引擎:

- platex
- xelatex
- pdflatex
- lualatex
- uplatex

日语的文档常用如下俩个工具:pLaTeX/upLaTeX.

## Hello World

```tex
\begin{document}
\LaTeX で日本語を書きましょう！
\end{document}
```

注意: Windows系统在测试 pLaTeX 的时候使用 ShiftJIS 编码,其他时候使用 UTF-8 编码.
原因在于：在 Windows 系统上,pTeX 以 ShiftJIS 编码作为默认编码；在其他系统上以 UTF-8 编码作为默认编码。
当然,你也可以在 Windows 上把 pLaTeX 的测试文档以 UTF-8 编码保存,但是在编译的时候你得加上 -kanji utf8 这样的参数。

## 中文日文混排

使用支持中日文字的统一字体，可以避免字符缺失的问题。

解决方案：
- 下载 思源宋体 或 思源黑体。
- 安装字体到系统中。
- 在命令中指定字体
  - 例如 ` pandoc input.md -o output.pdf --pdf-engine=xelatex -V CJKmainfont="Source Han Serif SC" `

## pLaTeX 以及 upLaTeX

```tex
\documentclass{article}
\begin{document}
\LaTeX で日本語を書きましょう！
\end{document}
```

以正确的编码将其保存为 hello-ptex.tex，然后运行 platex/uplatex

```bash
platex hello-ptex.tex
dvipdfmx hello-ptex.dvi
```

## XeLaTeX

```tex
% 使用xeCJK宏包,并选择一个日文字体
\documentclass{article}
\usepackage{xeCJK}
\setCJKmainfont{ipaexm.ttf}
\begin{document}
\LaTeX で日本語を書きましょう！
\end{document}
```

运行xelatex, 直接就能得到 PDF 文档.

> xelatex hello-xetex.tex

```tex
% 使用ZXjatype宏包,并选择一个日文字体
\documentclass{article}
\usepackage{zxjatype}
\setjamainfont{ipaexm.ttf}
\begin{document}
\LaTeX で日本語を書きましょう！
\end{document}
```

## pdfLaTeX

```tex
\documentclass{article}
\usepackage{CJKutf8}
\usepackage{CJKspace}
\begin{document}
\begin{CJK*}{UTF8}{min}
\LaTeX{} で日本語を書きましょう！
\end{CJK*}
\end{document}
```

> pdflatex hello-cjk.tex

## LuaLaTeX

```tex
\documentclass{article}
\usepackage{luatexja}
\begin{document}
\LaTeX で日本語を書きましょう！
\end{document}
```
