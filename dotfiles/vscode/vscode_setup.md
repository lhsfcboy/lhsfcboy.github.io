# Visual Studio Code 的配置与使用

## 快捷键 Shortcut

- font size zoom in : Ctrl + =
- font size zoom out: Ctil + -
- `CTRL+SHIFT+X` 快速去除当前文件中的行末空格

- [快捷键大全](https://blog.csdn.net/crper/article/details/54099319)

## 基础设置

- "editor.fontFamily": "Ubuntu Mono",

- 去除行末空格,文件末尾保留一个新行,去除文件末尾的多余连续空行,

```json
"files.trimTrailingWhitespace": true,
"files.insertFinalNewline": true,
"files.trimFinalNewlines": true,
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

- Material Icon Theme

- Indent Rainbow

## Markdown 相关

- 原生支持实时预览? Ctrl + K, V
- pass

## 文本编辑

- vscode-input-sequence

[vscode-input-sequence](https://marketplace.visualstudio.com/items?itemName=tomoki1207.vscode-input-sequence)

## python相关

- pylint

```json
    "python.linting.pylintArgs": [
        "--disable=C0301,C0111,C0103,E0611"
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
