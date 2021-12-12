import conf as ini

class Environement() :
    'This is Data class' 

    if ini.verif():
        ini.create()
    else:
        ini.update("0.0.1a")

    launchLog = ini.load("DEFAULT", "log_file", 2)
    launchEvent = ini.load("DEFAULT", "event_file", 2)

    ver = ini.load("VERSION", "version", 0)

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