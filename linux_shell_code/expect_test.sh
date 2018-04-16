#!/usr/bin/expect
set timeout 30
spawn ssh root@c97
expect "*assword:"
send "root123\n"
expect "*#"
send "ls /data/\n"
expect "*#"
send "exit\n"
exit 1
