#!/bin/bash
yum update -y
yum -y install python37
yes Y | curl -O https://bootstrap.pypa.io/get-pip.py
yes | pip3 install flask
yes Y | curl -LJO https://raw.githubusercontent.com/OleksF/flask-basic/main/app.py
