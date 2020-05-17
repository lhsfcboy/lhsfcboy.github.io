# Windows 10 操作系统的配置

## 操作系统基础设置
### 更改计算机名称
计算机名称会被用于蓝牙设备等.
- Settings / System / About /  Device specifications / Rename this PC
- Restart to apply
### 关闭快速访问历史Clear/Diable Windows 10 Quick Access History
- Click Start and type: file explorer options, General Tab, Privacy section
### 关闭活动历史时间线功能
Win+Tab会显示近期打开的文档等
- Setting / Privacy / Activity history, Disable and Clear
### 任务栏
- Personalization / Taskbar
- Use small taksbar buttons
- Cobine task bar buttons: When taskbar is full
- Show taskbar on all displays: off
### 桌面
- Windows 设置 / 个性化 / 主题 / 桌面图标设置 / 取消将回收站固定到桌面
### Uninstall Pre-Installed App
- McAfee
- MS Office
- MS OneDrive
### 删除自带的Metro应用
- WIP <https://www.howtogeek.com/224798/how-to-uninstall-windows-10s-built-in-apps-and-how-to-reinstall-them/>
### 关闭休眠(可选)
管理员CMD: `powercfg -h off`
### 关闭系统备份还原
控制面板>系统与还原>系统，左侧“系统保护”>设置，里面选择第三项“关闭系统还原”
### 清理Windows 资源管理器(Explorer)侧边栏 与 这台电脑(This PC)中得快捷方式
有桌面, 文档, 下载, 音乐, 图片, 视频, 3D 对象的快捷方式, 需要通过'以管理员身份'运行regedit进行清理. 清理操作无需重启, 即刻生效.
- 3D Objects
  - Hkey_LOCAL_MACHINESOFTWAREMicrosoftWindowsCurrentVersionExplorerMyComputerNamespace
  - 右键删除{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}
  - 64 位的 Windows 10 操作系统还需要追加如下操作
    - Hkey_LOCAL_MACHINESOFTWAREWow6432NodeMicrosoftWindowsCurrentVersionExplorerMyComputerNamespace
- 其他链接的清理
  - <https://www.techspot.com/guides/1703-remove-3d-objects-shortcut-windows-file-explorer/>
  
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
- 不记录历史播放:  选项 / 播放 / 列表 / 取消勾选 记忆近期播放名单/URL地址
- 选项 / 播放 / 鼠标指向进度条时显示缩略图
## 系统增强软件
### QTTabbar 资源浏览器增强
- <http://qttabbar.wikidot.com/>, 安装后重启系统.
- 打开「资源管理器」,「查看」,「选项」,「QTTabBar」
- <https://sspai.com/post/52521>
### 火绒安全软件
### TrafficMonitor
任务栏中实时显示网速
## 远程办公环境
### ZOOM 
- <https://zoom.us/download#client_4meeting>
## 基础开发环境
### VS Code
