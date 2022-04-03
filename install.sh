#!/bin/bash
sudo apt install python3
sudo apt install python3-pip

inInstall=$(pwd)
outInstall=$home/Projet/sensor-log

mkdir -p outInstall
cp $inInstall/sensor-log/* $outInstall

sudo pip3 install -R requirements.txt
pip3 install requirements.txt

sudo cp $inInstall/sensor.service /etc/systemd/system/
sudo systemctl start sensor
sudo systemctl enable sensor