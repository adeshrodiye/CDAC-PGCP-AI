class TemperatureExceededError(Exception):
    pass

class Sensors:
    def __init__(self,temperature):
        self._temperature = temperature

    def check_temperature(self):
        if self._temperature > 50:
            raise TemperatureExceededError('Temperature too high')

sensor = Sensors(55)

try:
    sensor.check_temperature()
except TemperatureExceededError as er:
    print(er)

print("!!!")