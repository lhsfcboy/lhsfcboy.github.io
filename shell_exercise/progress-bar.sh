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
