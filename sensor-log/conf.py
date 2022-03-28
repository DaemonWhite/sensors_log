#!/usr/bin/python3
from packaging.version import Version, parse

import interface as guiTer
import configparser
import os
import csv

config = configparser.ConfigParser()
config.read("conf.ini")

def verif():
    pathConf = "conf.ini"
    value = True

    isConf = os.path.isfile(pathConf)

    if isConf:
        value = False
    
    return value

def create():
    pwd = os.getcwd()
    
    #config['DEFAULT'] = {'log': 'true', 'log_time' : '300.0','event': 'true', 'timeStep' : '0.5'}
    config['ENVIRONEMENT'] = {
        'term': 'true', 
        'path': pwd,
        'log_file': 'true',
        'log_view': 'false',
        'event_file': 'true',
        'event_log': 'false'
        }

    config['TIME'] = {
        'log_time': '300.0',
        'log_step': '0.5',
        'event_step': '0.1'
        }

    config['SENSORS'] = {
        'humid': 'true',
        'presure': 'true',
        'temp': 'true',
        'orientation' : 'true',
        'Accel' : 'false'}

    config['VERSION'] = {'version': '0.0.1a'}

    with open('conf.ini', 'w') as configfile:
        config.write(configfile)

    guiTer.syntaxTermLog(0, "Fichier de configuration créer")

def load(OPTION, data, typeData):
    #typeData 0 = str
    #typeData 1 = float
    #typeData 2 = booleen

    load = config.get(OPTION, data)

    if typeData == 1:
        value = float(load)

    elif typeData == 2:
        value = True

        if load == "false" :
            value = False
        elif load != "false" and load != "true":
            guiTer.syntaxTermLog(2, "Erreur donnée du ini incorrecte la valeur", data,"prendra sera par défaut activé")
    else: 
        value = load


    
    return value

def modify(OPTION, data, value):
    config.set(OPTION, data, value)

    with open('conf.ini', 'w') as configfile:
        config.write(configfile)

def update(version):
    actual = Version(version)

    v001a = parse("0.0.1a")