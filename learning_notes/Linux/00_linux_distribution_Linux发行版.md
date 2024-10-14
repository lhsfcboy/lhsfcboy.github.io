# Linux GCC

Linux中的GCC是一件很麻烦的事情, 轻易不要碰的好。
这也是Docker飞速发展的原因

## 常见发行版

发行版的选择
- 对初学者而言各个系统几乎没有区别。
- 对实际系统维护者而言，我们也很少处在挑选发行版的岗位。
- 如果不知道应该选择什么，那就意味着对发行版没有特别要求。
- 这种情况统一选择 Ubuntu 发行版的最新的 LTS（长期支持）版本，这些版本每两年发布一次，具有 5 年的支持周期。
  - 5年以后呢？5年以后公司在不在都还不一定呢。

常见的发行版
- Debian / Ubuntu
  - 默认选择Ubuntu版本
- Fedora / RHEL / CentOS / Rocky
  - CentOS流行于2010年以前
- openeuler
  - 华为主推的免费开源系统
  - 国内自主化项目可能会用到

## 发行版的几个核心指标: Linux内核版本，GCC，GLIBC版本

- 云主机服务商开始发布各自的Linux版本
  - 亚马逊 AWS
    - Amazon Linux 2
    - Amazon Linux 2023
  - 微软 Azure
  - 甲骨文云（Oracle Cloud）
    - Oracle Linux 甲骨文基于RHEL克隆的Linux发行版
- Docker容器化技术流行以后，内核版本`uname -r`变成了很关键的考虑因素。
  - 1对1对应RHEL发布 https://en.wikipedia.org/wiki/Oracle_Linux#Release_history
- Linux内核
  - 官网 https://www.kernel.org/
  - latest stable:   6.11
  - 最近的大版本 https://en.wikipedia.org/wiki/Linux_kernel_version_history#Releases_6.x.y

企业应用中流行的版本  
| Distribution                    | Version       | Kernel Version | GCC Version | glibc Version | Support Lifetime      |
|---------------------------------|---------------|----------------|-------------|---------------|-----------------------|
| Red Hat Enterprise Linux        | 9.3           | 5.14           | 11          | 2.34          | May 2032              |
| Ubuntu LTS                      | 22.04 LTS     | 5.15           | 11.2        | 2.35          | April 2027 (Standard) |
| SUSE Linux Enterprise Server    | 15 SP5        | 5.14           | 7.5         | 2.26          | 2028 (Standard)       |
| Debian                          | 12 (Bookworm) | 6.1            | 12.2        | 2.36          | June 2028             |
| Oracle Linux                    | 9             | 5.14           | 11          | 2.34          | June 2032             |

RHEL红帽企业版的内核版本: 
- 版本使用说明: https://access.redhat.com/articles/3078
- RHEL 9 5.14
- RHEL 8 4.18
- RHEL 7 3.10
- RHEL 6 2.6

Ubuntu 的内核版本将以发布时最新版本为准. 2024, Ubuntu announced a change in policy to always use the latest upstream code of the Linux kernel at the time of each Ubuntu release, even if the kernel code hasn't seen a stable release.
- 版本使用说明: https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle
- 24.10 6.11
- 24.04 6.8
- 22.04 5.15
- 20.04 5.4
- 18.04 4.15
- 16.04 4.4
