#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.read("conf.ini")

def create():
    
    config['DEFAULT'] = {'log': 'true', 'log_time' : '300.0','event': 'true', 'timeStep' : '0.5'}
    config['SENSORS'] = {'humid': 'true', 'presure': 'true', 'temp': 'false', 'orientation' : 'true', 'Accel' : 'false'}

    with open('conf.ini', 'w') as configfile:
        config.write(configfile)

def load(OPTION, data):
    value = config.get(OPTION, data)
    
    return value

def modify():
    config.set('DEFAULT','log', 'false')

    with open('conf.ini', 'w') as configfile:
        config.write(configfile)
