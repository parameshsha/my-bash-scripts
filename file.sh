#!/bin/bash
file=$1

if [ -d $file ] ;then
echo "folder already exist"
else
echo "folder does not exit,we can creat here"
mkdir $file
fi

