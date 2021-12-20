#!/usr/bin/env python3
import interface as guiTer
import os

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

    return 1


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