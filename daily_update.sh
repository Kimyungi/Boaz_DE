#!/bin/sh
echo "`date` cron run"
PATH=/var/www/flaskapp
python3=~/jsh/bin/python3
$python3 /var/www/flaskapp/helper/crawling.py
$python3 $PATH/app/__init__.py
