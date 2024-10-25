# Secure Shell Protocol

太重要了, 非常值得单列一章讨论

## 预备知识

《SSH 原理与运用》（[上篇](https://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)，[下篇](https://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html)）  

## SSH免密登录的实现

核心的四大步骤
- 理解原理, 理解设置目标, 准备工具
- 生成密钥对
- 在服务器端和本地端配置密钥
- 登录
- 故障时的调试

阮一峰的《SSH 入门教程》
- 发布页: https://www.ruanyifeng.com/blog/2020/12/ssh-tutorial.html
- 在线阅读: https://wangdoc.com/ssh/
