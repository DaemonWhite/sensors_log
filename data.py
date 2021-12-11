import conf as ini

class Environement() :
    'This is Rectangle class' 
    launch = True


    if ini.verif():
        ini.create()
    else:
        ini.update("0.0.1a")

    ver = ini.load("VERSION", "version")

    def getDefault(self, options):
        self.value = ini.load("DEFAULT", options)
        return self.value

    def getVersion(self):
        return self.ver

    def setVersion(self, new):
        self.ver = new
        return self.ver