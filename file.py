#!/usr/bin/env python3
import os

#verif is foleder exist
def verif():
    pathEvent = "event/"
    pathLog = "log/"

    isEvent = os.path.isdir(pathEvent)
    isLog = os.path.isdir(pathLog)

    if isEvent != True:
        os.makedirs(pathEvent)

    if isLog != True:
        os.makedirs(pathLog)

#Fomat data for log and event
def format(type, value):
    data = type + " : " + str(value)
    return data

#Create log or event file
def writeFile(file, value):
    txt = open(file, "a")
    genTxt = value + "\n"
    txt.write(genTxt)
    txt.close()

verif()