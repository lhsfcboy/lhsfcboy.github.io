# Visual Studio Code 的配置与使用

## 快捷键 Shortcut

- font size zoom in : Ctrl + =
- font size zoom out: Ctil + -
- `CTRL+SHIFT+X` 快速去除当前文件中的行末空格

## 基础设置

- "editor.fontFamily": "Ubuntu Mono",

- 去除行末空格

```json
"files.trimTrailingWhitespace": true,
"files.insertFinalNewline": true,
"files.trimFinalNewlines": true,
```

## 外观设置

Sublime Material Theme - Dark

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
