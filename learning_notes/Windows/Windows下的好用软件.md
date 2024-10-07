## 基础软件
- Google Chrome
- 7Zip
  - https://www.7-zip.org/
- 微信WeChat
  - https://pc.weixin.qq.com/
  - 取消开机启动
- PotPlayer
  - https://potplayer.daum.net/
  - 不记录历史播放:  选项 / 播放 / 列表 / 取消勾选 记忆近期播放名单/URL地址
  - 选项 / 播放 / 鼠标指向进度条时显示缩略图
  - 选项 / 基本 / 皮肤/配色 / 视频下自动隐藏
- LibreOffice
  - 下载 LibreOffice https://zh-cn.libreoffice.org/download/libreoffice/
  - 中日韩字体 https://zh-cn.libreoffice.org/download/fonts/
  - 将下载后的字体文件解压缩，然后将文件复制到 %windir%\Fonts 文件夹
- Dropbox https://www.dropbox.com/install    
- Everything 文件搜索工具 https://www.voidtools.com/zh-cn/
- ZOOM https://zoom.us/download
- 腾讯会议
  
## 基础软件 - 输入法
现代的微软自带输入法已经比较堪用。

核心诉求:
- 能在中文模式下输入英语标点

备选方案有：
- QQ拼音 http://qq.pinyin.cn/
  - 中文状态下使用英文标点
  - 隐藏状态栏
- Google 日本語入力
- 
## 媒体播放器篇
核心诉求
- 支持格式多
- 支持变速播放

备选
- PotPlayer
- VLC
- QQ影音

## 截图、视频处理、多媒体编辑 
- Audacity
  - 音频编辑软件
- LosslessCut
  - 简单的视频片段剪切
- Carnac
  - 按下键时在屏幕一角实时显示按下的键位
- Snipaste
  - 截图工具 https://https://www.snipaste.com/www.snipaste.com/
  - 设置为开机启动
  - 设置快捷键为Ctrl + Alt + A
  - 关闭QQ/TIM的截图快捷键
- 视频压制 小丸工具箱
  - http://maruko.appinn.me
- 转码
  - HandBrake和ShanaEncoder
## 录屏
- screen To Gif
  - http://screentogif.codeplex.com
  - 强大的Gif录制工具，可自定义热键以及设置文件存放目录、设置 gif 质量、编辑 gif 文件等等，官网也有很多动画演示
- GifCam
  - http://blog.bahraniapps.com/gifcam
  - 超好用的 gif 动画录制/剪辑工具，录制后的动画可以逐帧编辑
- Screenbits
  - 这款录屏工具非常轻量，仅 675 KB，并且直接在 Windows Store 上架，相比于传统的录屏工具在安全性上更加可靠

## 不常用软件备份区
- 火绒安全软件
- qBittorrent增强版
  - 现代人已经不依靠下载软件了，以防万一做个记录
  - https://github.com/c0re100/qBittorrent-Enhanced-Edition
- TrafficMonitor
  - 任务栏中实时显示网速
- Ditto
  - 剪辑板历史工具。
  - 默认快捷键 Ctrl+~
- f.lux
  - 根据一天的地点和时间调整显示器的色温。软件的目的是减少夜间使用时的眼睛疲劳和昼夜节律的中断
  - Windows 11 系统自带了类似设置
- 鼠大侠鼠标连点器

## Windows小工具合集
- Microsoft PowerToys：用于自定义 Windows 的实用工具
  - 微软出品的功能丰富的使用工具集合。
  - 替代品的讨论：https://meta.appinn.net/t/topic/40517
-  Sysinternals Suite
  -  解压到某个目录，并将该目录设置到环境变量的PATH中。之后就能直接win+r或从cmd中运行sysinternals
  - procexp.exe: Process Explorer用来取代任务管理器，可以查看进程树形结构，快速搜索某个dll或文件被哪个进程占用了。
  - hex2dec: 目前我在windows上能找到的最方便的10/16进制互转工具。
    - 命令行输入hex2dec 10(10进制转换为16进制)，hex2dec abc(含英文参数自动转换为10进制)，hex2dec 0x123(16进制转10进制)
  - psping: 取代原有的ping工具，psping的时候可以带上端口号以探测某个端口是否开通，还有更多高级用法比如带宽测试等

## 快捷启动器
-  Wox
  -  国人开发的免费开源启动器 http://www.getwox.com
  - 类似于Mac的的 Alfred
  - https://sspai.com/post/33460

## 快捷键设置
- Windows Hotkey Explorer
  - http://hkcmdr.anymania.com/index.html
  - 热键冲突检测
- Hot Keys List
  - http://www.nirsoft.net/utils/hot_keys_list.html
  - Windows 10 support

## 磁盘空间管理
- SpaceSniffer
  - 图形化的页面直观展示各个文件夹的磁盘空间占用

## 资源浏览器增强
- Windows11开始微软默认提供了基本且简陋的标签式资源浏览器页面，勉强堪用
- Clover
  - 让你的Windows资源管理器拥有像谷歌浏览器一样好用的多标签页
  - 软件商业化了, 广告满天飞 
- QTTabbar 资源浏览器增强
  - 提供了标签式的资源浏览器扩展
  - [QTTabBar – 从安装到能用再到秒飞Clover](https://www.mokeyjay.com/archives/1811)
  - [QTTabBar 「资源管理器」该有的样子](https://sspai.com/post/52521)
  - http://qttabbar.wikidot.com/, 安装后重启系统, 打开「资源管理器」,「查看」,「选项」,「QTTabBar」
  - QTTabBarOption 
  - 关闭文件预览 
  - Preview, Uncheck Show preview ... 
  - 双击Toolbar时复制现有Tab 
  - Events, Double Clikc on Toolbar, Duplicate active tab
