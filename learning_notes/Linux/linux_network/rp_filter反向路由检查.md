# 反向路由检查

##

linux有一个叫做反向过滤（reverse path filter）的功能，简单来说就是为了防DDOS攻击，会检查报文源地址的合法性，如果反查源地址的路由表，发现源地址下一跳的最佳出接口并不是收到报文的入接口，则将报文丢弃。

为了防止非法的包被转发或送给上层协议，查找路由后Linux还会调用fib_validate_source()以
检查其来源的合法性，基本原理是根据包的源地址查找路由的出接口，然后比较包的原始入接口是
否和查到的出接口一致;如果一致则放过，如果不一致查询skb->dev的rp_filter值，为1时将丢弃这
个包，0时放过。

每个接口的rp_filter配置在/proc/sys/net/ipv4/conf/ethN/rp_filter，其值为1时是使能该
接口反向路由检查机制，为0时则关闭该机制。

在实际运用时该机制可能会带来问题。对于一些虚接口上来的包，如gre0,ipsec0来的包，如果没有
IP地址，从该虚接口上来的包可能被认为来源不合法而被内核DROP。
这时需要根据实际情况设置rp_filter为0，并配置IP地址。

以上分析是根据2.6.32内核代码而来。
更高版本的kernel可能已经解决这个问题，如3.6.3内核，对该机制有改进，对IPSEC的接口不做反射路
由检查。

## 
内核sysctl中的rp_filter变量可以控制反向过滤。其取值如下
```
rp_filter - INTEGER
	0 - No source validation.
	1 - Strict mode as defined in RFC3704 Strict Reverse Path
	    Each incoming packet is tested against the FIB and if the interface
	    is not the best reverse path the packet check will fail.
	    By default failed packets are discarded.
	2 - Loose mode as defined in RFC3704 Loose Reverse Path
	    Each incoming packet's source address is also tested against the FIB
	    and if the source address is not reachable via any interface
	    the packet check will fail.
```


## 
可以直接修改/proc/sys/net/ipv4/conf/${ethx}/rp_filter的值，也可以使用sysctl命令配置

一直生效，可以修改/etc/sysctl.conf
```
# Controls source route verification
net.ipv4.conf.default.rp_filter = 0

```


## debug on log
```
sysctl -w net.ipv4.conf.all.log_martians=1
```
Your syslog will now show dropped packets.