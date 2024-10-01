# Ubuntu的安装配置

## Virtual Box 基础设置
- 安装增强功能
- 删除launcher中不使用的快捷方式
- 共享粘贴板 - 双向
- 共享文件夹
  - 添加当前用户到vboxsf用户组
  - `sudo adduser $USER vboxsf`
- 从系统设置中关闭屏幕锁定
- 从系统设置中启用自动隐藏Launcher
  - System Settings | Appearance | Behavio

## Basic Dev Tools

```text
sudo apt-get update
sudo apt-get install git vim
sudo apt -y install make gcc g++ libtool
sudo apt-get install -y build-essential libssl-dev
```

## 删除不常用的软件

```text
apt purge unity-webapps-common
apt purge thunderbird totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines cheese gnome-sudoku transmission-common gnome-orca webbrowser-app landscape-client-ui-install
apt purge deja-dup
# unity-webapps-common Amazon 链接
# thunderbird 雷鸟邮件客户端
# totem 自带的播放器
# rhythmbox 自带的音乐播放器
# empathy 自带的即时聊天应用
# brasero 自带的光盘刻录器
# simple-scan 扫描仪
# gnome-mahjongg 对对碰游戏
# aisleriot 纸牌游戏
# gnome-mines 扫雷游戏
# cheese webcam 应用
# gnome-sudoku 数独游戏
# transmission-common BT 客户端
# gnome-orca 屏幕阅读
# webbrowser-app Ubuntu 自带的浏览器（有了 chrome 和 Firefox 根本用不到这个）
# landscape-client-ui-install landscape 远程控制软件
# deja-dup 备份
# onboard 屏幕键盘

# 可以删除libreoffice
apt purge libreoffice-common

```

## 桌面应用类

```text
# 使用chromium浏览器
sudo apt install chromium-browser
sudo apt remove firefox  # 卸载 FireFox，视自己喜好而定。
chromium-browser  # 打开 Chromium 浏览器

sudo apt-get instll -y indicator-multiload #系统监视插件，装完在顶栏就能看到
```
## 中文相关

- 搜狗输入法
  - <https://pinyin.sogou.com/linux/>
  - 安装完成后, 注销再登入, 齿轮设置->language support->keyboard input method system
  - Ctrl+空格切换输入法
- WPS  
  - <https://www.wps.cn/product/wpslinux>
  - 导入Windows字体  
    - <https://www.jianshu.com/p/5042a4855267>
```text
sudo dpkg -i wps-office_10.1.0.6757_amd64.deb
sudo apt install -f
```

- 卸载自带的fcitx输入法
 - `sudo apt-get remove fxitx`
## 开发工具类

- vscode
  - https://code.visualstudio.com/


## Docker Community Edition
<https://docs.docker.com/install/linux/docker-ce/ubuntu/>

```text
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -    
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get -y install docker-ce docker-ce-cli containerd.io

sudo groupadd docker
sudo usermod -aG docker $USER
#reboot
docker run hello-world
```

## Docker Compose
- <https://docs.docker.com/compose/install/>
- <https://github.com/docker/compose/releases>

```text
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

#或者直接apt安装
sudo apt -y install docker-commpose

docker-compose --version
#docker compose会自动安装所依赖的python2.7
python -V #检查是否是2.7
```

## Node.js & npm

Hyperledger Fabric SDK for Node.js, version 8.9.4 and higher or 10.15.3 and higher.

- <https://github.com/nodesource/distributions/blob/master/README.md>

```text
curl -sL https://deb.nodesource.com/setup_6.x | sudo bash -
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

node -v
npm -v

#或者使用
sudo apt-get install nodejs
# Node.js and npm packages are available from the default Ubuntu 18.04 repositories.
# At the time of writing, the version included in the Ubuntu repositories is v8.10.0 which is the previous TLS version.

#或者使用n工具来制定想要的版本
  sudo npm cache clean -f
  sudo npm install -g n
  sudo n 8
  
#或者使用snap工具
#https://github.com/nodesource/distributions/blob/master/README.md#snapinstall
sudo snap install node --classic --channel=8
sudo snap refresh node --channel=10
```

## Golang

```text
# Archived versions could be found at https://golang.org/dl/
wget https://dl.google.com/go/go1.7.6.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.7.6.linux-amd64.tar.gz

wget https://dl.google.com/go/go1.9.2.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.9.2.linux-amd64.tar.gz 

echo $PATH
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.profile
echo 'export GOROOT=/usr/local/go' >> ~/.profile
echo 'export GOPATH=$HOME/go' >> ~/.profile
chmod +x ~/.profile
~/.profile
echo $PATH

# Or, install from APT
# https://github.com/golang/go/wiki/Ubuntu

go version
```






