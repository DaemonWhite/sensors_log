#!/usr/bin/python3
import asyncio

import file
import interface as guiTer

import pysense as senseHat

from data import Environement
from kill import GracefulKiller

async def start(env):
    restart= True

    while restart:
        try:
            if env.termEnable:
                retFunc = await asyncio.gather(senseHat.event(env), senseHat.log(env), guiTer.guiMain(env))
            else:
                retFunc = await asyncio.gather(senseHat.event(env), senseHat.log(env))
        except BaseException:
            guiTer.syntaxTermLog(1, "Fermeture du programme extérieure ou plantage")
        restart = retFunc[2]
        print(retFunc[2])

        if restart == True: 
            guiTer.syntaxTermLog(0, "Redémarrage...")



async def main(env):
    file.verif(env.path)

    print(env.path)

    guiTer.syntaxTermLog(0, "Vérification de la présence du senseHat")
    senseHat.test(env)
    guiTer.syntaxTermLog(0, "senseHat détecter démarrage")

    try:
        await asyncio.gather(killFunction(env),start(env))
    except  BaseException:
        guiTer.syntaxTermLog(1, "Fermeture du programme extérieure ou plantage")
    


    

async def killFunction(kenv):
    killer = GracefulKiller()
    noKill=True

    while noKill:
        await asyncio.sleep(1)
        if (killer.kill_now):
            noKill=False
        elif (kenv.termEnable == False) and (kenv.launchLog == False) and (kenv.launchEvent == False):
            noKill=False

    kenv.launchLog = False
    kenv.launchEvent = False
    kenv.termEnable = False

    await asyncio.sleep(1)

    guiTer.syntaxTermLog(0, "Fermeture du programme")
    exit()

    

if __name__ == '__main__':
    enve = Environement()
    asyncio.run(main(enve))

   