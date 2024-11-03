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



