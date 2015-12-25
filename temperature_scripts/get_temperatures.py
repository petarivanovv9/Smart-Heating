import os
import glob
import time


def get_temperatures_sensors():
    temperatures = []

    # find the path of a sensor directory that starts with 28
    devicelist = glob.glob('/sys/bus/w1/devices/28*')

    # append the device file name to get the absolute path of the sensor
    devicefile_1 = devicelist[0] + '/w1_slave'
    # devicefile_2 = devicelist[1] + '/w1_slave'

    # sensor 1
    # open the file representing the sensor.
    fileobj_1 = open(devicefile_1, 'r')
    lines_1 = fileobj_1.readlines()
    fileobj_1.close()

    temperature_1 = int(lines_1[1].split(" ")[9].split("=")[1]) / 1000.0

    # sensor 2
    # open the file representing the sensor.
    # fileobj_2 = open(devicefile_2, 'r')
    # lines_2 = fileobj_2.readlines()
    # fileobj_2.close()

    # temperature_2 = int(lines_2[1].split(" ")[9].split("=")[1]) / 1000.0

    temperatures.append(temperature_1)
    # temperatures.append(temperature_2)

    return temperatures


# load the kernel modules needed to handle the sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


# print the lines read from the sensor apart from the extra \n chars
while True:

    print("sensor_1: " + str(get_temperatures_sensors()[0]))
    # print("sensor_2: " + str(get_temperatures_sensors()[1]))

    time.sleep(0.5)
