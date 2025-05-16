


我们甚至可以用Linux脚本, 创建一个简单的web服务器.

```bash
#!/bin/bash
#===============================================================================
#
#          FILE:  webserver.sh
#         USAGE:  chmod +x webserver.sh; ./webserver.sh
#   DESCRIPTION:  在8080端口启动一个模拟的Web服务器
#          TEST:  curl http://localhost:8080
#===============================================================================

while true; do
  # 使用 nc 监听端口 8080，处理一个连接后退出
  {
    echo -ne "HTTP/1.1 200 OK\r\n"
    echo -ne "Content-Length: 13\r\n"
    echo -ne "Content-Type: text/plain\r\n"
    echo -ne "Connection: close\r\n"
    echo -ne "\r\n"
    echo -ne "Hello, world"
  } | nc -l -p 8080 -q 1
done

```
