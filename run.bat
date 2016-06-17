@echo off
cd D:/nginx
start nginx.exe
cd D:/netmaster
python manage.py runfcgi method=threaded host=127.0.0.1 port=8051
