#!/usr/bin/env python3
import os

def verif():
    pathEvent = "event/"
    pathLog = "log/"

    isEvent = os.path.isdir(pathEvent)
    isLog = os.path.isdir(pathLog)

    if isEvent != True:
        os.makedirs(pathEvent)

    if isLog != True:
        os.makedirs(pathLog)

def format(type, value):
    data = type + " : " + str(value)
    return data

def writeFile(file, value):
    txt = open(file, "a")
    genTxt = value + "\n"
    txt.write(genTxt)
    txt.close()