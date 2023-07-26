#!/bin/bash
echo -n " please give a number : "
read num
 if [ $(($num%2)) == 0 ] ;then
 echo "$num is even number"
 else
 echo "$num is odd number"
 fi