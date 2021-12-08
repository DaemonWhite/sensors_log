#!/usr/bin/env python3
from sense_emu import SenseHat
import time
import datetime
import asyncio

import conf as ini
import file


# defineSense
sense = SenseHat()

def loadConf(data):

    value = True
    load = ini.load('SENSORS', data)

    if load == "false" :
        value = False
    elif load != "false" and load != "true":
        print("Error donner du ini incorecte la valeur", data,"prendra sera par défaut activer")

    return value;

#Fomat hours 
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

#Test present sense hat
def test():
    #Define Colors
    noColors = (0, 0, 0)
    red = (255, 0, 0)

    #Define of colors pixel x pixel 'Ok message'
    defineColors =  [
    noColors, red, noColors, noColors, red, noColors, red, noColors,
    red, noColors, red, noColors, red, red, noColors, noColors,
    red, noColors, red, noColors, red, noColors, red, noColors,
    noColors, red, noColors, noColors, noColors, noColors, noColors, noColors,
    noColors, noColors, noColors, noColors, noColors, noColors, noColors, noColors,
    noColors, noColors, noColors, noColors, noColors, noColors, noColors, noColors,
    noColors, noColors, noColors, noColors, noColors, noColors, noColors, noColors,
    noColors, noColors, noColors, noColors, noColors, noColors, noColors, noColors,
    ]
    # set colors pi sense
    sense.set_pixels(defineColors)

    time.sleep(0.5)

    #Define of colors pixel x pixel
    defineColors =  [noColors for i in range(64)]

    # set colors pi sense
    sense.set_pixels(defineColors)

#Event isWokining
async def event(stopTime):
    repEvent = "event/event.txt"

    while True:
        file.writeFile(repEvent, "ok")
        await asyncio.sleep(stopTime)

#Log isWorkig but functional
async def log(stopTime, sleep, sleepTime):

    isHumidity = loadConf('humid')
    isPressure =  loadConf('presure')
    isOrientation = loadConf('orientation')
    #compas
    #accel_only
    isTemp = loadConf('temp')
    
    while True:

        humidity = sense.humidity
        pressure = sense.get_pressure()
        orientation = sense.get_orientation_degrees()
        compas = sense.get_compass_raw()
        accel_only = sense.get_accelerometer()
        temp = sense.temp
        

        h = hours()
    
        if sleepTime >= sleep:
            repLog = "log/"
            repLog += h
            repLog += ".log"
            sleepTime = 0.0
    
        else:
            sleepTime += stopTime

        file.writeFile(repLog, h)
        if isHumidity:
            file.writeFile(repLog,  file.format("humidity", humidity))
        if isPressure:
            file.writeFile(repLog, file.format("pressure", pressure))
        if isOrientation:
            file.writeFile(repLog, file.format("orientation", orientation))
        file.writeFile(repLog, file.format("compas", compas))
        file.writeFile(repLog, file.format("accel", accel_only))
        if isTemp:
            file.writeFile(repLog, file.format("temp", temp))

        await asyncio.sleep(stopTime)
