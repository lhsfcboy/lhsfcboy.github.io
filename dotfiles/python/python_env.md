# 搭建Python开发环境

### 设置提示符样式

```console
$ cat ~/.virtualenvs/postactivate
#!/bin/bash
# This hook is sourced after every virtualenv is activated.

PS1="\[\e[1;33;45m\](`basename \"$VIRTUAL_ENV\"`)\[\e[0m\]$_OLD_VIRTUAL_PS1"
```
