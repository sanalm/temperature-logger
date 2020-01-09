# from ota_update.main.ota_updater import OTAUpdater
from ota_updater import OTAUpdater

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/sanalm/temperature-logger.git')
    o.download_and_install_update_if_available('wifi-ssid', 'wifi-password')

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    import dhtRead


def boot():
    download_and_install_update_if_available()
    start()

boot()
