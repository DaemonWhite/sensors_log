#!/usr/bin/env python3
from packaging.version import Version, parse

import configparser
import os

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
    
    #config['DEFAULT'] = {'log': 'true', 'log_time' : '300.0','event': 'true', 'timeStep' : '0.5'}
    config['DEFAULT'] = {'term': True, 'path': '',
        'log_file': 'true',
        'log_view': 'false',
        'event_file': 'true',
        'event_log': 'false',
        'log_time': '300.0',
        'log_step': '0.5',
        'event_step': '0.1'}
    config['SENSORS'] = {'humid': 'true', 'presure': 'true', 'temp': 'false', 'orientation' : 'true', 'Accel' : 'false'}
    config['VERSION'] = {'version': '0.0.1a'}

    with open('conf.ini', 'w') as configfile:
        config.write(configfile)

    print("Fichier de configuraton créer")

def load(OPTION, data):
    value = config.get(OPTION, data)
    
    return value

def modify():
    config.set('DEFAULT','log', 'false')

    with open('conf.ini', 'w') as configfile:
        config.write(configfile)

def update(version):
    actual = Version(version)

    v001a = parse("0.0.1a")