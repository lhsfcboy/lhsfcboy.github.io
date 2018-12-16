# windows

记录一下windows的配置,免得每次重装都折腾

## path

创建一个名为C:\mybin的文件夹, 并加入path.
bin文件直接扔到这个文件夹里.

## 软件

- 7-Zip
- Amazon Kindle
- CCLeaner
- QTTab/Clover
- Dropbox
- f.lux
- FormatFactory(格式工厂)
- Google Chrome/Firefox
- Google Japanese IME
- ImgBurn/VirtualCloneDrive
- Listary
- Mozilla Thunderbird
- SumatraPDF
- QQ拼音
- PotPlayer
- Sumatra PDF
- TeamViewer
- QQ轻聊版/TIM
- 阿里旺旺
- 百度云管家
- 猎豹免费Wifi
- 鼠大侠鼠标连点器
- 网易云音乐
- 微信
- 有道词典
- 有道云笔记

### Chrome

扩展插件列表

- AdBlock
- Better History
- Enable Copy
- ChromeReloadPlus
- Chrome UA Spoofer
  - 以其他平台/浏览器来请求网页
- Grammarly for Chrome
  - 英语语法检查
- goog.gl URL Shortener
- JSON viewer
- Nimbus 截屏 录屏
- OneTab
- Quick source viewer
- User-Agent Switcher for Chrome
- Vimium
  - 完全用键盘操作网页
  - 修改键位, 使用左键盘区的字母标记链接, 来实现单手操作
- Octotree
  - Github在左侧显示目录结构树
- Stylish
  - 为任意网站自定义主题
- IE Tab
- Tampermonkey
  - 脚本扩展
- EditThisCookie
  - Cookie编辑/删除

Chrome设置

- 标签页使用梯形样式
  - chrome://flags/#top-chrome-md 将Flag值设为Normal
- 地址栏完整显示http/https的网络协议, 和www/m等前缀
  - chrome://flags/#omnibox-ui-hide-steady-state-url-scheme-and-subdomains Disabled
- 视觉上加快关闭标签页和窗口的速度
  - chrome://flags/#enable-fast-unload Enabled

### QTTab

QTTabBar官方网站: [http://qttabbar.wikidot.com/](http://qttabbar.wikidot.com/)

[QTTabBar – 从安装到能用再到秒飞Clover](https://www.mokeyjay.com/archives/1811)

QTTabBar Options

Windows Exporer / View / Options / Show QTTabs Standard Buttons

- Window
  - Capturing and Exclusion list
    - [check] Capture windows by ShellExecuteHooks(relogon required)
- Events
  - Double Click on Toolbar: Duplicate active tab
  - Click on + button on TabBar: Duplicate active tab
- Preview
  - [uncheck] Show preview

### Clover

[ZDfans的去广告版](http://www.zdfans.com/html/596.html)

### Snipaste

- 设置为开机启动
- 设置快捷键为Ctrl + Alt + A
- 关闭QQ/TIM的截图快捷键

### Ditto

剪辑板历史工具。
默认快捷键 `Ctrl+~`

### Listary

### Notepad++ (Notepad Plus Plus)

插件:

- NppExport
  - 把高亮显示的代码，粘贴到html中
- Json Viewer
- C

设置:

- 主题: `Solarized`
- Auto-Completion
  - Disable
- General
  - Tab Bar, Multi-line
- Editing
  - Multi-Editing Settings, Enable
    - Ctrl + Mouse click/selection
- Language
  - Tab Setting, Enable `Replace by space`
  
快捷键:

```text
快速复制一行	CTRL+D
快速删除一行	CTRL+L
将上下行交换	CTRL+T
快速定位到某一行	CTRL+G
快速查询	CTRL+F
进行单行注释	CTRL+K 或者是 CTRL+Q
取消单行注释	CTRL+SHIFT+K 或者是 CTRL+Q
进行多行注释	CTRL+SHIFT+Q
字体放大、缩小	点击放大、缩小按钮 或 CTRL+鼠标+滚轮的方式
选择多行	鼠标右击出现： “开始/结束” 最后一行选择 “开始/结束”
折叠所有行	ALT+0
释放所有行	ALT+SHIFT+0
折叠当前行	CTRL+ALT+F
释放当前行	CTRL+ALT+SHIFT+F
全屏模式	F11 (和浏览器一样)
合并行	Ctrl+J
```
