#  字体

## 程序源代码用的字体
基础要求
- 严格等宽
- 易于分辨单词中的每个字母，防止变量函数名误认
- 代码中大量出现的特殊符号（如 # % $ * \）与字母混杂在一起时依然美观协调

扩展要求
- 支持中文与日文
- 汉字宽度等于两个字母

```
Ubuntu Mono (中英文严格等宽)
SimSun(推荐)
NSimSun
Microsoft YaHei
KaiTi
FangSong
YouYuan

Monaco (only problem: no bold/italic variant)
Menlo
Consolas (only if using Windows)
Bitstream Vera Sans Mono / DejaVu Sans Mono (only if using Linux)
```
## Windows下查看当前系统安装的字体
- CMD查看当前系统的字体: `dir  %windir%\Fonts`
- PoswerShell查看：
```PowerShell
[System.Reflection.Assembly]::LoadWithPartialName("System.Drawing") | Out-Null
$fonts = New-Object System.Drawing.Text.InstalledFontCollection
$fonts.Families | ForEach-Object { $_.Name }
```


## 常见的中文字体名称
在筛选字体时，可以参考以下常见的中文字体名称：

- SimSun（宋体）
- SimHei（黑体）
- KaiTi（楷体）
- FangSong（仿宋）
- Microsoft YaHei（微软雅黑）
- Microsoft JhengHei（微软正黑体）
- DengXian（等线）
- LiSu（隶书）
- YouYuan（幼圆）
- STXihei（华文细黑）
- STKaiti（华文楷体）
- STSong（华文宋体）
- STFangSong（华文仿宋）

## 开源且可以商用的字体

### 1. 思源黑体（Source Han Sans）

- 简介：由 Adobe 和 Google 合作开发，涵盖简体中文、繁体中文、日文和韩文等 East Asian 字符集。
- 下载链接：[GitHub - adobe-fonts/source-han-sans](https://github.com/adobe-fonts/source-han-sans)

### 2. 思源宋体（Source Han Serif）

- 简介：同样由 Adobe 和 Google 合作开发，提供高质量的宋体字形。
- 下载链接：[GitHub - adobe-fonts/source-han-serif](https://github.com/adobe-fonts/source-han-serif)

### 3. Noto Sans CJK

- 简介：Google 的 Noto 字体家族的一部分，旨在消除“豆腐块”（无法显示的字符），支持多种语言。
- 下载链接：[Google Noto Fonts](https://www.google.com/get/noto/#sans-hans)

### 4. 霞鹜文楷

- 简介：由国内开发者 LXGW 基于思源宋体修改，优化了字形和标点，适合阅读和显示。
- 下载链接：[GitHub - lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai)

### 5. 霞鹜新晰黑

- 简介：同样由 LXGW 开发，专为屏幕显示优化的黑体字体。
- 下载链接：[GitHub - lxgw/LxgwClearGothic](https://github.com/lxgw/LxgwClearGothic)

### 6. 更纱黑体（Sarasa Gothic）

- 简介：基于思源黑体和 Iosevka 混合的等宽字体，适合编程和终端使用。
- 下载链接：[GitHub - be5invis/Sarasa-Gothic](https://github.com/be5invis/Sarasa-Gothic)
