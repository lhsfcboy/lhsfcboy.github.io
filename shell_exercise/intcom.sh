#!/bin/sh
#compare the input integer
#run like intcom.sh 10 20

if test $# -ne 2;then
    echo "Not enough parameters"
    exit 0
fi

if test $1 -gt $2
    then 
    echo "$1 is grater then $2"
elif test $1 -eq $2
    then 
    echo "$1 is equal then $2"
else
    echo "$1 is lesser then $2"
fi
