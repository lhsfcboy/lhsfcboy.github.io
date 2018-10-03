# curl

curl是一个向服务器传输数据的工具，它支持http、https、ftp、ftps、scp、sftp、tftp、telnet等协议

```bash
# 源代码输出
curl http://www.baidu.com
# Save
curl -o /tmp/baidu.html http://www.baidu.com
# GET请求
curl http://www.baidu.com/s?wd=curl
# POST请求
curl -d "name=test&page=1" http://www.baidu.com
// -d 参数指定表单以POST的形式执行
# 只展示Header
curl -I  http://www.baidu.com
# 显示通信过程
## -v参数可以显示一次http通信的整个过程，包括端口连接和http request头信息
curl -v www.baidu.com
curl --trace output.txt www.baidu.com
curl --trace-ascii output.txt www.baidu.com
# HTTP方法
curl -X POST www.example.com
curl -X DELETE www.example.com
# Referer字段
curl --referer http://www.example.com http://www.example.com
# User Agent字段
curl --user-agent "[User Agent]" [URL]
# 增加头信息
curl --header "Content-Type:application/json" http://example.com
```
