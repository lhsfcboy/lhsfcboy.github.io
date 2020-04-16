# windows7

记录一下windows的配置,免得每次重装都折腾

## Lenovo ThinkPad X220i

- Remove the Windows Recovery Partition

```cmd
diskpart
list disk
select disk n
list partition
select partition n
delete partition override
```
Expanding a Partition to Use the Unallocated Space

## path

创建一个名为C:\mybin的文件夹, 并加入path.
bin文件直接扔到这个文件夹里.

## OS

- Windows Update
- 硬件驱动
- 卸载掉无用的预装软件

## 软件 必备类

- 7-Zip
- Google Chrome
- Google Japanese IME
- QQ拼音
- PotPlayer
- 有道云笔记
- OneNote

## 软件 常用类

- Dropbox
- 微信
- QQ轻聊版/TIM
- TeamViewer
- Amazon Kindle
- CCLeaner
- QTTab/Clover
- f.lux
- FormatFactory(格式工厂)
- Firefox
- ImgBurn/VirtualCloneDrive
- Listary
- Sumatra PDF
- 阿里旺旺
- 百度云管家
- 猎豹免费Wifi
- 鼠大侠鼠标连点器
- 网易云音乐
- 有道词典

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
