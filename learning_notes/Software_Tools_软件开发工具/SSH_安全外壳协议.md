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
  
## 加密与口令

### 密文与原文

- **密文** = $(\text{加密算法}, \text{加密用密钥}, \text{原文})$  
- **原文** = $(\text{加密算法}, \text{解密用密钥}, \text{密文})$

设想的情况是，密文在传输过程中对所有人可见。如果能够100%确保信息传输过程保密，就不需要加密了，例如使用国防光缆。然而，维持一个保密的传输信道代价昂贵，并且假设传输信道是绝对安全的不可取。因此，不能依赖传输信道的保密性来保证信息传递的安全性。

---

### 对加密通信的攻击方式

1. 窃听后解密  
2. 中间人攻击  

---

### 对称加密

- **加密过程**以$f$表示。  
- 面临的主要挑战是**密钥管理的困难**，特别是密钥长期使用时可能被泄露。  
- **好的加密算法**需要平衡以下因素：
  - 密文长度与原文长度的比例。
  - 执行速度（加密和解密的速度不一定相同，也没有必要相同）。

---

### 非对称加密：签名

非对称加密利用两个素数相乘容易，而从乘积推导这两个素数困难的特点：

- **私钥加密**必须用公钥解密，且结果无法用私钥解密。  
- **公钥加密**必须用私钥解密，且结果无法用公钥解密。  
- 公钥和私钥的关系：  
  - 持有私钥无法推测出公钥。  
  - 持有公钥无法推测出私钥。  

---

### SSH终端软件

#### Windows下的SSH终端：

- **较新的Windows系统**预装了`ssh`，可以直接使用。  
- **常见SSH工具**：  
  - `OpenSSH`  
  - `PuTTY`  

#### Mac下的工具：

- **推荐工具**：`iTerm2`

---

### 原理与工程实现

#### 非对称加密的具体应用：SSH免密码登录

常见的工程实践：**堡垒机**。  

**Linux/Mac环境下的命令**：  

```bash
ssh -J <jump-user>@<jump-host> <protected-user>@<protected-host>
```

创建SSH配置文件 `~/.ssh/config` 示例：

```plaintext
Host jump
    User <jump-user>
    HostName <jump-host>

Host protected
    User <protected-user>
    HostName <protected-host>
    ProxyJump jump
```

**Windows使用OpenSSH**：  

- 在Windows 10（版本1803或更新）中，`OpenSSH`是内置的。  
- 旧版本可以通过安装"Optional Feature"中的"OpenSSH Client"来使用。

**Windows PuTTY的ProxyJump设置**：  

- PuTTY自版本0.77起支持"SSH proxy"功能，等价于`-J`或`ProxyJump`。

### 不是加密的单向加密：摘要算法

#### 口令类数据的安全存储攻防

- **MD5算法被破解**：  
  王小云老师对MD5算法的破解，显示出其存在严重的安全性缺陷。

### 思考题

1. **SSH的key文件可以复用吗？**  
   - 可以，但并不推荐。  

2. **实验1**：公钥和私钥是我们指定的吗？  
   - 如果调换公钥和私钥的内容，是否依然可行？  
     - 从加密解密的角度来看，这是可行的。

3. **公钥与私钥的关系**：  
   - 持有私钥可能计算出公钥。  


### 参考与扩展阅读

- **Deniffer**：SSH免密登录背后！保姆级解读，手把手教学。  
- **清凉薄荷**：Linux上SSH免密登录原理及实现。
