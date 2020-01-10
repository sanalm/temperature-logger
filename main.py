from main.config import Config
from main.ota_updater import OTAUpdater
import os

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
    from main.dhtRead import dhtRead


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

print('>>> ******************************************** <<<')

boot()
