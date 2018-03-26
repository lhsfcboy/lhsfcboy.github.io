# VSCode with LaTex Workshop

VSCode里的LaTex Workshop插件升级到5.0.2以后, 设置方法上貌似变了很多.
网上能搜到的设置教程都是4.0时代的, 利用toolchain这个设置来

## 准备工作

- 注意检查path是否包含TexLive
    > d:\texlive\2017\bin\win32
- pass

## 配置文件

```json
"latex-workshop.latex.toolchain": [{
    "command": "ptex2pdf",
    "args": [
        "-l",
        "-ot",
        "-kanji=utf8 -synctex=1",
        "%DOC%"
    ]
}
],
```

自动修改后

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
    }
],
"latex-workshop.latex.recipes": [
    {
        "name": "toolchain",
        "tools": [
            "Step 1: ptex2pdf"
        ]
    }
],
```