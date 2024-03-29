# Windows 10 操作系统的配置
## 操作系统基础设置
### 更改计算机名称
计算机名称会被用于蓝牙设备等.
- Settings / System / About /  Device specifications / Rename this PC
- Restart to apply
### 关闭活动历史时间线功能
Win+Tab会显示近期打开的文档等
- Setting / Privacy / Activity history, Disable and Clear
### 任务栏
- Personalization / Taskbar
- Use small taksbar buttons
- Cobine task bar buttons: When taskbar is full
- Show taskbar on all displays: off 双屏幕时的任务栏显示 个性化/任务栏
### 桌面
- Windows 设置 / 个性化 / 主题 / 桌面图标设置 / 取消将回收站固定到桌面
### 总是在任务栏显示language bar (以避免其自动调整size)
- Settings / Time & language / Language / Keyboard / Advanced keyboard settings
- Use the desktop language bar when it's available.
### Uninstall Pre-Installed App
- McAfee
- MS Office
- MS OneDrive
### 删除自带的Metro应用
PowerShell, run as Administrator

```PowerShell
# Uninstall 3D Builder:
Get-AppxPackage *3dbuilder* | Remove-AppxPackage

# Uninstall Alarms and Clock:
Get-AppxPackage *windowsalarms* | Remove-AppxPackage

# Uninstall Calculator:
Get-AppxPackage *windowscalculator* | Remove-AppxPackage

# Uninstall Calendar and Mail:
Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage

# Uninstall Get Office:
Get-AppxPackage *officehub* | Remove-AppxPackage

# Uninstall Get Skype:
Get-AppxPackage *skypeapp* | Remove-AppxPackage

# Uninstall Get Started:
Get-AppxPackage *getstarted* | Remove-AppxPackage

# Uninstall Groove Music:
Get-AppxPackage *zunemusic* | Remove-AppxPackage

# Uninstall Maps:
Get-AppxPackage *windowsmaps* | Remove-AppxPackage

# Uninstall Microsoft Solitaire Collection:
Get-AppxPackage *solitairecollection* | Remove-AppxPackage

# Uninstall Money:
Get-AppxPackage *bingfinance* | Remove-AppxPackage

# Uninstall Movies & TV:
Get-AppxPackage *zunevideo* | Remove-AppxPackage

# Uninstall News:
Get-AppxPackage *bingnews* | Remove-AppxPackage

# Uninstall Phone Companion:
Get-AppxPackage *windowsphone* | Remove-AppxPackage

# Uninstall Sports:
Get-AppxPackage *bingsports* | Remove-AppxPackage

# Uninstall Weather:
Get-AppxPackage *bingweather* | Remove-AppxPackage

# Uninstall Xbox:
Get-AppxPackage *xboxapp* | Remove-AppxPackage

# Uninstall Voice Recorder:
Get-AppxPackage *soundrecorder* | Remove-AppxPackage

# Uninstall Camera:
Get-AppxPackage *windowscamera* | Remove-AppxPackage

# 以下三个APP有待确认具体用途

# Uninstall Store:
Get-AppxPackage *windowsstore* | Remove-AppxPackage
# Uninstall Photos:
Get-AppxPackage *photos* | Remove-AppxPackage
# Uninstall OneNote:
Get-AppxPackage *onenote* | Remove-AppxPackage
```

### 关闭休眠(可选)
管理员CMD: `powercfg -h off`
### 关闭系统备份还原
控制面板>系统与还原>系统，左侧“系统保护”>设置，里面选择第三项“关闭系统还原”
### 清理Windows 资源管理器(Explorer)侧边栏 与 这台电脑(This PC)中得快捷方式
有桌面, 文档, 下载, 音乐, 图片, 视频, 3D 对象的快捷方式, 需要通过'以管理员身份'运行regedit进行清理. 清理操作无需重启, 即刻生效.
- 3D对象文件夹的清理
  - 找到：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\
  - 删除{0DB7E03F-FC29-4DC6-9020-FF41B59E513A} 
  - 打开：HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace
  - 删除{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}
- 3D Objects 以外
  - 定位到HKEY_LOCAL_MACHINE＼SOFTWARE＼Microsoft＼Windows＼CurrentVersion＼Explorer＼FolderDescriptions 
  - 可以通过该项右侧窗口中Name的数据值来判断是否是我们需要的项，这里“图片”对应的是英文名Local Pictures
  - 进入它的子项“PropertyBag”，双击右侧窗口中的“ThisPCPolicy”，将其数据数值由Show改为Hide
- FolderDescriptions
  - 图片文件夹：{0ddd015d-b06c-45d5-8c4c-f59713854639}＼PropertyBag
  - 视频文件夹：{35286a68-3c57-41a1-bbb1-0eae73d76c95}＼PropertyBag
  - 下载文件夹：{7d83ee9b-2244-4e70-b1f5-5393042af1e4}＼PropertyBag
  - 音乐文件夹：{a0c69a99-21c8-4671-8703-7934162fcf1d}＼PropertyBag
  - 桌面文件夹：{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}＼PropertyBag
  - 文档文件夹：{f42ee2d3-909f-4907-8871-4c22fc0bf756}＼PropertyBag
### 修改电源选项中屏幕关闭与休眠的时间
Power&Sleep
### 关闭无线网卡无活动时自动断电
笔记本电脑使用电池时, 处于省电考虑, 无线网卡可能会关闭电源
设备管理器 - 网路适配器 - 无线网卡 - 属性
## 基础软件
### 7Zip
- https://www.7-zip.org/
### QQ拼音
- <http://qq.pinyin.cn/>
- 中文状态下使用英文标点
- 隐藏状态栏
### Google 日本語入力
### 微信WeChat
- <https://pc.weixin.qq.com/>
- 取消开机启动
### 有道云笔记
- <https://note.youdao.com/download.html>
### Dropbox
- <https://www.dropbox.com/install>
### PotPlayer
- <https://potplayer.daum.net/>
- 不记录历史播放:  选项 / 播放 / 列表 / 取消勾选 记忆近期播放名单/URL地址
- 选项 / 播放 / 鼠标指向进度条时显示缩略图
- 选项 / 基本 / 皮肤/配色 / 视频下自动隐藏
### LibreOffice
- 下载 LibreOffice <https://zh-cn.libreoffice.org/download/libreoffice/>
- 中日韩字体 <https://zh-cn.libreoffice.org/download/fonts/>
  - 将下载后的字体文件解压缩，然后将文件复制到 %windir%\Fonts 文件夹
## 系统增强软件
### Everything 文件搜索工具
- https://www.voidtools.com/zh-cn/
### QTTabbar 资源浏览器增强
- <http://qttabbar.wikidot.com/>, 安装后重启系统, 打开「资源管理器」,「查看」,「选项」,「QTTabBar」
- QTTabBarOption 
  - 关闭文件预览 
    - Preview, Uncheck `Show preview ...`
  - 双击Toolbar时复制现有Tab 
    - Events, Double Clikc on Toolbar, Duplicate active tab
### 火绒安全软件
### TrafficMonitor
任务栏中实时显示网速
## 远程办公环境
### ZOOM 
- <https://zoom.us/download#client_4meeting>
## 基础开发环境
### VS Code
### Putty等远程连接
