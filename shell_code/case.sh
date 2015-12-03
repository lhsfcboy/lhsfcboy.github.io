

read OPCHAR

case $OPCHAR in
	A)
		echo "It is A."
	;;
	B)
		echo "It is B."
	;;
	*)
		echo "It is not A neither B."
		echo "Usage $0 {A|B}"
	;;
esac

