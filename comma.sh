#!/bin/bash

ips=("10.0.0.0","10.0.0.1","10.0.0.2")
IFS=',' read -ra values <<< "$ips"
echo "print all ips : ${values[@]}"
echo "number of ips is : ${#values[@]}"
echo "frst ips : ${values[0]}"
