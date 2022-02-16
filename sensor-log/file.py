#!/usr/bin/python3
import interface as guiTer
import os
import csv

#verif is foleder exist

def verif(path):
    if path == os.getcwd() or path == os.getcwd() + "/":
        guiTer.syntaxTermLog(1, "Chemin par default et utiliser : " + path)
    else:
        guiTer.syntaxTermLog(0, "Chemin des sorties : " + path)

    pathEvent = path + "/event/"
    pathLog = path + "/log/"

    isEvent = os.path.isdir(pathEvent)
    isLog = os.path.isdir(pathLog)

    if isEvent != True:
        os.makedirs(pathEvent)
        guiTer.syntaxTermLog(0, "Dossier Event créer")

    if isLog != True:
        os.makedirs(pathLog)
        guiTer.syntaxTermLog(0, "Dossier Log créer")



#Fomat data for log and event
def format(type, value):
    data = type + " : " + str(value)
    return data

#Create log or event file
def writeFile(file, value):
    header = ['Heure','humid','presure','temp','orientation x','orientation y','orientation z','accel x','accel y','accel z']
    ise = os.path.isfile(file)

    with open(file, 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        if ise != True:
            writer.writerow(header)
        writer.writerow(value)