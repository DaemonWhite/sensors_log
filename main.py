#!/usr/bin/env python3
import asyncio

import conf as ini
import file
import pysense as senseHat

async def main():


    file.verif()
    ini.create()
    
    sleep = float(ini.load('DEFAULT', 'timestep'))
    sleep_Log = float(ini.load('DEFAULT', 'log_time'))
    sleep_Log_Time = sleep_Log

    senseHat.test()

    
    await asyncio.gather(senseHat.event(sleep), senseHat.log(sleep, sleep_Log, sleep_Log_Time))

asyncio.run(main())