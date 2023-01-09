#!/bin/sh
echo "Installing dependencies for the project..."
pip install -r requirements.txt
echo "Starting application... Go to >> http://127.0.0.1:8000/"
python ./crowdsourcing/manage.py runserver