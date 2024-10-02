# TCPDUMP命令详解

<https://note.youdao.com/ynoteshare1/index.html?id=33436c25eb93a8a4a7edda8499aab103>

tcpdump -w /opt/test.pcap
tcpdump -i eth7 icmp          #watching ICMP packets on eth7
tcpdump -nn -s 1600 -w /opt/nTI-agent.pcap  host 172.16.181.58 and host 172.16.181.239

#tcpdump host 210.27.48.1 and \ (210.27.48.2 or 210.27.48.3 \)
#tcpdump tcp port 23 host 210.27.48.1
#tcpdump ip host 210.27.48.1 and ! 210.27.48.2
tcpdump -n host 172.16.181.51 | tee test-tcpdump.log



tcpdump采用命令行方式，它的命令格式为：
tcpdump [ -adeflnNOpqStvx ] [ -c 数量 ] [ -F 文件名 ][ -i 网络接口 ] [ -r 文件名] [ -s snaplen ][ -T 类型 ] [ -w 文件名 ] [表达式 ]

　　-a          将网络地址和广播地址转变成名字；
　　-d          将匹配信息包的代码以人们能够理解的汇编格式给出
-e          在输出行打印出数据链路层的头部信息；
　　-f           将外部的Internet地址以数字的形式打印出来；
　　-l           使标准输出变为缓冲行形式；
-n          不把网络地址转换成名字；
     -nn     Don't convert host  addresses and  port  numbers to names.
-t           在输出的每一行不打印时间戳；
　　-v           输出一个稍微详细的信息，例如在ip包中可以包括ttl和服务类型的信息；
　　-vv         输出详细的报文信息；
　　-c           在收到指定的包的数目后，tcpdump就会停止；q
　　-F           从指定的文件中读取表达式,忽略其它的表达式；
     -D     Print the list of the network interfaces available on the system
　　-i            指定监听的网络接口；
　　-r           从指定的文件中读取包(这些包一般通过-w选项产生)；
　　-w          直接将包写入文件中，并不分析和打印出来；
　　-T           将监听到的包直接解释为指定的类型的报文，常见的类型有rpc (远程过程调用)和snmp(简单网络管理协议；)
　　2、tcpdump的表达式介绍
　　表达式是一个正则表达式，tcpdump利用它作为过滤报文的条件，如果一个报文满足表达式的条件，则这个报文将会被捕获。如果没有给出任何条件，则网络上所有的信息包将会被截获。 在表达式中一般如下几种类型的关键字，一种是关于类型的关键字，主要包括host， net，port, 例如 host 210.27.48.2，指明 210.27.48.2是一台主机，net 202.0.0.0 指明202.0.0.0是一个网络地址，port 23 指明端口号是23。如果没有指定类型，缺省的类型是host.
　　第二种是确定传输方向的关键字，主要包括src , dst ,dst or src, dst and src ,这些关键字指明了传输的方向。举例说明，src 210.27.48.2 ,指明ip包中源地址是210.27.48.2 , dst net 202.0.0.0 指明目的网络地址是202.0.0.0 。如果没有指明方向关键字，则缺省是src or dst关键字。
　　第三种是协议的关键字，主要包括fddi,ip ,arp,rarp,tcp,udp等类型。Fddi指明是在FDDI(分布式光纤数据接口网络)上的特定的网络协议，实际上它是"ether"的别名，fddi和ether具有类似的源地址和目的地址，所以可以将fddi协议包当作ether的包进行处理和分析。 其他的几个关键字就是指明了监听的包的协议内容。如果没有指定任何协议，则tcpdump将会听所有协议的信息包。
　　除了这三种类型的关键字之外，其他重要的关键字如下：gateway, broadcast,less,greater,还有三种逻辑运算，取非运算是 'not ' '! ', 与运算是'and','&amp;&amp;';或运算 是'or' ,'||'；
　　这些关键字可以组合起来构成强大的组合条件来满足人们的需要，下面举几个例子来说明。
  
  
  
  
