#!/bin/bash

n=0

while [ $n -le 1 ]
do

    echo "Select an option from below:
    1) Hello World!
    2) Ping Self
    3) IP Info
    4) Exit"

    read input

    if [ $input = 1 ]
    then
        echo "Hello World!"
    elif [ $input = 2 ]
    then
        ping -c 3 192.168.68.75
    elif [ $input = 3 ]
    then
        ip a
    elif [ $input = 4 ]
    then
        echo "Goodbye!"
        ((n++))
        exit
    else
        echo "Invalid input, please try again!"
    fi
done