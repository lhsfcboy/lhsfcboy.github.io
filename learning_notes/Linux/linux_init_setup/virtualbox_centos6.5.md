# VirtualBox 环境下的 CentOS 6.5 的配置

## 网卡的设置

- eth0: NAT
- eth1: Host-Only

eth0的NAT保持了Guest机对外网的访问,
而eth1方便了Host机访问内网Guest机.

## 注意点

Host机的虚拟网卡的IP设置在VirtualBox当中, 而不是Windows的`网络配置中心`

如果修改过网卡地址的话, 注意检查如下文件:
`/etc/udev/rules.d/70-persistent-net.rules`

默认网关需要主动指定为eth0

## 命令工具

- `route -n`
  - 检查路由

- `service network restart`
  - 重新载入网络相关设置

## 参考配置

```text
# cat /etc/sysconfig/network
NETWORKING=yes
HOSTNAME=localhost.localdomain
GATEWAYDEV=eth0

# cat /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=dhcp

cat /etc/sysconfig/network-scripts/ifcfg-eth1
DEVICE=eth1
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.56.10
GATEWAY=192.168.56.1
NETMASK=255.255.255.0
IPV6INIT=no
```

## 参考文章

- [Linuxルーティング追加](http://www.server-memo.net/centos-settings/network/linux-routeing.html#i)