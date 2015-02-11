
SUM=0
while [ $# -ne 0 ]
do
	SUM=`expr $SUM + $1`
	shift
done


echo $SUM
