# Visual Studio Code 的配置与使用

## 快捷键 Shortcut

- [快捷键大全](https://blog.csdn.net/crper/article/details/54099319)
- <https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf>
- `文件-首选项-键盘快捷方式` or `Ctrl + K, Ctrl + S`

## 外观调整
  - font size zoom in : `Ctrl + =`
  - font size zoom out: `Ctrl + -`

## 多行编辑

- 任何光标操作，可以按`Ctrl + U`取消

- 列编辑: `Ctrl + Shift + Alt + 方向键`
- Add Coursor Above/Below: `Ctrl + Alt + 方向键`

`Ctrl + Shift + P` to setup `Multi Cursor Modifier` to `Ctrl` or `Alt`

`Ctrl` 更加直观一点
- 选择列块: `Alt + Shift + 鼠标拖动`
- 选择多个编辑位点: `Alt + 点击`
- 自由多行选择: `Alt + 鼠标拖动`

- 选中一段文字，按`Shift + Alt + I`，可以在每行末尾出现光标

- `Ctrl + D` to multi select
  - Press `Ctrl + K` and `Ctrl + D` to skip a selection
  - `Ctrl + U` to return to a previous selection.
- 光标放在一个地方，按`Ctrl + Shift + L`或者`Ctrl + F2`，可以在页面中出现这个词的不同地方都出现光标

## 文本编辑
- 移除空行
  - `Ctrl + H` Quick Replace 
  - `Alt + R` Use Regular Expressions
  - Find `^$\n`
    - `Alt + L` Find in Selection
  - `Ctrl + Shift + 1` Replace
    - `Ctrl + Alt + Enter` Replace All
- 移除行末空格    
  - `Ctrl + Shift + P` to search command `trimTrailingWhitespace`
- 转换大小写
  - `Ctrl + Shift + P` to search command `transformToUppercase` or `transformToLowercase`
  - 也可自己手动添加快捷键`Ctrl + Shift + L/U`  

## 基础设置

- 设置配置同步 `Setting Sync`

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

显示控制字符

```json
"editor.renderControlCharacters": true
```

## 值得安装的VSCode插件 准备

- 官方Web市场: [Extensions for Visual Studio Code](https://marketplace.visualstudio.com/vscode)
- 查看已安装的插件列表: `code --list-extensions`
- 只安装自己理解其用途的插件!
- 对于插件带来的快捷键覆盖等问题保持警觉!

## 有待尝试

- TODO Highlight / TODO Tree
  - https://qiita.com/taka-kawa/items/673716d77795c937d422
- Bookmartks
  - 在文档几个不同位置跳转时，这个书签插件很实用，右键菜单里直接设置/取消书签，快捷键在不同的书签位置跳转，左边还有当前书签列表，双击立马跳转
- Path Autocomplete / Path Intellisense
  - 自动完成文件名、文件路径
- Output Colorizer
- Trailing Spaces 高亮行末空格
  - 一般会配置自动删除行末空格, 这个插件已经没有意义了
- Blockman
  - 用浅显的背景色，直观的展示代码的层次结构
  - ![image](https://github.com/user-attachments/assets/2f4f9e34-65f7-4b70-96f7-6160251a3595)
- Window Colors
  - 适合多开 vscode 的同学们，看着几个 vscode 窗口经常蒙圈找不到谁是谁的, 可以为每个项目制定一个专属的颜色，多开窗口再也不会迷路
- Indent Rainbow
  - 使得对齐更加具有可读性
- highlight-matching-tag
  - 高亮匹配的标签 

## 语言无关

### AI

- TONGYI Lingma 通义灵码

### 文件图标

依据文件类型设置不同的文件图标

- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
- [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)


### Git相关

- [GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
  - 快速理解代码的修改历史, 比较不同提交之间的文本变化等
  + Current Line Blame
    当前行代码的结尾处查看最近一次commit的姓名、时间以及信息
  + Current Line Hovers
    在当前行代码的悬浮框查看详细的最近一次的commit信息
- Git History

### 代码格式化
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- 匹配括号着色 / Bracket Pair Colorizer / Bracket Pair Colorizer
  - 已经包含在其他插件功能中了, 不需要额外安装

### 文本输入相关

- [vscode-input-sequence](https://marketplace.visualstudio.com/items?itemName=tomoki1207.vscode-input-sequence)

### PDF

- vscode-pdf

## CSV / Excel

- Rainbow CSV
- Excel Viewer
  
## Markdown

- Markdown PDF
- Markdown All in One
  + 自动调整列表的数字序号
  + 自动格式化表格
    `Alt + Shift + F`
- markdownlint    

## python相关

- Python
- Python Debugger
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8)
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)
  - 禁止的规则
  - missing-module-docstring / C0114
  - C0301:Line too long
  - C0103:Constant name doesn't conform to UPPER_CASE naming style
  - C0413:Import "" should be placed at the top of the module
  - E0611:No name '' in module ''
  - W0105:String statement has no effect
  - W0611:Unused import random
  - W0404:Reimport ''
  - W1203:Use % formatting in logging functions and pass the % parameters as arguments
```json
    "python.linting.pylintArgs": [
        "--disable=C0413,  # Import related",
        "--disable=C0301,  # Line length",
        "--disable=C0111,  # Documentation",
        "--disable=C0103,  # Naming",
        "--disable=E0611,  # Import errors",
        "--disable=W0105,W0611,W0621,W0404  # Various warnings"
    ]
```

