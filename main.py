#!/usr/bin/env python3

import conf as ini
import asyncio

import file
import pysense as senseHat

from data import Environement

env = Environement()

async def main():

    test = input("La valeur de ta maison?")

    file.verif()

    print("Verification de la présence su senseHat")
    senseHat.test()

    print("senseHat detecter démarage")
    await asyncio.gather(senseHat.event(env), senseHat.log(env))

asyncio.run(main())