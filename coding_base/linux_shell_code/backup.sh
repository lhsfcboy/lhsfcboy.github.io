#!/bin/sh
#backup files specified by first arg

DATE=`/bin/date +%Y%m%d`
/bin/tar -cf /backup$1.$DATE.tar $1 1> /dev/null 2>> /backup/$1.bak.log
/bin/gzip -f  /backup/$1.$DATE.tar

if [ $? -eq 0 ]; then
	echo "`date`  $1 $DATE backup have sucessed"  >> /backup/$1.bak.log
else
	echo "`date`  ERROR: failure $1 $DATE backup"  >> /backup/$1.bak.log
fi	

