import time
from simple_pid import PID
from boiler import GaggiaBoiler

pid = PID(1, 0.1, 0.05, setpoint=95)

while True:
    gaggia = GaggiaBoiler()
    current_temp = gaggia.get_boiler_temperature()
    new_value = pid(current_temp)
    if new_value > 0:
        gaggia.start()
    else:
        gaggia.stop()
    time.sleep(.5)
