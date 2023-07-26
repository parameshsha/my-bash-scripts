#!/bin/bash

ips=("172.31.28.23","172.31.18.167","172.31.27.216")
IFS=',' read -ra my_array <<< "$ips"
echo "print all ips : ${my_array[@]}"
echo "number of ips is : ${#my_array[@]}"
echo "frst ips : ${my_array[0]}"

for myip in ${my_array[@]}
    do
        echo $myip
        ssh -o StrictHostKeyChecking=no -i /tmp/key.pem ec2-user@$myip "hostname -i"
        scp -o StrictHostKeyChecking=no -i /tmp/key.pem /tmp/tomcat.sh ec2-user@$myip:/tmp/
        ssh -o StrictHostKeyChecking=no -i /tmp/key.pem ec2-user@$myip "ls -l /tmp/"
        ssh -o StrictHostKeyChecking=no -i /tmp/key.pem ec2-user@$myip "bash /tmp/tomcat.sh"
    done