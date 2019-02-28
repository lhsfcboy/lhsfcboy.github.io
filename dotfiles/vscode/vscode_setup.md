# Visual Studio Code 的配置与使用

## 快捷键 Shortcut

- font size zoom in : `Ctrl + =`
- font size zoom out: `Ctrl + -`
- !!!NOT WORKING!!! `CTRL+SHIFT+X` 快速去除当前文件中的行末空格

- [快捷键大全](https://blog.csdn.net/crper/article/details/54099319)
- 列编辑: `Ctrl + Shift + Alt + 方向键`

- `Ctrl + D` to multi select
  - Press `Ctrl + K` and `Ctrl + D` to skip a selection
  - `Ctrl + U` to return to a previous selection.

## 基础设置

- `"editor.fontFamily": "Ubuntu Mono",`

- 去除行末空格,文件末尾保留一个新行,去除文件末尾的多余连续空行,

```json
"files.trimTrailingWhitespace": true,
"files.insertFinalNewline": true,
"files.trimFinalNewlines": true,
```

- 中文乱码

```json
"files.autoGuessEncoding": true,
```

## 外观设置

- Sublime Material Theme - Dark

注释所用的字体格式为斜体,且是墨绿色, 很难在黑色背景中看清.
修改配置文件: `/c/Users/Mike/.vscode/extensions/jprestidge.theme-material-theme-1.0.1/themes/Material-Theme.tmTheme`.

删除掉控制`comments`格式的如下两行, 并将颜色改为 `<string>#37EC27</string>` (亮绿色.

```xml
<key>fontStyle</key>
<string>italic</string>
```

- Dracula Theme
  深色主题

- Material Icon Theme
  依据文件类型设置不同的文件图标

- Indent Rainbow
  使得对齐更加具有可读性

- Bracket Pair Colorizer
  为代码中的匹配的括号自动着色，以不同的颜色进行区分

- highlight-matching-tag
  高亮匹配的标签

## Markdown 相关

- 原生支持实时预览? `Ctrl + K, V`

- Markdown All in One
  + 自动调整列表的数字序号
  + 自动格式化表格
    `Alt + Shift + F`

## 文本编辑

- vscode-input-sequence

[vscode-input-sequence](https://marketplace.visualstudio.com/items?itemName=tomoki1207.vscode-input-sequence)

## Git相关

- GitLens
  快速理解代码的修改历史
  + Current Line Blame
    当前行代码的结尾处查看最近一次commit的姓名、时间以及信息
  + Current Line Hovers
    在当前行代码的悬浮框查看详细的最近一次的commit信息

## python相关

- pylint

```json
    "python.linting.pylintArgs": [
        "--disable=C0301,C0111,C0103,E0611"
    ],

    "python.linting.pylintArgs": [
        "--disable=C0413,C0301,C0111,C0103,E0611,W0105,W0611,W0621,W0404"
    ],
```

- 禁止的规则
  - C0111:Missing module docstring
  - C0301:Line too long
  - C0103:Constant name doesn't conform to UPPER_CASE naming style
  - C0413:Import "" should be placed at the top of the module
  - E0611:No name '' in module ''
  - W0105:String statement has no effect
  - W0611:Unused import random
  - W0404:Reimport ''
  - W1203:Use % formatting in logging functions and pass the % parameters as arguments
