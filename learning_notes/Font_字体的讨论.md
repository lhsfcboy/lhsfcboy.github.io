#  字体

## 思源等宽

https://github.com/adobe-fonts/source-han-mono/releases/
`请逐步指导我如何在Windows11下载安装支持亚洲字符的Source Han Mono`

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

目前宋体、黑体、仿宋体和楷体成为汉字印刷的主要四种字体
- 宋体
  - 白体 笔画有粗细变化，而且一般是横细竖粗，末端有装饰部分（即“字脚”或“衬线”），点、撇、捺、钩等笔画有尖端
  - 日本的明朝体（日语：明朝体／みんちょうたい
- 黑体
  - 笔画厚度均匀，平笔无节。与白体相反，和拉丁字母的无衬线体（英语：sans-serif）属于同类
  - 中文里的黑体，与日文中的ゴシック体（ゴシックたい）属于同一种风格
- 仿宋体
  - 采用宋体结构、楷书笔画的较为清秀挺拔的字体，笔画横竖粗细均匀，
  - 常用于排印副标题、诗词短文、批注、引文等，在一些读物中也用来排印正文部分。
  - 仿宋体亦是中国公文指定内文字体。
- 楷体
  - 手写字体风格 印刷最早期参照的字体

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

## 中文开源字体集 Open Source Fonts Collection for Chinese

https://drxie.github.io/OSFCC/

### 1. 思源黑体（Source Han Sans）

- 简介：由 Adobe 和 Google 合作开发，涵盖简体中文、繁体中文、日文和韩文等 East Asian 字符集。
- 下载链接：[GitHub - adobe-fonts/source-han-sans](https://github.com/adobe-fonts/source-han-sans)

### 2. 思源宋体（Source Han Serif）

- 简介：同样由 Adobe 和 Google 合作开发，提供高质量的宋体字形。
- 下载链接：[GitHub - adobe-fonts/source-han-serif](https://github.com/adobe-fonts/source-han-serif)

