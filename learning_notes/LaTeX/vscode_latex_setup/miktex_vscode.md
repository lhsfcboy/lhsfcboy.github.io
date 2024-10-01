# Miktex

[https://miktex.org/](https://miktex.org/)

## 安装

安装完成有运行"Miktex console"进行配置(选择"以管理员身份运行")。

点击"Packages"标签，然后依次安装ctex和CJK包， 以便支持中文。

## 配置VSCode

```json
// Latex workshop
"latex-workshop.latex.recipes": [{
    "name": "texify",
    "tools": [
         "texify"
    ]
}],

"latex-workshop.latex.tools": [{
    "name": "texify",
    "command": "texify",
    "args": [
        "--synctex",
        "--pdf",
        "--tex-option=\"-interaction=nonstopmode\"",
        "--tex-option=\"-file-line-error\"",
        "%DOC%.tex"
    ]
}],
```

如果需要在编译出PDF文件后，删除临时文件，则加上如下配置：

```json
"latex-workshop.latex.clean.enabled": true,
"latex-workshop.latex.clean.fileTypes": [
    "*.aux",
    "*.bbl",
    "*.blg",
    "*.idx",
    "*.ind",
    "*.lof",
    "*.lot",
    "*.out",
    "*.toc",
    "*.acn",
    "*.acr",
    "*.alg",
    "*.glg",
    "*.glo",
    "*.gls",
    "*.ist",
    "*.fls",
    "*.log",
    "*.fdb_latexmk",
    "*.synctex.gz"
]
```

## 验证

```tex
%!TEX program = xelatex
% 使用 ctexart 文类，UTF-8 编码
\documentclass[UTF8]{ctexart}
\title{测试}
\author{ddswhu}
\date{\today}

\begin{document}
\maketitle

This is the context of the article.

这就是文章的所有内容。

\end{document}
```