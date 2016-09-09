#!/usr/bin/expect
set timeout 30



spawn telnet localhost 62001
expect ">"
send "ha_primary\n"
#send "exit\n"
expect ">"




spawn telnet localhost 62002
expect ">"
send "ha_primary\n"
#send "exit\n"
expect ">"







spawn telnet localhost 62003
expect ">"
send "ha_primary\n"
#send "exit\n"
expect ">"

