
# Linux 网络基本设置排障

---

## Netstat

Netstat 用于显示与 IP、TCP、UDP 和 ICMP 协议相关的统计数据，一般用于检验本机各端口的网络连接情况。

---

## 网络

```bash
# ifconfig                # 查看所有网络接口的属性
# route -n                # 查看路由表
# netstat -lntp           # 查看所有监听端口
# netstat -antp           # 查看所有已经建立的连接
# netstat -s              # 查看网络统计信息
```

`netstat` 显示网络状态:
```bash
netstat -tulnp  # 找出目前系统上已在监听的网路连线及其 PID
```

### 查看所有 80 端口的连接数
```bash
netstat -nat | grep -i "80" | wc -l
```

### 对连接的 IP 按连接数量进行排序
```bash
netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
```

### 查看 TCP 连接状态
```bash
netstat -nat | awk '{print $6}' | sort | uniq -c | sort -rn
```

```bash
netstat -an | awk '/^tcp/ {++S[$NF]}; END {for(a in S) print a, S[a]}'
```

```bash
netstat -an | awk '/^tcp/ {++state[$NF]}; END {for(key in state) print key, "	", state[key]}'
```

```bash
netstat -an | awk '/^tcp/ {++arr[$NF]}; END {for(k in arr) print k, "	", arr[k]}'
```

```bash
netstat -an | awk '/^tcp/ {print $NF}' | sort | uniq -c | sort -rn
```

```bash
netstat -ant | awk '{print $NF}' | grep -v '[a-z]' | sort | uniq -c
```

### 查看 80 端口连接数最多的 20 个 IP
```bash
netstat -anlp | grep 80 | grep tcp | awk '{print $5}' | awk -F: '{print $1}' | sort | uniq -c | sort -nr | head -n 20
```

```bash
netstat -ant | awk '/:80/ {split($5,ip,":");++A[ip[1]]} END {for(i in A) print A[i],i}' | sort -rn | head -n 20
```

### 用 tcpdump 嗅探 80 端口的访问看看谁最高
```bash
tcpdump -i eth0 -tnn dst port 80 -c 1000
```

### 查找较多 time_wait 连接
```bash
netstat -n | grep TIME_WAIT | awk '{print $5}' | sort | uniq -c | sort -rn | head -n 20
```

### 查找较多的 SYN 连接
```bash
netstat -an | grep SYN | awk '{print $5}' | awk -F: '{print $1}' | sort | uniq -c | sort -nr | more
```

---

## Tips Command

```bash
# 查看
watch -n 1 "/sbin/ifconfig eth0 | grep bytes"
```

`nload` 和 `iftop` 也可以用于实时查看网络流量情况。

---

## 如何在 Linux 下测试一个 port 是否被防火墙拦截？

可以使用 `telnet ip 端口` 进行测试。如果无法连接，说明该端口可能被防火墙拦截或者未开启相应的服务。
例如：
```bash
telnet www.pku.edu.cn 80  # 可以连接
telnet www.pku.edu.cn 8101  # 无法连接
```

---

## 查看路由表

```bash
ip route show
route
```

---

## NIS

NIS（Network Information System）用于实现账户信息的集中管理。NIS 服务器维护用户帐号信息，用户登录 NIS 客户端时，在 NIS 服务器进行登录验证。

### NIS 安装与配置

1. 安装 NIS 服务器软件包：
```bash
rpm -ivh ypserv...
chkconfig time on
chkconfig time-udp on
service xinetd restart
```

2. 建立服务器的 NIS 域名：
```bash
nisdomainname nistest
echo '/bin/nisdomainname nistest' >> /etc/rc.d/rc.local
echo 'NISDOMAIN=nistest' >> /etc/sysconfig/network
```

3. 设置 `ypserv` 服务的配置文件，启动 NIS 服务器，构建 NIS 数据库。

---

## 网卡工作模式修改

在 Linux 环境下，可以使用 `mii-tool` 或 `ethtool` 设置网卡的工作模式。

### 使用 `mii-tool`

1. 查看网卡的工作模式：
```bash
mii-tool -v
```

2. 更改网卡的工作模式：
```bash
mii-tool -F [media] [interface]
```
示例：
```bash
mii-tool -F 10baseT-HD eth0
```

3. 恢复网卡的自适应工作模式：
```bash
mii-tool -r eth0
```

### 使用 `ethtool`

更详细的使用方法：
```bash
ethtool -s eth0 duplex half autoneg off  # 禁用自协商，启用半双工模式
ethtool -s eth1 duplex full speed 1000 autoneg off  # 禁用自协商，启用全双工，速度设置为 1000Mb/s
```

---

## 路径追踪

使用 `traceroute` 命令来追踪路径。

---
