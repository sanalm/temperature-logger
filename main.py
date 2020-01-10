from main.config import Config
from main.ota_updater import OTAUpdater

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/sanalm/temperature-logger')
    o.using_network(ssid, password)
    o.check_for_update_to_install_during_next_reboot()
    # o.download_and_install_update_if_available('VM4420671', 'k5qdPdscrybp')
    # o.download_updates_if_available()
    # print(o.get_latest_version())

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    from main.dhtRead import dhtRead


def boot():
    download_and_install_update_if_available()
    start()

# load configuration for a file
config = Config('main.conf')
ssid = config.get('ssid')
password = config.get('password')

boot()
