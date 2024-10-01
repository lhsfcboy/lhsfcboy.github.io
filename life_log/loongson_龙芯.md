# 龙芯2F 折腾笔记

## Yeeloong 8089_B 配置

### Hardware

- 160G HDD
- Loonson 2F CPU
- 8.9" TFT LCD 1024 x 600
- https://en.wikipedia.org/wiki/Lemote#Netbook_computers

### OS

- DebianYeeloong https://wiki.debian.org/DebianYeeloong/
- LightDM

Debian从龙芯2E时代开始就一直支持龙芯，如今最新的Debian9放弃了2E/2F，只支持龙芯3
我现在使用的是基于vmlinux-4.2.0

[Debian7.11 for loongson-2f](http://mirrors.ustc.edu.cn/debian/dists/Debian7.11/main/installer-mipsel/current/images/loongson-2f/netboot/)

## 基本配置

### 配置网络

- 确认网卡名称: `ls /sys/class/net/`
- 确认配置文件地址: `/etc/network/interfaces`

#### 配置DHCP

```text
    auto eth0
    allow-hotplug eth0
    iface eth0 inet dhcp
```

#### 手动配置

```text
    auto eth0
    iface eth0 inet static
        address 192.168.137.100
        netmask 255.255.255.0
        gateway 192.168.2.254
```

### 配置sshd

- 允许root使用ssh登录
  - 修改`/etc/ssh/sshd_config`
    - `PermitRootLogin yes`
  - 重启ssh服务
    - `/etc/init.d/ssh restart`

## 挂载U盘

- 检查分区挂载情况

```bash
lsblk
sudo blkid
sudo fdisk -l
```

- 执行挂载命令

```bash
sudo mkdir /media/usb
sudo mount /dev/sdb1 /media/usb
sudo umount /media/usb
```

## 离线情况下准备安装环境

- 下载所需要的 **mipsel** 架构下deb文件, 
  - [make](https://packages.debian.org/wheezy/mipsel/make/download)
- 使用dpkg安装deb包
  - `sudo dpkg -i DEB_PACKAGE`

## 安装 USB WiFi 驱动

- [EP-N8508GS](http://www.edup.cn/product-item/ep-n8508gs/)
- [EP-N8508GS 驱动](http://www.edup.cn/?page_id=9592)

- 插入USB wifi转换器之前, 分别运行 `ifconfig -a` 来确认具体的网卡名称

### 驱动安装是碰到的问题


可能的解决方法:

- `apt-get install linux-headers-$(uname -r)`
  - 到哪里去找header文件?
    - `https://packages.debian.org/jessie/linux-headers-loongson-3`

- pass