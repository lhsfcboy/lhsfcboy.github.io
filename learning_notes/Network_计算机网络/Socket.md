# 计算机网络编程

本篇讨论计算机网络在代码层面的具体实现

## 网络编程头文件

```shell
find / -name in.h 2>/dev/null

/usr/include/netinet/in.h # 网络编程用的头文件
```

`usr/include/netinet/in.h`是 POSIX 标准的网络编程头文件，定义了常用的网络协议相关的结构和常量，如 IP 地址、端口、套接字等。大多数网络编程（如 socket 编程）会直接包含这个头文件。

```c

/* Internet address.  */
typedef uint32_t in_addr_t;
struct in_addr
  {
    in_addr_t s_addr;
  };


/* Type to represent a port.  */
typedef uint16_t in_port_t;

/* Structure describing an Internet socket address.  */
struct sockaddr_in
  {
    __SOCKADDR_COMMON (sin_);    // sa_family_t sin_family
    in_port_t sin_port;                 /* Port number.  */
    struct in_addr sin_addr;            /* Internet address.  */

    /* Pad to size of `struct sockaddr'.  */
    unsigned char sin_zero[sizeof (struct sockaddr)
                           - __SOCKADDR_COMMON_SIZE
                           - sizeof (in_port_t)
                           - sizeof (struct in_addr)];
  };
```

`sin`是`socket adress internet`的缩写
