#!/usr/bin/env python3
import asyncio

import file
import interface as guiTer

import pysense as senseHat

from data import Environement

env = Environement()

async def main():

    restart= True

    file.verif(env.path)

    guiTer.syntaxTermLog(0, "Verification de la présence su senseHat")
    senseHat.test(env)
    guiTer.syntaxTermLog(0, "senseHat detecter démarage")

    while restart:
        retFunc = await asyncio.gather(senseHat.event(env), senseHat.log(env), guiTer.guiMain(env))
        restart = retFunc[2]

        if restart == True: 
            guiTer.syntaxTermLog(0, "Redemarage...")

    guiTer.syntaxTermLog(0, "Fermeture du programe")
    exit()

asyncio.run(main())