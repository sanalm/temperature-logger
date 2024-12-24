# Temperature Logger
This repository contains ESP32 firmware to read temperature and humidity from DHT22 on an ESP32 dev board using micropython
It can also send the temperature by email and OTA upgrade

## Raspberry Pi

rshell --buffer-size=30 -p /dev/ttyUSB0

### To see what files are written to ESP32 board
ls /pyboard

### To write from Raspberry Pi to ESP32
cp main/dhtRead.py /pyboard/main/dhtRead.py


## Ubuntu
minicom

### Environment Setup (Ubuntu)
    sudo apt-get install minicom

    sudo snap install micropython

    sudo apt install python-pip

    pip install esptool

    git clone https://github.com/espressif/esptool.git

    cd esptool/

    sudo     python setup.py install

    cd git/

    git clone https://github.com/adafruit/ampy.git

    cd ampy/

    sudo python3 setup.py install

## Firmware upload procedure
### Erase flash

Whilst pressing the "Boot" button on the esp32

  `sudo esptool.py --chip esp32 -p /dev/ttyUSB0 erase_flash`

Release button when flashing starts

### Flash Python environment

Whilst pressing the "Boot" button on the esp32

  `ls ~/Downloads/esp32-20210902-v1.17.bin`

  `sudo esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ~/Downloads/esp32-20210902-v1.17.bin` 

Release button when flashing starts

### Flash Python firmware (Python source files)
  
  `cd ~/git`
  `git clone https://github.com/sanalm/temperature-logger/`

Momentarily press "EN" button on ESP32 and then

  `cd temperature-logger`
  `ampy -p /dev/ttyUSB0 put boot.py`
  `ampy -p /dev/ttyUSB0 put main.conf`
  `ampy -p /dev/ttyUSB0 put umail.py`
  `ampy -p /dev/ttyUSB0 mkdir main`
  `ampy -p /dev/ttyUSB0 put main/config.py main/config.py`
  `ampy -p /dev/ttyUSB0 put main/main.py main/main.py`
  `ampy -p /dev/ttyUSB0 put main/dhtRead.py main/dhtRead.py`
  `ampy -p /dev/ttyUSB0 put main/ota_updater.py main/ota_updater.py` 

Then momentarily press "EN" button on ESP32 again to reboot and run

## Serial port
   `sudo minicom --baudrate 115200 --device /dev/ttyUSB0`

## To read Flash Id

Issue:

    sudo esptool.py --chip esp32 -p /dev/ttyUSB0 flash_id

Hold down BOOT button when "Connecting........_____....." appears on the terminal