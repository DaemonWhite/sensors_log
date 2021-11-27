#!/usr/bin/env python3
def format(type, value):
    data = type + " : " + str(value)
    return data

def writeFile(file, value):
    txt = open(file, "a")
    genTxt = value + "\n"
    txt.write(genTxt)
    txt.close()