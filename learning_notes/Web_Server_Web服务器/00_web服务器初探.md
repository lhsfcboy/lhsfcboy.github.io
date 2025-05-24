# Web服务器初探

我们可以用Linux脚本, 创建一个简单的web服务器.

```bash
#!/usr/bin/env bash
#===============================================================================
#          FILE:  webserver.sh
#         USAGE:  chmod +x webserver.sh; ./webserver.sh
#   DESCRIPTION:  在8080端口启动一个模拟的Web服务器
#       EXAMPLE:  curl -v http://localhost:8080
#===============================================================================

msg="Hello, world"
while true; do
  {
    printf "HTTP/1.1 200 OK\r\n"
    printf "Content-Type: text/plain\r\n"
    printf "Content-Length: %d\r\n" "${#msg}"
    printf "Connection: close\r\n"
    printf "\r\n"
    printf "%s" "${msg}"
  } | nc -l 8080 -q 1
done

```

我们也可以通过浏览器访问这个服务器，查看返回的页面。
`http://140.238.59.191:8080/`

从开发工具/Network/Request/Headers中查看返回的响应头。正是我们所输出的语句.
注意观察服务器端的输出。对比curl访问和浏览器访问时的区别.

我们还可以模拟一下大量的访问请求:
`for i in {1..100}; do curl -s http://localhost:8080 & done`
