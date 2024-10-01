# 在VSCode中编译中文的LaTex

## 配置编译命令

LaTeX Workshop默认的编译工具是latexmk,
把其修改为中文环境最常用的xelatex

```json
"latex-workshop.latex.tools": [
    {
        // 编译工具和命令
        "name": "xelatex",
        "command": "xelatex",
        "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-pdf",
            "%DOC%"
        ]
    },
    {
        "name": "pdflatex",
        "command": "pdflatex",
        "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
        ]
    },
    {
        "name": "bibtex",
        "command": "bibtex",
        "args": [
            "%DOCFILE%"
        ]
    }
],
```

## 配置编译链

第一个recipe为默认的编译工具，

如需要使用bibtex可在编译时单击VSCode界面左下角的小勾，单击“Build LaTeX project”，
选择“xe->bib->xe->xe”，

或者直接将“xe->bib->xe->xe”的recipe放到第一位，即可以默认工具编译，但会比较慢。

大家可以根据需要自行按照格式添加自己需要的编译链。

```json
"latex-workshop.latex.recipes": [
    {
        "name": "xelatex",
        "tools": [
            "xelatex"
        ]
    },
    {
        "name": "xe->bib->xe->xe",
        "tools": [
            "xelatex",
            "bibtex",
            "xelatex",
            "xelatex"
        ]
    }
],
```

要使用pdflatex，只需在tex文档首加入以下代码：

```tex
%!TEX program = pdflatex
```

## 使用SumatraPDF预览编译好的PDF文件

```json
"latex-workshop.view.pdf.viewer": "external",

"latex-workshop.view.pdf.external.command": {
    "command": "E:/Programs/SumatraPDF/SumatraPDF.exe",
    "args": [
        "%PDF%"
    ]
},
```

## 正向搜索

添加代码进入设置区以配置正向搜索

右键文件空白处，单击“SyncTeX from cursor”即可正向搜索

```json
"latex-workshop.view.pdf.external.synctex": {
    "command": "E:/Programs/SumatraPDF/SumatraPDF.exe",
    "args": [
        "-forward-search",
        "%TEX%",
        "%LINE%",
        "%PDF%"
    ]
},
```

## 反向搜索

打开SumatraPDF，进入设置->选项, 填入Code.exe的所在位置，另外添加以下命令
`-g "%f:%l"`




