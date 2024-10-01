# 日文 LaTeX

在不同 TeX 引擎和宏包下的最简日文示例

## 常见的TeX引擎

以CloudLateX为例, 该网站提供了一下五种引擎:

- platex
- xelatex
- pdflatex
- lualatex
- uplatex

## Hello World

```tex
\begin{document}
\LaTeX で日本語を書きましょう！
\end{document}
```

注意: Windows系统在测试 pLaTeX 的时候使用 ShiftJIS 编码,其他时候使用 UTF-8 编码.
原因在于：在 Windows 系统上,pTeX 以 ShiftJIS 编码作为默认编码；在其他系统上以 UTF-8 编码作为默认编码。
当然,你也可以在 Windows 上把 pLaTeX 的测试文档以 UTF-8 编码保存,但是在编译的时候你得加上 -kanji utf8 这样的参数。

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
