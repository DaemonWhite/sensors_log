#!/usr/bin/env python3
import asyncio

import file
import interface as guiTer

import pysense as senseHat

from data import Environement

env = Environement()

async def main():

    restart= True

    file.verif()

    print("Verification de la présence su senseHat")
    senseHat.test()

    print("senseHat detecter démarage")

    while restart:
        retFunc = await asyncio.gather(senseHat.event(env), senseHat.log(env), guiTer.guiMain(env))
        print(retFunc[2])
        restart = retFunc[2]

        if restart == True: 
            print("Redemarage...")

    print("Fermeture du programe")
    exit()

asyncio.run(main())