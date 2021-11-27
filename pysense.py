from sense_emu import SenseHat
import time
import datetime
import asyncio

import file

# defineSense
sense = SenseHat()

def hours():
    defineDate = datetime.datetime.now()

    retHours ="["

    retHours += str(defineDate.year)
    retHours += "-"
    retHours += str(defineDate.month)
    retHours += "-"
    retHours += str(defineDate.day)
    retHours += "_"
    retHours += str(defineDate.hour)
    retHours += "h"
    retHours += str(defineDate.minute)
    retHours += "m"
    retHours += str(defineDate.second)
    retHours += "s]"

    return retHours


def test():
    #off colors
    colors = (0, 0, 0)
    red = (255, 0, 0)

    #Define of colors pixel x pixel
    defineColors =  [
    colors, red, colors, colors, red, colors, red, colors,
    red, colors, red, colors, red, red, colors, colors,
    red, colors, red, colors, red, colors, red, colors,
    colors, red, colors, colors, colors, colors, colors, colors,
    colors, colors, colors, colors, colors, colors, colors, colors,
    colors, colors, colors, colors, colors, colors, colors, colors,
    colors, colors, colors, colors, colors, colors, colors, colors,
    colors, colors, colors, colors, colors, colors, colors, colors,
    ]

    # set colors pi sense
    sense.set_pixels(defineColors)

    time.sleep(0.5)



    #Define of colors pixel x pixel
    defineColors =  [colors for i in range(64)]

    # set colors pi sense
    sense.set_pixels(defineColors)

async def event(stopTime):
    repEvent = "event/event.txt"

    while True:
        file.writeFile(repEvent, "ok")
        await asyncio.sleep(0.5)

async def log(stopTime, sleep, sleepTime):

    humidity = sense.humidity
    pressure = sense.get_pressure()
    orientation = sense.get_orientation_degrees()
    compas = sense.get_compass_raw()
    accel_only = sense.get_accelerometer()
    temp = sense.temp
    
    while True:
        

        h = hours()

        print(h)
    
        if sleepTime >= sleep:
            repLog = "log/"
            repLog += h
            repLog += ".log"
            sleepTime = 0.0
    
        else:
    
            sleepTime += stopTime
        
        print(sleepTime)

        file.writeFile(repLog, h)
        file.writeFile(repLog,  file.format("humidity", humidity))
        file.writeFile(repLog,  file.format("pressure", pressure))
        file.writeFile(repLog,  file.format("orientation", orientation))
        file.writeFile(repLog,  file.format("compas", compas))
        file.writeFile(repLog,  file.format("accel", accel_only))
        file.writeFile(repLog,  file.format("temp", temp))

        await asyncio.sleep(stopTime)