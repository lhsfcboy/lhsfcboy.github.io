# Vagrant

## Install

### 安装vagrant

#### Windows7

Win7 pro x64 自带的PowerShell是版本2, 而Vagrant 1.9.7 以后, Vagrant使用了PowerShell 3.
解决办法有

- 降级到[1.9.6](https://releases.hashicorp.com/vagrant/1.9.6/)
- 安装PS3
  - 检查PS版本: `$PSVersionTable`

修改`VAGRANT_HOME`, 将默认指向的`C:/Users/USERNAME/.vagrant.d/boxes`, 改为`D:\ProgramData\.vagrant.d`

### 安装virtual box

全局设置中修改 `默认虚拟机位置/Default Machine Folder` 为 `D:\ProgramData\VirtualBox VMs`

## 创建虚拟机

```bash
# 添加本地镜像
vagrant box add centos65 /vagrant/centos/centos65-x86_64.box
# centos65是box的别名

cd /vagrant/centos #切换目录，随意
vagrant init centos65 #为centos65初始化一个环境
```

执行命令后，/vagrant/centos目录下会有一个叫Vagrantfile的文件

```bash
config.vm.network "private_network", ip: "192.168.33.10"
# 虚拟机会拥有一个为192.168.33.10的IP,宿主可以通过ssh访问到这个虚拟机
config.vm.synced_folder "../data", "/vagrant_data"
# vagrant可以为虚拟机提供一个映射目录，这样可以很简便地为虚拟机与宿主之间共享文件
config.vm.network "forwarded_port", guest: 80, host: 8080
将宿主的8080端口的TCP请求转发到虚拟机的80端口中
```

## 启动

```bash
vagrant up
```