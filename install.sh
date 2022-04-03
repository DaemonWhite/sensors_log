#!/bin/bash
sudo apt install python3
sudo apt install python3-pip

inInstall=$(pwd)
outInstall=$HOME/Projet/sensor-log

mkdir -p $outInstall
cp $inInstall/sensor-log/* $outInstall

sudo pip3 install -r $inInstall/requirements.txt
pip3 install -r $inInstall/requirements.txt

sudo cp $inInstall/sensor.service /etc/systemd/system/
sudo systemctl start sensor
sudo systemctl enable sensor
sudo systemctl daemon-reload
