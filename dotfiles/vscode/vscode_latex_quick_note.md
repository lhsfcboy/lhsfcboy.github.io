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