# Secure Shell Protocol

太重要了, 非常值得单列一章讨论

## 预备知识

《SSH 原理与运用》（[上篇](https://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)，[下篇](https://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html)）  

## SSH免密登录的实现

需要“machineA机器的nameA账号”建立到“machineB机器的nameB账号”的ssh信任关系，达到无需输密码即可登陆的目的

核心的四大步骤
- 理解原理, 理解设置目标, 准备工具
- 生成密钥对
  - `cd ~/.ssh/; ssh-keygen -t dsa`
  - 需要注意的是id_dsa.pub是一行文字，如果使用vi查看后复制会导致，在authorized_keys中出现回车符，
    - 最好的办法是cat出来在复制到authorized_keys里面
- 在服务器端和本地端配置密钥
  - 服务器端如果不存在则创建`~/.ssh/authorized_keys`文件
  - 服务器端检查authorized_keys文件的权限，确保其group/other位没有w权限
- 登录
- 故障时的调试

阮一峰的《SSH 入门教程》
- 发布页: https://www.ruanyifeng.com/blog/2020/12/ssh-tutorial.html
- 在线阅读: https://wangdoc.com/ssh/
