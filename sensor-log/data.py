#!/usr/bin/python3
import conf as ini
from tui import ui

class Environement() :
    'This is Data class'
    def __init__(self, term=True):

        self.uiLog = ui(term)

        self.uiLog.syntaxLog(0, "coucou")
        self.version="0.0.1a"

        if ini.verif():
            ini.create()
        else:
            ini.update(self.version)

        self.path = ini.load("ENVIRONEMENT", "path", 0)
        self.launchLog = ini.load("ENVIRONEMENT", "log_file", 2)
        self.launchEvent = ini.load("ENVIRONEMENT", "event_file", 2)
        self.termEnable = ini.load("ENVIRONEMENT", "term", 2)

        self.ver = ini.load("VERSION", "version", 0)

    def getSensors(self, options):
        self.value = ini.load("SENSORS", options, 2)

        return self.value

    def getTime(self, options):
        self.value = ini.load("TIME", options, 1)
        return self.value

    def getEnv(self, options):
        self.value = ini.load("ENVIRONEMENT", options, 0)
        return self.value

    def getVersion(self):
        return self.ver

    def setVersion(self, new):
        self.ver = new
        return self.ver