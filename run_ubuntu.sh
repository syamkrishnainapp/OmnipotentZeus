#!/bin/bash

apt-add-repository multiverse
apt-get update
apt-get install build-essential
apt-get install wget python-pip mysql-server libmysqlclient-dev libaio1 python-dev python-lxml --yes
pip install mysql-python
pip install sqlalchemy
mysql -u root -e "create database omnipotentzeuslinux; create user 'testuser' identified by 'TestUser'; grant all privileges on omnipotentzeuslinux.* to 'testuser'@'%' identified by 'TestUser'; flush privileges;"
#screen python hermes.py
