from time import sleep
from machine import Pin
from dht import DHT22
import ujson
import machine

sensor = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))   # DHT-22 on GPIO 15 (input with internal pull-up resistor)
blueLed = machine.Pin(2, machine.Pin.OUT)
ledInterval = 0.01
readingInterval = 0.5

while True:
    try:
        sensor.measure()   # Poll sensor
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):  # Confirm sensor results are numeric
            reading = {}
            reading["temperature"] = t
            reading["humidity"] = h
            reading["interval"] = readingInterval
            encodedReading = ujson.dumps(reading)
            print(encodedReading)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    blueLed.value(1)
    sleep(ledInterval)
    blueLed.value(0)
    sleep(ledInterval)
    sleep(readingInterval)
