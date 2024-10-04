## less

https://linux.die.net/man/1/less
https://ss64.com/bash/less.html

### 参数 OPTIONS
-i
-e
-n, 加速跳转到文件底部
-f, 强制打开, 避免系统提示是否打开文件

### 命令 Commands

### 实例
less -in

## grep

### 常用参数
-v or --invert-match
-i or --ignore-case, 当字符串不包含大写字母时, 搜索忽略大小写
--color=always
-n, 显示行号
-r, 指定目标为文件夹时, 搜索结果显示文件名
### GNU Only
-P or --perl-regexp, PCRE-enabled grep, to use advanced function of regexp, e.g. negative lookahead

-B num to set how many lines before the match and 
-A num for the number of lines after the match.
-C num same number of lines before and after

### 实例
grep -i --color=always
