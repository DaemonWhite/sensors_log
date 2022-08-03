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
            env.uiLog.syntaxLog(1, "Fermeture du programme par l'extérieur ou plantage du processus")
        restart = retFunc[2]
        print(retFunc[2])

        if restart == True: 
            env.uiLog.syntaxLog(0, "Redémarrage...")
            env.termEnable=True

async def main(env):
    file.verif(env.path)

    env.uiLog.syntaxLog(0, "Verification de la présence du senseHat ...")
    senseHat.test(env)
    env.uiLog.syntaxLog(0, "Sense Hat détecté. Démarrage en cours...")

    try:
        await asyncio.gather(killFunction(env),start(env))
    except  BaseException:
        env.uiLog.syntaxLog(1, "1 Fermeture du programme par l'extérieur ou plantage du processus")
    

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

    kenv.uiLog.syntaxLog(0, "Fermeture du programme")
    

    

if __name__ == '__main__':
    enve = Environement()
    asyncio.run(main(enve))
    exit()

   