from main.config import Config
from main.ota_updater import OTAUpdater
from main.dhtRead import DHTReader
import os
import machine

def check_for_update_to_install_during_next_reboot():
    o = OTAUpdater('https://github.com/sanalm/temperature-logger')
    o.using_network(ssid, password)
    o.check_for_update_to_install_during_next_reboot()

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/sanalm/temperature-logger')
    o.using_network(ssid, password)
    o.download_and_install_update_if_available(ssid, password)

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    r = DHTReader()
    t = r.measure()
    r.using_email(from_email, from_password)
    r.send_email(to_email, email_body, override_mail_from, email_subject, t)
    r.read_forever()

def boot():
    if 'next' in os.listdir():
        download_and_install_update_if_available()
    else:
        check_for_update_to_install_during_next_reboot()
    start()

# load configuration for a file
config = Config('main.conf')
ssid = config.get('ssid')
password = config.get('password')
from_email = config.get('from_email')
from_password = config.get('from_password')
to_email = config.get('to_email')
email_body = config.get('email_body')
override_mail_from = config.get('override_mail_from')
email_subject = config.get('email_subject')

print('>>> ********************************************** <<<')
print('<<< ********************************************** >>>')

boot()
