# VB虚拟机中Ubuntu的安装

## Virtual Box 基础设置
- 安装增强功能
- 删除launcher中不使用的快捷方式
- 共享粘贴板 - 双向
- 共享文件夹
  - 添加当前用户到vboxsf用户组
  - `sudo adduser $USER vboxsf`

## Basic Dev Tools

```text
sudo apt-get install git
sudo apt -y install make gcc g++ libtool
apt-get install -y build-essential libssl-dev
```

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

## Node.js 6.x npm

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

## Go 1.7.6

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






