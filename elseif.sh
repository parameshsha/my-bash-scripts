#!/bin/bash
echo -n "please add your age : "
read age
echo "you provided age number is : $age"
if [ $age -le 16 ];then
echo "child"
elif [[ $age -ge 17 ]] && [[ $age -le 30 ]];then
echo "young adults"
elif [[ $age -ge 31 ]] && [[ $age -le 45 ]] ;then
echo "middle aged"
else
echo "others"
fi