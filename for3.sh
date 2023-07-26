#!/bin/bash

for num in {1..100}
do
if [ $(( $num%5)) == 0 ];
then
echo "the multiple by 5 is : $num"
fi
done