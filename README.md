# Temperature Logger
This repository contains ESP32 firmware to read temperature and humidity from DHT22 on an ESP32 dev board using micropython

## Environment
minicom


### Environment Setup (Ubuntu)
sudo apt-get install minicom
sudo snap install micropython
sudo apt install python-pip
pip install esptool

git clone https://github.com/espressif/esptool.git
cd esptool/

sudo python setup.py install
sudo esptool.py --chip esp32 -p /dev/ttyUSB0 erase_flash

ls ~/Downloads/esp32spiram-20190112-v1.9.4-779-g5064df207.bin
sudo esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/esp32spiram-20190112-v1.9.4-779-g5064df207.bin
sudo esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/esp32-20190112-v1.9.4-779-g5064df207.bin

sudo minicom -s
esptool.py --chip esp32 -p /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 -p /dev/ttyUSB0 erase_flash

cd workspace/
git clone https://github.com/adafruit/ampy.git
cd ampy/
sudo python3 setup.py install

# Flash firmware

Power reset ESP DEV board
Hold down button EN and momentariloy press button BOOT
cd ~/workspace/temperature-logger
sudo ampy -p /dev/ttyUSB0 put dhtRead.py 