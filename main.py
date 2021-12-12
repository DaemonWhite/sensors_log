#!/usr/bin/env python3
import asyncio

import file
import interface as guiTer

import pysense as senseHat

from data import Environement

env = Environement()

async def main():

    file.verif()

    print("Verification de la présence su senseHat")
    senseHat.test()

    print("senseHat detecter démarage")
    await asyncio.gather(senseHat.event(env), senseHat.log(env), guiTer.guiMain(env))

    print("Fermeture du programe")
    exit()

asyncio.run(main())