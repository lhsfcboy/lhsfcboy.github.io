# Bash编程练习

本文将给出一系列的Bash编程练习和对应参考实现。

## 练习题: 观察shell脚本中的特殊变量
- 使用 $* 输出所有参数。
- 使用 $# 输出参数个数。
- 使用 $$ 输出当前脚本的 PID。
- 使用 $! 输出最近一个后台进程的 PID。
- 使用 $? 输出上一个命令的退出状态码。
### 参考实现
```bash
#!/bin/sh
echo $*
echo $#
echo $$
echo $!
echo $?
```

## 练习题: 打印命令行参数

### 具体要求：
1. 编写一个 Shell 脚本，使用 `for` 循环来遍历传递给脚本的所有命令行参数。
2. 在循环中，逐个输出每个参数。
3. 假设传递的参数是一些天数（如 `Monday`、`Tuesday` 等），脚本应当输出每个天数。
### 提示：
- 使用 $* 获取所有命令行参数。
- 使用 for 循环逐个遍历参数。
### 参考实现
```bash
for DAY in $*
do
	echo $DAY
done
```

## 练习题: 检查进程是否运行
- 例如 Apache2 或 sshd 进程
- 给出合适的输出告知用户检查结果
- 简单命令的执行, if分支的应用
### 参考实现
```bash
#!/bin/sh

APA_STA=`pgrep httpd`
if [ "$APA_STA" != "" ]
then
	echo "Apache2 is running!"
else
	echo "Apache2 not running! help!"
fi	
```

## 练习题: 输出 1 到 10 的数字

### 具体要求：

1. 编写一个 Shell 脚本，输出从 1 到 10 的数字。
2. 使用 `while` 循环来遍历 1 到 10，并在每次循环中输出当前数字。
3. 在循环中，逐次将数字增加 1，直到数字超过 10 时循环结束。

### 提示：
- 使用 `while` 循环判断数字是否小于或等于 10。
- 使用 Shell 内置的算术运算符 `(( ))` 来增加数字。

### 参考实现
```bash
#!/bin/sh

NUM=1
while [ $NUM -le 10 ]; do
    echo $NUM
    NUM=$((NUM + 1))  # 使用内置算术运算符
done
```

## 练习题: 文件备份

编写一个 Shell 脚本，用于备份指定的文件或目录，并将备份的结果压缩为 `.tar.gz` 文件。备份的文件名应包含当前日期，并且将备份操作的成功或失败记录到日志文件中。

### 具体要求：

1. 脚本应接受一个参数，该参数为需要备份的文件或目录的路径。
2. 备份的文件应保存到 `/backup/` 目录中，文件名格式为 `文件名_YYYYMMDD.tar.gz`，其中 `YYYYMMDD` 为备份执行时的日期。
3. 备份完成后，脚本应将 `.tar` 文件压缩为 `.tar.gz` 文件。
4. 脚本应将备份操作的结果（成功或失败）记录到 `/backup/文件名_backup.log` 日志文件中，日志条目应包括当前时间和备份结果信息。
5. 如果 `/backup` 目录不存在，脚本应自动创建该目录。
6. 日志文件应记录成功或失败的详细信息，例如：
   - 成功：`YYYY-MM-DD HH:MM:SS 文件名 YYYYMMDD backup have succeeded`
   - 失败：`YYYY-MM-DD HH:MM:SS ERROR: failure 文件名 YYYYMMDD backup`

### 提示：
- 使用 `tar` 命令创建备份文件。
- 使用 `gzip` 命令进行文件压缩。
- 使用 `$?` 检查命令执行的结果。

### 示例输入：
```bash
./backup.sh /path/to/file_or_directory
```

### 示例输出：
1. `/backup/file_or_directory_YYYYMMDD.tar.gz` 备份文件被成功创建。
2. `/backup/file_or_directory_backup.log` 日志文件中记录了备份成功或失败的信息。
### 参考实现
```bash
#!/bin/sh
# Backup files specified by first argument and log the process

# Ensure backup directory exists
[ ! -d /backup ] && mkdir /backup

# Variables
DATE=$(date +%Y%m%d)
LOG_FILE="/backup/${1}_backup.log"

# Create tar file and compress it
/bin/tar -cf /backup/$1.$DATE.tar $1 1> /dev/null 2>> $LOG_FILE
/bin/gzip -f /backup/$1.$DATE.tar

# Check if the backup was successful
if [ $? -eq 0 ]; then
	echo "$(date)  $1 $DATE backup have succeeded"  >> $LOG_FILE
else
	echo "$(date)  ERROR: failure $1 $DATE backup"  >> $LOG_FILE
fi
```

## 练习题: 读取用户输入字符并执行分支

编写一个 Shell 脚本，根据用户输入的字符输出不同的消息。具体要求如下：

### 具体要求：

