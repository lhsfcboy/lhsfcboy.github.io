# LaTex 备忘录

## 工具的选择

日语的文档常用如下俩个工具:pLaTeX/upLaTeX.

配置文件示例:

```json
// settings.json
{
    // コマンドの定義
    "latex-workshop.latex.tools": [
        {
            "name": "pLaTeX command",
            "command": "platex",
            "args": [
                    "-shell-escape",
                    "-file-line-error",
                    "-halt-on-error",
                    "-interaction=nonstopmode",
                    "-synctex=1",
                    "-kanji=utf8",
                    "%DOCFILE%"
            ]
        },
        {
            "name": "upLaTeX command",
            "command": "uplatex",
            "args": [
                    "-shell-escape",
                    "-file-line-error",
                    "-halt-on-error",
                    "-interaction=nonstopmode",
                    "-synctex=1",
                    "-kanji=utf8",
                    "%DOCFILE%"
            ]
        },
        {
            "name": "plain dvipdfmx command",
            "command": "dvipdfmx",
            "args": [
                "%DOCFILE%"
            ]
        }
    ],
    // ビルドタスクの定義
    "latex-workshop.latex.recipes": [
        // recipesの最初のビルドタスクはデフォルトのビルド処理に用いられます
        {
            "name": "Build with pLaTeX",
            "tools": [
                // $ platex docname
                "pLaTeX command",
                // $ dvipdfmx docname
                "plain dvipdfmx command"
            ]
        },
        // これ以降はlatex-workshop.recipesコマンドから用いることができるビルドタスクです
        {
            "name": "Build with upLaTeX",
            "tools": [
                // $ uplatex docname
                "upLaTeX command",
                // $ dvipdfmx docname
                "plain dvipdfmx command"
            ]
        }
    ]
}
```

## bibファイルがないなら

```json
"latex-workshop.latex.tools": [
        {
            "command": "ptex2pdf",
            "args": [
                "-l",
                "-ot",
                "-kanji=utf8 -synctex=1",
                "%DOC%"
            ]
        }
],
"latex-workshop.latex.recipes": [
{
    "name": "toolchain",
    "tools": [
        "Step 1: ptex2pdf"
    ]
}],
```


## 完整的四步编译

```json
    "latex-workshop.latex.tools": [
        {
            "command": "ptex2pdf",
            "args": [
                "-l",
                "-ot",
                "-kanji=utf8 -synctex=1",
                "%DOC%"
            ],
            "name": "Step 1: ptex2pdf"
        },
        {
            "command": "pbibtex",
            "args": [
                "%DOCFILE%",
                "-kanji=utf8"
            ],
            "name": "Step 2: pbibtex"
        },
        {
            "command": "ptex2pdf",
            "args": [
                "-l",
                "-ot",
                "-kanji=utf8 -synctex=1",
                "%DOC%"
            ],
            "name": "Step 3: ptex2pdf"
        },
        {
            "command": "ptex2pdf",
            "args": [
                "-l",
                "-ot",
                "-kanji=utf8 -synctex=1",
                "%DOC%"
            ],
            "name": "Step 4: ptex2pdf"
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "toolchain",
            "tools": [
                "Step 1: ptex2pdf",
                "Step 2: pbibtex",
                "Step 3: ptex2pdf",
                "Step 4: ptex2pdf"
            ]
        }
    ],
```
