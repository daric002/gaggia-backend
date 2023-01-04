import pigpio
from tsic import TsicInputChannel, TSIC306

try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO


BOILER_NUMBER = 23
TEMPERATURE_PROBE_NUMBER = 17


class GaggiaBoiler:
    """A boiler class"""

    pi = pigpio.pi()
    tsic = TsicInputChannel(pi, gpio=TEMPERATURE_PROBE_NUMBER, tsic_type=TSIC306)
    boiler = GPIO.PWM(BOILER_NUMBER, 50)
    boiler_temperature_target = 0

    def get_boiler_temperature(self) -> int:
        """the temperature of the boiler"""
        return self.tsic.measure_once(0.1)

    def start(self):
        """start the heater"""
        self.boiler.start()

    def stop(self):
        """stop the heater"""
        self.boiler.stop()
