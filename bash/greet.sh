#!/bin/zsh

user=$(whoami)
date=$(date)
whereami=$(pwd)
publicipaddress=$(curl -s ifconfig.me | tac | tac | tr -d '%')
privateipaddress=$(hostname -I)

city="YOUR CITY NAME"
weather=$(curl -s wttr.in/${city} | tac | tac | head -7 | tail -6)

h=$(date +"%H")
if [ $h -gt 6 -a $h -le 12 ]
then
echo "Good morning, sir. Shall we begin?"
elif [ $h -gt 12 -a $h -le 16 ]
then 
echo "Afternoon sir, your assistant is reporting for duty"
elif [ $h -gt 16 -a $h -le 19 ]
then
echo "A bit late for work, isn't it?"
else
echo "7 hours of sleep is essential. Perhaps you should call it an early night"
fi

echo ""
echo "You are currently logged in as $user and in the directory $whereami"
echo "Today is $date"
echo "Your public IP Address is $publicipaddress and your private ip address is $privateipaddress"
echo "The weather in ${(C)city} right now is"
echo $weather