1. 脚本应读取用户输入的单个字符。
2. 如果用户输入 'A'，则输出 "It is A."。
3. 如果用户输入 'B'，则输出 "It is B."。
4. 如果输入的既不是 'A' 也不是 'B'，则输出 "It is not A neither B." 并显示用法提示信息：
   - 提示格式为：`Usage ./script.sh {A|B}`
### 参考实现
```bash
#!/bin/sh
# 提示用户输入字符
echo "Please enter a character (A or B):"
read -r OPCHAR

# 检查是否输入为空
if [ -z "$OPCHAR" ]; then
    echo "No input provided. Please enter A or B."
    exit 1
fi

# 使用case语句进行判断
case $OPCHAR in
    A|a)  # 允许大写或小写输入
        echo "It is A."
    ;;
    B|b)  # 允许大写或小写输入
        echo "It is B."
    ;;
    *)
        echo "It is not A neither B."
        echo "Usage: $0 {A|B}"
    ;;
esac
```
## 练习题: 比较两个整数的大小

### 具体要求：

1. 编写一个 Shell 脚本，接受两个整数作为参数，并输出它们之间的关系：大于、等于或小于。
2. 如果传递的参数个数不足 2 个，脚本应提示并退出。
3. 如果传递的参数不是整数，脚本应提示并退出。
4. 使用 `if-elif-else` 语句比较两个参数，并根据它们的关系输出适当的信息。

### 示例输入与输出：

- 输入: `./intcom.sh 10 20`
  - 输出: `10 is lesser than 20`

- 输入: `./intcom.sh 30 30`
  - 输出: `30 is equal to 30`

- 输入: `./intcom.sh 50 10`
  - 输出: `50 is greater than 10`

### 提示：
- 使用 `[ ]` 来比较整数。
- 使用正则表达式验证输入是否为整数。

### 参考实现
```bash
#!/bin/sh
# Compare two input integers
# Usage: intcom.sh 10 20

if [ $# -ne 2 ]; then
    echo "Not enough parameters. Please provide two integers."
    exit 1
fi

# Validate if both inputs are integers
if ! [[ "$1" =~ ^-?[0-9]+$ ]] || ! [[ "$2" =~ ^-?[0-9]+$ ]]; then
    echo "Both arguments must be integers."
    exit 1
fi

if [ $1 -gt $2 ]; then
    echo "$1 is greater than $2"
elif [ $1 -eq $2 ]; then
    echo "$1 is equal to $2"
else
    echo "$1 is lesser than $2"
fi
```

## 练习题: 批量创建用户并为每个用户设置密码

### 具体要求：

1. 脚本使用一个基础用户名作为前缀，创建多个用户。用户名称格式为 `user1`、`user2` 等，直到 `user99`。
2. 每个用户的密码都设置默认密码 `abcd1234` + 用户名。
3. 使用 `chpasswd` 命令批量设置用户密码。
4. 脚本每创建一个用户并设置密码时，应该输出该用户名及密码。
5. 增加错误处理逻辑，在设置密码失败时输出错误信息并停止脚本执行。

### 提示：
- 使用 `while` 循环创建用户。
- 使用 `chpasswd` 命令批量设置用户密码。
- 使用 Shell 内置的算术运算符 `(( ))` 来增加用户编号。

### 参考实现
```bash
#!/bin/bash

USER_PREFIX="user"  # 基础用户名前缀
USER_NUMBER=1  # 初始用户编号
MAX_USERS=99  # 最大用户编号
DEFAULT_PASSWORD="abcd1234"  # 默认密码前缀

while (( USER_NUMBER <= MAX_USERS )); do  # 循环创建用户直到 user99
    USERNAME="${USER_PREFIX}${USER_NUMBER}"  # 生成用户名
    PASSWORD="${DEFAULT_PASSWORD}${USERNAME}"  # 生成密码
    useradd "$USERNAME"  # 创建用户
    if [[ $? -ne 0 ]]; then echo "Error: Failed to create user $USERNAME"; exit 1; fi  # 检查用户创建是否成功
    echo "$USERNAME:$PASSWORD" | chpasswd  # 设置用户密码
    if [[ $? -ne 0 ]]; then echo "Error: Failed to set password for user $USERNAME"; exit 1; fi  # 检查密码设置是否成功
    echo "Created user $USERNAME with password $PASSWORD"  # 输出用户名和密码
    (( USER_NUMBER++ ))  # 增加用户编号
done

echo "All users created successfully."  # 完成提示
```

## 练习题: 实现控制台动画效果

### 具体要求：

1. 编写一个 Shell 脚本，实现以下控制台动画效果：
   - 旋转指示器（显示 `-`、`\`、`|`、`/` 交替变化，模拟旋转）。
   - 百分比进度显示，从 `0%` 到 `100%`。
   - 使用 `#` 逐步填充的进度条。
   - 带百分比显示的进度条，进度从 `0%` 增长到 `100%`。

