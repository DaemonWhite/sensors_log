#!/usr/bin/env python3
from sense_emu import SenseHat
import time
import datetime
import asyncio

import file

# defineSense
sense = SenseHat()

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
def test(env):
    #Define Colors

    sense.set_imu_config(True, True, True)

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
async def event(env):
    repEvent = env.path + "/event/event.txt"

    stopTime = env.getTime("event_step")

    while env.launchEvent:
        #file.writeFile(repEvent, "ok")
        await asyncio.sleep(stopTime)

#Log isWorkig but functional
async def log(env):

    stopTime = env.getTime("log_step")
    sleep = env.getTime("log_time")
    sleepTime = sleep

    isHumidity = env.getSensors('humid')
    isPressure =  env.getSensors('presure')
    isOrientation = env.getSensors('orientation')
    #compas
    isAccel = env.getSensors('accel')
    isTemp = env.getSensors('temp')
    
    while env.launchLog:

        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        orientation = sense.get_orientation_degrees()
        #compas = sense.get_compass() Disable Gyroscope et magnetometre pour fonctioner
        accel_only = sense.get_accelerometer_raw()
        temp = sense.get_temperature_from_pressure()

        tempon = "Error"

        sendTabl = []

        h = hours()
    
        if sleepTime >= sleep:
            repLog = env.path + "/log/"
            repLog += h
            repLog += ".csv"
            sleepTime = 0.0
    
        else:
            sleepTime += stopTime

        sendTabl.append(h)

        if isHumidity:
            #file.writeFile(repLog,  file.format("humidity", humidity))
            sendTabl.append(humidity)
        if isPressure:
           #file.writeFile(repLog, file.format("pressure", pressure))
           sendTabl.append(pressure)
        if isTemp:
            #file.writeFile(repLog, file.format("temp", temp))
            sendTabl.append(temp)
        if isOrientation:
            #file.writeFile(repLog, file.format("orientation", orientation))
            tempon = "{pitch}".format(**orientation)
            sendTabl.append(tempon)
            tempon = "{roll}".format(**orientation)
            sendTabl.append(tempon)
            tempon = "{yaw}".format(**orientation)
            sendTabl.append(tempon)
        if isAccel:
            #file.writeFile(repLog, file.format("accel", accel_only))
            tempon = accel_only['x']
            sendTabl.append(tempon)
            tempon = accel_only['y']
            sendTabl.append(tempon)
            tempon = accel_only['z']
            sendTabl.append(tempon)
              

        file.writeFile(repLog, sendTabl)

        await asyncio.sleep(stopTime)
