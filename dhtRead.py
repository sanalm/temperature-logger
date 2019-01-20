from time import sleep
from machine import Pin
from dht import DHT22
import ujson
import machine

sensor = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))   # DHT-22 on GPIO 15 (input with internal pull-up resistor)
blueLed = machine.Pin(2, machine.Pin.OUT)
ledTimeout = 0.01
readingTimeout = 4

while True:
    try:
        sensor.measure()   # Poll sensor
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):  # Confirm sensor results are numeric
            reading = {}
            reading["temperature"] = t
            reading["humidity"] = h
            encodedReading = ujson.dumps(reading)
            print(encodedReading)
            # msg = (b'{0:3.1f},{1:3.1f}'.format(t, h))
            # print(msg)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    blueLed.value(1)
    sleep(ledTimeout)
    blueLed.value(0)
    sleep(ledTimeout)
    sleep(readingTimeout)
    sleep(4)
