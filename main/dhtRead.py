from time import sleep
from machine import Pin
from dht import DHT22
import ujson
import machine
import umail
import urequests
import ubinascii
import urandom as random
import utime as time

class DHTReader:
    def __init__(self):
        self.sensor = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))   # DHT-22 on GPIO 15 (input with internal pull-up resistor)
        self.blueLed = machine.Pin(2, machine.Pin.OUT)
        self.ledInterval = 0.01
        self.readingInterval = 0.5
        self.bellPress = 0

    def using_email(self, from_email, from_password):
        self.smtp = umail.SMTP('smtp.gmail.com', 587, username=from_email, password=from_password)

    def boundary(self):
        return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOUPQRSTUWVXYZ') for i in range(15))

    def send_mail(self, email, attachment = None):
        time_now = time.time()
        tm = time.localtime(time_now)
        self.bellPress += 1
        capture = False    
        if attachment:
            img_buffer = urequests.get(attachment['image_capture'])
            if img_buffer.status_code == 200:
                b64 = ubinascii.b2a_base64(img_buffer.content)
                capture = True

        smtp = umail.SMTP('smtp.gmail.com', 587, username=email['from_email'], password=email['from_password'])
        smtp.to(email['to'])
        smtp.write("From: ({0})\n".format(email['from']))
        smtp.write("To: {0} <{0}>\n".format(email['to']))
        smtp.write("Subject: {0}\n".format(email['subject']))
        bell_press = "Bell Press # {0}, {1}\n".format(self.bellPress, tm)
        print(tm)
        if capture:
            text_id = self.boundary()
            attachment_id = self.boundary()
            smtp.write("MIME-Version: 1.0\n")
            smtp.write('Content-Type: multipart/mixed;\n boundary="------------{0}"\n'.format(attachment_id))
            smtp.write('--------------{0}\nContent-Type: multipart/alternative;\n boundary="------------{1}"\n\n'.format(attachment_id, text_id))
            smtp.write('--------------{0}\nContent-Type: text/plain; charset=utf-8; format=flowed\nContent-Transfer-Encoding: 7bit\n\n{1}\n\n--------------{0}--\n\n'.format(text_id, bell_press))
            smtp.write('--------------{0}\nContent-Type: image/jpeg;\n name="{1}"\nContent-Transfer-Encoding: base64\nContent-Disposition: attachment;\n  filename="{1}"\n\n'.format(attachment_id, attachment['name']))
            smtp.write(b64)
            smtp.write('--------------{0}--'.format(attachment_id))
            smtp.send()
        else:
            smtp.send("{} image couldn\'t be retreived\n".format(bell_press))
        smtp.quit()

    def send_email2(self, to_email, email_body, override_mail_from, email_subject, t):
        self.smtp.to(to_email)
        img_buffer = urequests.get('http://192.168.0.4/img/snapshot.cgi?size=4')
        buffer = "data: \n html: \n <img src={}>\n".format(img_buffer)
        self.smtp.write(buffer)
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