from time import sleep
from machine import Pin
from dht import DHT22
import ujson
import machine
import umail

class DHTReader:
    def __init__(self):
        self.sensor = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))   # DHT-22 on GPIO 15 (input with internal pull-up resistor)
        self.blueLed = machine.Pin(2, machine.Pin.OUT)
        self.ledInterval = 0.01
        self.readingInterval = 0.5

    def using_email(self, from_email, from_password):
        self.smtp = umail.SMTP('smtp.gmail.com', 587, username=from_email, password=from_password)

    def send_email(self, to_email, email_body, override_mail_from, email_subject, t):
        self.smtp.to(to_email)
        email_message = "From: ({})\n".format(override_mail_from)
        email_message += "Subject: {}\n".format(email_subject)
        email_message += " {}C.\n".format(t)
        self.smtp.send(email_message)
        self.smtp.quit()

    def measure(self):
        try:
            self.sensor.measure()   # Poll sensor
            t = self.sensor.temperature()
            h = self.sensor.humidity()
            if isinstance(t, float) and isinstance(h, float):  # Confirm sensor results are numeric
                reading = {}
                reading["temperature"] = t
                reading["humidity"] = h
                reading["interval"] = self.readingInterval
                encodedReading = ujson.dumps(reading)
                print(encodedReading)
            else:
                print('Invalid sensor readings.')
        except OSError:
            print('Failed to read sensor.')
        self.blueLed.value(1)
        sleep(self.ledInterval)
        self.blueLed.value(0)
        sleep(self.ledInterval)
        sleep(self.readingInterval)
        return t

    def read_forever(self):
        while True:
            t = self.measure()