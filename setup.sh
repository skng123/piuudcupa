#! /bin/bash

apt-get update
apt-get install mysql-server -y
mysqladmin --user=root password "root"
mysql -u root -e "create database piuudcupa_schema"
apt-get install python-is-python3 -y
apt-get install python3-pip -y
apt-get install python3-pymysql -y