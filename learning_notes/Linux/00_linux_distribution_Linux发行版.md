# Linux GCC

Linux中的GCC是一件很麻烦的事情, 轻易不要碰的好。
这也是Docker飞速发展的原因

## 常见发行版

对初学者而言各个系统几乎没有区别。
对实际系统维护者而言，我们也很少处在挑选发行版的状态。
如果不知道应该选择什么，那就意味着对发行版没有特别要求。

这种情况统一选择 Ubuntu 发行版的最新的 LTS（长期支持）版本，这些版本每两年发布一次，具有 5 年的支持周期。
5年以后呢？5年以后公司在不在都还不一定呢。

- Debian / Ubuntu
- Fedora / RHEL / CentOS / Rocky
  - CentOS流行于2010年以前
- openeuler
  - 华为主推的免费开源系统
  - 国内自主化项目可能会用到
 
    
## 发行版的几个核心指标: Linux内核版本，GCC，GLIBC版本

- Docker容器化技术流行以后，内核版本`uname -r`变成了很关键的考虑因素。
- https://en.wikipedia.org/wiki/Linux_kernel_version_history#Releases_6.x.y
| Distribution                    | Version       | Kernel Version | GCC Version | glibc Version | Support Lifetime      |
|---------------------------------|---------------|----------------|-------------|---------------|-----------------------|
| Red Hat Enterprise Linux        | 9.3           | 5.14           | 11          | 2.34          | May 2032              |
| Ubuntu LTS                      | 22.04 LTS     | 5.15           | 11.2        | 2.35          | April 2027 (Standard) |
| SUSE Linux Enterprise Server    | 15 SP5        | 5.14           | 7.5         | 2.26          | 2028 (Standard)       |
| Debian                          | 12 (Bookworm) | 6.1            | 12.2        | 2.36          | June 2028             |
| Oracle Linux                    | 9             | 5.14           | 11          | 2.34          | June 2032             |
