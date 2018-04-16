#!/bin/sh
#This script kick off bad user

echo "Below user currently logged in to system"
ONLINEUSERS=`who  | awk '{print $1}'|sort -u`
for ONLINEUSER in $ONLINEUSERS
do
 echo $ONLINEUSER
done


echo
echo "-------------------------------------"
echo "The current memory usage of each user"
ps aux | awk 'NR!=1{a[$1]+=$6;} END { for(i in a) printf"%-10s%-10skb\n",i, a[i];}'|sort -n -k 2 -r


echo
echo "-------------------------------------"
echo "Please input the user name we should kick"
read KICKUSER

echo
echo "-------------------------------------"
echo "Ok, so you dont like $KICKUSER"
echo "$KICKUSER nwo is running below process"
echo "-------------------------------------"
ps uU $KICKUSER|awk 'NR!=1 {print $11,$12}'
echo "-------------------------------------"
echo "Anyway, lets kick $KICKUSER"


KICKUSERPIDS=`ps uU $KICKUSER|awk 'NR!=1 {print $2}'`
for KICKUSERPID in $KICKUSERPIDS
do
 /bin/kill -9 $KICKUSERPID 2> /dev/null
done


echo "-------------------------------------"
echo "$KICKUSER nwo is running below process"
echo "-------------------------------------"
ps uU $KICKUSER|awk 'NR!=1 {print $11,$12}'
echo "-------------------------------------"



