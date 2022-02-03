#!/bin/bash
yum update -y
yum install python37
curl -O https://bootstrap.pypa.io/get-pip.py
pip3 install flask
curl -LJO https://raw.githubusercontent.com/OleksF/flask-basic/main/app.py
