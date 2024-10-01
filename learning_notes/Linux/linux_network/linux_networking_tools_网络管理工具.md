# Linux Networking Tools 
ss, nmap, dig, netcat, ping, tcpdump, socat, top, ethtool 

https://twitter.com/devops_tech/status/1446683409644851201

## ss / netstat
ss command is a tool that is used for displaying network socket related information on a Linux system

查看远程的 IP 连接并统计

netstat -atn | awk '{print $5}' | awk -F ':' '{print $1}' | sort -n | uniq -c

## nmap


## dig


## netcat


## ping


## tcpdump


## socat


## top


## ethtool 
