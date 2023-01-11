#!/bin/sh
echo "Installing dependencies for the project..."
pip install -r requirements.txt
if [ -z "$1"] 
    then 
        echo "\nStarting application in default port 8000... Go to >> http://127.0.0.1:8000/ \n"
        python ./crowdsourcing/manage.py runserver
    else
        echo "\nStarting application in port $1... Go to >> http://127.0.0.1:$1/ \n"
        python ./crowdsourcing/manage.py runserver $1
fi