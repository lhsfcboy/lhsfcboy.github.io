# 设置新的linux服务器

## Reference

- https://sollove.com/2013/03/03/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers/
- https://becomesovran.com/blog/server-setup-basics.html

## 创建新用户

```console
adduser hereisusername
```

为新用户添加 root 权限

安装 sudo
赋予 sudo 权限

```bash
install sudo
usermod -a -G sudo hereisusername
```

## 设置SSH登录

```bash
# 在登录端生成密钥对
ssh-keygen
# 命令运行结束后，会在本地用户的根目录中的 .ssh 目录下创建一个私钥 id_rsa 和一个公钥 id_rsa.pub

# 复制公钥到服务器端可以使用
ssh-copy-id user-name@server-ip
# 其原理在于把 id_rsa.pub 手动拷贝到了服务器端的 .ssh/authorized_keys 文件中.
```

## 禁用 root 登陆

管理员身份下打开文件  /etc/ssh/sshd_config 并将其中的
PermitRootLogin yes 将其修改为 PermitRootLogin no .
重启 SSH 服务

```bash
systemctl restart ssh
service sshd restart
```

## 本地配置 SSH

`ssh earlgrey@qcloud-cvm-ip` 即可登陆服务器.
不过这样还是有点麻烦，每次都得输入用户名和 IP 地址.
为了进一步简化操作，我们对本地的 SSH 登陆进行配置.

打开 ~/.ssh/config 文件，然后添加如下配置：

```config
Host qcloud
Hostname qcloud-cvm-ip
User earlgrey
IdentityFile ~/.ssh/id_rsa
```

之后，只需要执行 `ssh qcloud` 即可登陆服务器。
