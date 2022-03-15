#!/usr/bin/python3
import asyncio

import file
import interface as guiTer

import pysense as senseHat

from data import Environement
from kill import GracefulKiller



async def main(env):

    restart= True

    file.verif(env.path)

    print(env.path)

    guiTer.syntaxTermLog(0, "Verification de la présence su senseHat")
    senseHat.test(env)
    guiTer.syntaxTermLog(0, "senseHat detecter démarage")

    while restart:
        retFunc = await asyncio.gather(killFunction(env), senseHat.event(env), senseHat.log(env), guiTer.guiMain(env))
        restart = retFunc[2]

        print(restart)

        if restart == True: 
            guiTer.syntaxTermLog(0, "Redemarage...")

async def killFunction(kenv):
    killer = GracefulKiller()

    while not (killer.kill_now) or (kenv.termEnable == False) or (kenv.launchLog == False) or (kenv.launchEvent == False):
        await asyncio.sleep(1)

    kenv.launchLog = False
    kenv.launchEvent = False
    kenv.termEnable = False

    guiTer.syntaxTermLog(0, "\nFermeture du programe")

    exit()

if __name__ == '__main__':
    enve = Environement()
    asyncio.run(main(enve))