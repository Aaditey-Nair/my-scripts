#!/bin/zsh

user=$(whoami)
date=$(date)
whereami=$(pwd)
publicipaddress=$(curl -s ifconfig.me | tac | tac | tr -d '%')
privateipaddress=$(hostname -I)
weather=$(curl -s wttr.in | tac | tac | head -7)

echo "Hello $user"
echo ""
echo "You are currently logged in as $user and in the directory $whereami"
echo "Today is $date"
echo "Your public IP Address is $publicipaddress and your private ip address is $privateipaddress"
echo ""
echo $weather
