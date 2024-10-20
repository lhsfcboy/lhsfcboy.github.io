#  字体

## 字体的基础知识

字体是从手写体发展而来的, 最早出现的字体是衬线字体(Serif), 主要特点是笔画有粗细变化，而且一般是横细竖粗，末端有装饰部分. 例如中文的点、撇、捺、钩等笔画有尖端.

之后出现了非衬线字体(Non-Serif), 主要是横细竖粗，没有装饰部分. 例如中文的方体字、黑体、楷体等。

等宽字体是指，数字与字母高度一致，且宽度一致。显然中文作为方块字天然就是等宽的, 但是英文字母, `A`与`I`显然宽度不一致. 等宽字体会强行设置为一致. 例如：Mono，Monaco等. 

中英文严格等宽. 如果把汉字宽度视为`1`, 那么通常字母的宽度为`0.6`左右. 对于强迫症而言, 实在痛苦, 希望能实现汉字宽度严格等于两个字母. 这样即使中英文混排也能字符天然对其.
- 这会导致英文相对`瘦`很多
- 部分编辑器可以不依赖字体达到这个效果, 例如略微拉宽汉字的字间距, 同时减小字母的字间距
- 遗憾的是`VSCode`这类基于Web的编辑器，

## 系统预装字体

某些字体是 Windows 系统自带的核心字体，如 Segoe UI，它们用于系统界面显示

Windows自带
- Courier New
  - 字体发虚, 非常不喜欢
- Consolas
  - 好!

Mac自带
- Menlo
- Monaco
- SF Mono

Adobe
-  Source Code Pro

Mozilla
- Fira Code

安卓
- Droid Sans Mono
## VSCode字体的背景知识

- https://www.bilibili.com/video/BV19r4y1W74d/

## Noto Sans Mono CJK SC
- https://github.com/notofonts/noto-cjk/blob/main/Sans/Mono/NotoSansMonoCJKsc-Regular.otf

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
  - 例如: 严格2:1等宽的“思源黑体HW”

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

## 字体封装

思源字体的封装格式是 OpenType/CFF (OTF)。该格式由 Adobe 主导开发，Windows 和 Office 软件中的 OTF 解析和渲染程序也由他们直接提供给微软。
然而，Adobe 并没有专门为 Office 软件编写 OTF 字体的嵌入功能，这导致 OTF 格式的思源字体无法嵌入。

不过，市面上常见的另一种字体格式，TrueType (TTF)，是微软（和苹果）直接开发的，该格式在 Windows 和 Office 上支持良好，支持嵌入。

