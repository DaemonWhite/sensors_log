#!/usr/bin/env python3
import asyncio

import conf as ini
import file
import pysense as senseHat

from packaging import version

async def main():
    version = "0.0.1"

    if ini.verif():
        ini.create()
    else:
        ini.update(version)

    file.verif()

    sleep = float(ini.load('DEFAULT', 'timestep'))
    sleep_Log = float(ini.load('DEFAULT', 'log_time'))
    sleep_Log_Time = sleep_Log

    print("Verification de la présence su senseHat")
    senseHat.test()

    print("senseHat detecter démarage")
    await asyncio.gather(senseHat.event(sleep), senseHat.log(sleep, sleep_Log, sleep_Log_Time))

asyncio.run(main())