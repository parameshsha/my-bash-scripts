#!/bin/bash
echo "Number of elements passed to this script is :$#"
echo "Number of arguments passed to $0 is :$#"
echo "all provided arguments is :$@"
echo $1
echo $2
echo $3

number=$#
echo "Number of elements passed to this sript is :$number"
if [ $number == 3 ];then
echo "we are good to execute this script"
else 
echo "provided number is wrong, please provide 3 params only"
exit 1
fi
echo "some commands will be execute here"
hostname -i
free
unmae -a