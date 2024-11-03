# 值得安装的VSCode插件

## 准备

- 官方Web市场: [Extensions for Visual Studio Code](https://marketplace.visualstudio.com/vscode)
- 查看已安装的插件列表: `code --list-extensions`

## 有待尝试

- TODO Highlight
- Bookmartks
- Path Autocomplete / Path Intellisense
- Output Colorizer
- Trailing Spaces 高亮行末空格
- Indent Rainbow
  - 使得对齐更加具有可读性
- highlight-matching-tag
  - 高亮匹配的标签 

## 语言无关

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

## CSV

- Rainbow CSV
  
## Markdown

- Markdown All in One
  + 自动调整列表的数字序号
  + 自动格式化表格
    `Alt + Shift + F`

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
