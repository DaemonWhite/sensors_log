import time
import datetime
import conf as ini

from sense_emu import SenseHat

event = open("event/test.txt", "a")
# defineSense
sense = SenseHat()

def format(type, value):
    data = type + " : " + str(value)
    return data

def writeFile(file, value):
    txt = open(file, "a")
    genTxt = value + "\n"
    txt.write(genTxt)
    txt.close()

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


def main():

    ini.create()
    sleep = float(ini.load('DEFAULT', 'timestep'))
    sleep_Log = float(ini.load('DEFAULT', 'log_time'))
    sleep_Log_Time = sleep_Log

    humidity = sense.humidity
    pressure = sense.get_pressure()
    orientation = sense.get_orientation_degrees()
    compas = sense.get_compass_raw()
    accel_only = sense.get_accelerometer()
    temp = sense.temp

    print(sleep_Log)
    test()

    #off colors
    colors = (0, 0, 0)

    #Define of colors pixel x pixel
    defineColors =  [colors for i in range(64)]

    # set colors pi sense
    sense.set_pixels(defineColors)

    while True:
        

        h = hours()

        if sleep_Log_Time >= sleep_Log:
            repLog = "log/"
            repLog += h
            repLog += ".log"
            sleep_Log_Time = 0.0

        else:
            sleep_Log_Time += sleep


        writeFile(repLog, h)
        writeFile(repLog,  format("humidity", humidity))
        writeFile(repLog,  format("pressure", pressure))
        writeFile(repLog,  format("orientation", orientation))
        writeFile(repLog,  format("compas", compas))
        writeFile(repLog,  format("accel", accel_only))
        writeFile(repLog,  format("temp", temp))

        #Time stop
        time.sleep(sleep)

main()