#!/bin/sh

APA_STA=`pgrep httpd`
if [ "$APA_STA" != "" ]
then
	echo "Apache2 is running!"
else
	echo "Apache2 not running! help!"
fi	
