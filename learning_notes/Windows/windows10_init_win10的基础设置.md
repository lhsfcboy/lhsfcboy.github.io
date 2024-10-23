## 操作系统基础设置
- 更改计算机名称
计算机名称会被用于蓝牙设备等. - Settings / System / About /  Device specifications / Rename this PC - Restart to apply

- 关闭活动历史时间线功能
Win+Tab会显示近期打开的文档等 - Setting / Privacy / Activity history, Disable and Clear

- 任务栏
  - Personalization / Taskbar
  - Use small taksbar buttons
  - Cobine task bar buttons: When taskbar is full
  - Show taskbar on all displays: off 双屏幕时的任务栏显示 个性化/任务栏
  - 总是在任务栏显示language bar (以避免其自动调整size)
    - Settings / Time & language / Language / Keyboard / Advanced keyboard settings
    - Use the desktop language bar when it's available.
- 桌面
  - Windows 设置 / 个性化 / 主题 / 桌面图标设置 / 取消将回收站固定到桌面
 
## 文件夹重新链接
- 使用下载目录作为默认的文件Inbox
- 截图文件夹默认保存到下载目录
- 扫描文件默认保存到下载目录

## 关闭休眠(可选)
- 休眠把内存中的数据保存到硬盘中然后关机, 下次开机可以快速完成
- 用于保存内存数据的文件，只能在C盘根目录，文件名是`Hiberfil.sys`, 大小约为内存50%
- 管理员CMD执行 `powercfg -h off` 可以关闭这个功能

## 关闭系统备份还原
控制面板>系统与还原>系统，左侧“系统保护”>设置，里面选择第三项“关闭系统还原”

## 清理Windows 资源管理器(Explorer)侧边栏 与 这台电脑(This PC)中得快捷方式
有桌面, 文档, 下载, 音乐, 图片, 视频, 3D 对象的快捷方式

## 修改电源选项中屏幕关闭与休眠的时间
Power&Sleep

## 关闭无线网卡无活动时自动断电
笔记本电脑使用电池时, 处于省电考虑, 无线网卡可能会关闭电源 设备管理器 - 网路适配器 - 无线网卡 - 属性

## Uninstall Pre-Installed App
- McAfee
- MS Office
- MS OneDrive
- 
## 删除自带的Metro应用
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

## 以下三个APP有待确认具体用途
# Uninstall Store:
Get-AppxPackage *windowsstore* | Remove-AppxPackage
# Uninstall Photos:
Get-AppxPackage *photos* | Remove-AppxPackage
# Uninstall OneNote:
Get-AppxPackage *onenote* | Remove-AppxPackage
```
