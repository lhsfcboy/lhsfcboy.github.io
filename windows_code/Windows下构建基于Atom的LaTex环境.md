本文记录了Windows下的LaTex环境配置.

## Ref
https://texwiki.texjp.org/?Atom


Atom で LaTeX on Windows （+ 最近のビルド環境）
http://ichiro-maruta.blogspot.jp/2016/01/atom-latex-on-windows.html


## 下载并安装Tex Live
http://tug.org/texlive/acquire-netinstall.html

## Atom上的相关插件
- pdf-view
- latextools
    - 这个插件没法选择uplatex, 太坑了,
- latexer
- language-latex

LaTeX 命令的自动补全

这个 Package 仅会在所有扩展名为 .tex.latex.text 的文件中被启用

- latex
    - TeX Path
    - SumatraPDF Path
    -


- atom-latex
在 Atom 中实现 LaTeX 的编译



## 使用
新建文件，后缀名为.tex，编码为UTF-8
Ctrl + Alt + B 生成PDF文档。
在atom里右键PDF文档，点Split Right。每当重新生成文档，会更新预览。

## 小提示

- Ctrl + \ 隐藏/展示左边的目录树

## Quick Check
- latex (compile latex)
- language-lax (syntax highlighting)
- latexer (autocmpletion)
- latextools (more support)
- minimap (preview of code)
- open-recent (open recent files)
- pdf-view (builtin pdf viewer)
- file-icons
- autocomplete-paths
- spell-check

###
Package Settings:

- latex:
Tex Path: C:\texlive\2015\bin\win32
Builder: latexmk
Always Open Result in Atom: Yes
(Other settings: keep default)
- spell-check:
Grammars: text.tex
- pdf-view:
Fit to width on open: Yes
###
Important shortcuts:

Alt+Shift+S: search for latex snippet
Alt+Ctrl+B: compile
Alt+Ctrl+S: sync
Alt+Ctrl+C: clear

###
- TeXWorksで日本語が表示されない
http://dokoka.org/wiki.cgi?page=TeXWorks%A4%C7%C6%FC%CB%DC%B8%EC%A4%AC%C9%BD%BC%A8%A4%B5%A4%EC%A4%CA%A4%A4%A1%A2%A4%C8%A4%A4%A4%A6%BB%FE%A4%CF


- LaTeX Error: This file needs format `pLaTeX2e' but this is `LaTeX2e
 jsarticle などの (u)pLaTeX 専用のクラスファイルで作成したソースを (u)platex 以外で処理しようとすると出るエラーです． 大抵の場合，お使いの統合環境のデフォルト設定で pdflatex（日本語非対応）を使うようになっていることが原因です． (u)platex を使う設定を追加する必要があります．


## Hello Latex

\documentclass[UTF8]{article}
\author {Author}
\title {Title}
\usepackage{ctex}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
\maketitle
\section{First section} test1.
    \subsection{First subsection} test2.
        \subsubsection{First double subsection}
            \paragraph{Fist paragraph} test3.
                \subparagraph{First subparagraph} test4.
    \subsection{Second subsection}
        \paragraph{段落} 中文测试。
\\
Hello World! \\ % This is comment
Hello \LaTeX ! \\

$\lim\limits_{n \rightarrow +\infty} P\lbrace\frac{\sum\limits_{i=1}{n}Xi - n\cdot EX}{ \sqrt{n \cdot DX} }  \leqslant x\rbrace = \Phi(x)$ \\

$P\lbrace a<X<b \rbrace \approx \Phi(\frac{b - n\cdot EX}{\sqrt {n\cdot DX}}) - \Phi(\frac{a - n\cdot EX}{\sqrt{n\cdot DX} })$ \\

$F(x,y) = F_{X}(x)F_{Y}(y)$
\end{document}
