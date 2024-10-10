
# working_on_unfamiliar_linux_hosts

在工作中，我们经常需要登录到一台不归自己管理的陌生的 Linux 主机上，进行一些如查看日志文件、排除系统故障、修改配置文件等任务。此时，我们可能会面临一些挑战。

## 常见挑战

- 没有预装常用的管理软件，也没有权限或网络连接来安装
   - 例子：未安装 `htop`，无法使用更直观的界面查看系统信息。
   - 习惯使用 Linux 默认命令
   - 不追求各种第三方工具的便捷性 利用系统自带的工具进行任务处理

2. 软件版本与预期不一致
   例子：预期的 Python 版本为 3，但实际安装的是 Python 2。

3. 常用的 alias 设置不一致
   - 无法使用自己习惯的快捷命令。

## 使用 `export` 等设置常用命令的参数

可以通过 `export` 命令设置一些环境变量，以提高工作效率：

```bash
export GREP_OPTIONS='--color=auto'  # 使得 grep 命令以彩色高亮搜索结果
# GREP_OPTIONS 已在较新的 grep 版本中被弃用（自 GNU grep 2.21 起）
   
alias grep='grep --color=auto -i' # 使得 grep 命令以彩色高亮搜索结果
export PS1='\u@\h:\w\$ '          # 设置命令行提示符显示 用户名@主机名:当前目录$

export HISTCONTROL=ignoredups:erasedups
                                  # ignoredups：忽略重复的命令。
                                  # erasedups：删除所有重复的命令，只保留最后一个
export HISTIGNORE="ls:cd:cd -:pwd:exit:history"
                                  # HISTIGNORE：指定不记录的命令列表
export PROMPT_COMMAND='history -a'
                                  # 每次显示提示符前，自动将保存当前会话的历史命令，确保历史记录的实时性
export CLICOLOR=1                 # 启用颜色输出
export LS_COLORS='di=34:ln=36:so=35:pi=33:ex=32:*.txt=31:*.sh=32'
                                  # 定义不同类型文件的颜色编码。
                                  # 目录（di）为蓝色，符号链接（ln）为青色，可执行文件（ex）为绿色，.txt 文件为红色，.sh 文件为绿色

# 模拟tree命令
which tree # 确认没有现存的tree命令或别名
            find . | sed -e "s/[^-][^\/]*\//  |/g" -e "s/|\([^ ]\)/|-\1/"  # 确认命令运行正常
alias tree='find . | sed -e "s/[^-][^\/]*\//  |/g" -e "s/|\([^ ]\)/|-\1/" '

# 模拟watch命令
which watch
alias watch='func() { while true; do clear; "$@"; sleep 5; done; }; func'

```


### 快速掌握系统的主要信息

```bash
cat /etc/os-release # 查看 Linux 发行版本
uptime              # 查看系统已启动时间
df -h               # 查看磁盘使用情况
```
