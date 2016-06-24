#!/bin/sh
/usr/bin/python3 /root/wikibirthdays/get_birthdays.py
cp birthdays.html /var/www/rails/public
