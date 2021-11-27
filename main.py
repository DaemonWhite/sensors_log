import asyncio

import conf as ini
import pysense as senseHatater

async def main():

    ini.create()
    sleep = float(ini.load('DEFAULT', 'timestep'))
    sleep_Log = float(ini.load('DEFAULT', 'log_time'))
    sleep_Log_Time = sleep_Log

    

    print(sleep_Log)
    senseHatater.test()

    
    await asyncio.gather(senseHatater.event(sleep), senseHatater.log(sleep, sleep_Log, sleep_Log_Time))

asyncio.run(main())