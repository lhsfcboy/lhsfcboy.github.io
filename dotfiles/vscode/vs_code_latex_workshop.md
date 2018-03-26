# VSCode with LaTex Workshop

VSCode里的LaTex Workshop插件升级到5.0.2以后, 设置方法上貌似变了很多.
网上能搜到的设置教程都是4.0时代的, 利用toolchain这个设置项进行配置的.

## 准备工作

- 注意检查path是否包含TexLive
  - d:\texlive\2017\bin\win32 
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

修改后

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

说明文档中进行了如下的解释:
> From toolchain to recipe? \
> If you have a custom toolchain defined in pre-4.0 versions of LaTeX Workshop, you may want to migrate the existing configuration to the new recipe system. This can be easily done with the following steps:

>- Create a tool in latex-workshop.latex.tools for each step in the original toolchain.
>- Name the tools with the name field.
>- Create a recipe in latex-workshop.latex.recipes with its tools field set as a list of the defined names in Step 2.
>- Name the recipe with the name field.

先照猫画虎一个简单例子.

```json
{
        "latex-workshop.latex.toolchain": [
        {
            "command": "latexmk",
            "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-pdf",
            "%DOC%"
            ]
        }
    ]
},
```

修改后

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

下面试着修改一个多个命令的例子.

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