### 提示：
- 使用 `while` 和 `for` 循环来控制进度。
- 使用 `\033` ANSI 转义序列控制光标位置和输出样式。
- 使用 `sleep` 控制每次更新的时间间隔。

### 参考实现
```bash
#!/bin/bash
i=0
while [ $i -lt 10 ]
do
    for j in '-' '\\' '|' '/'
    do
        echo -ne "\033[1D$j"
        sleep 0.01
    done
    ((i++))
done


POS=25
echo -n "Doing ..."
for (( i=0; i<=100; i++ ))
do
       echo -en "\\033[${POS}G $i % completed"
       sleep 0.05
done
echo -ne "\n"

i=0
while [ $i -lt 200 ]
do
    ((i++))
    echo -ne "#"
    sleep 0.50000
done     
echo -ne "=>\n"


b=''
for ((i=0;$i<=100;i+=2))
do
    printf "progress:[%-50s]%d%%\r" $b $i
    sleep 0.1
 
    b=#$b
done
echo
```

## 练习题: 编写一个脚本来踢出特定用户并终止其进程

### 具体要求：
1. 编写一个 Shell 脚本，显示当前登录到系统的所有用户。
2. 显示每个用户的内存使用情况，并按照内存使用量排序。
3. 提示管理员输入要踢出的用户名，并显示该用户正在运行的所有进程。
4. 终止该用户的所有进程，并确认该用户是否还有进程在运行。
5. 防止误杀关键用户（如 root），增加确认步骤以避免误操作。

### 提示：
- 使用 `who` 命令获取登录的用户。
- 使用 `ps aux` 和 `awk` 来统计内存使用情况。
- 使用 `ps uU` 和 `kill` 来终止特定用户的进程。

### 参考实现
```bash
#!/bin/sh
# This script kicks off bad user

# Step 1: List all logged-in users
echo "Below user currently logged in to the system:"
ONLINEUSERS=`who | awk '{print $1}' | sort -u`
for ONLINEUSER in $ONLINEUSERS; do
    echo $ONLINEUSER
done

# Step 2: Display memory usage for each user
echo
echo "-------------------------------------"
echo "The current memory usage of each user (in KB):"
ps aux | awk 'NR!=1 {a[$1]+=$6;} END { for(i in a) printf "%-10s%-10skb\n", i, a[i]; }' | sort -n -k 2 -r

# Step 3: Get the user to kick out
echo
echo "-------------------------------------"
echo "Please input the user name we should kick (e.g., 'john'):"
read KICKUSER

# Prevent root from being kicked out
if [ "$KICKUSER" = "root" ]; then
    echo "You cannot kick out root!"
    exit 1
fi

# Step 4: List the user's processes
echo
echo "-------------------------------------"
echo "You have chosen to kick $KICKUSER"
echo "$KICKUSER is currently running the following processes:"
echo "-------------------------------------"
ps uU $KICKUSER | awk 'NR!=1 {print $2, $11, $12}'
echo "-------------------------------------"

# Step 5: Confirm kick-out action
echo "Are you sure you want to terminate all processes for $KICKUSER? (y/n)"
read CONFIRM
if [ "$CONFIRM" != "y" ]; then
    echo "Action cancelled."
    exit 1
fi

# Step 6: Kill all the user's processes
KICKUSERPIDS=`ps uU $KICKUSER | awk 'NR!=1 {print $2}'`
for KICKUSERPID in $KICKUSERPIDS; do
    echo "Killing process ID: $KICKUSERPID"
    /bin/kill -9 $KICKUSERPID 2> /dev/null
done

# Step 7: Verify if all processes are killed
echo "-------------------------------------"
echo "Checking if any processes are still running for $KICKUSER:"
ps uU $KICKUSER | awk 'NR!=1 {print $2, $11, $12}'
echo "-------------------------------------"
```

## 练习题: 使用 `expect` 自动化 SSH 登录并执行命令

### 具体要求：

1. 编写一个 `expect` 脚本，自动登录到远程服务器并执行命令。
2. 使用 `spawn` 启动 SSH 会话，并通过 `expect` 等待密码提示。
3. 在登录成功后，执行命令 `ls /data/` 列出 `/data/` 目录的内容。
4. 在执行命令后，退出 SSH 会话并返回退出代码。

### 提示：
- 使用 `expect` 处理交互式 SSH 登录。
- 通过 `send` 发送密码和命令。
- 使用 `expect` 等待输出的提示符。

### 参考实现
```bash
#!/usr/bin/expect

# 设置超时时间
set timeout 30

# 定义变量
set host "c97"
set user "root"
set password "root123"

# 启动 SSH 会话
spawn ssh $user@$host

# 等待密码提示并输入密码
expect "*assword:"
send "$password\n"

# 等待命令提示符并执行命令
expect "*#"
send "ls /data/\n"

# 再次等待命令提示符并退出
expect "*#"
send "exit\n"

# 退出 expect 脚本
exit 0
```