from tsic import TsicInputChannel, Measurement, TSIC306
from simple_pid import PID
import RPi.GPIO as GPIO
import pigpio
import time

boilerNumber = 23

pi = pigpio.pi()
tsic = TsicInputChannel(pi, gpio=17, tsic_type=TSIC306)
pid = PID(1, 0.1, 0.05, setpoint=95)
boiler = GPIO.PWM(boilerNumber, 50)


while True:
    current_temp = tsic.measure_once(0.1)
    new_value = pid(current_temp)
    if new_value > 0:
        boiler.start()
    else:
        boiler.stop()
    time.sleep(.5)