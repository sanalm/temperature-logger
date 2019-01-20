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
 1925  sudo esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/esp32spiram-20190112-v1.9.4-779-g5064df207.bin
 1926  ls ~/Downloads/
 1927  sudo esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/esp32-20190112-v1.9.4-779-g5064df207.bin
 1928  pip3 install --user adafruit-ampy
 1929  sudo apt install python3-pip
 1930  pip3 install --user adafruit-ampy
 1931  ampy --help
 1932  sudo pip3 install --user adafruit-ampy
 1933  ampy --help
 1934  sudo pip3 install adafruit-ampy
 1935  ampy --help
 1936  pip install adafruit-ampy
 1937  ampy --help
 1938  exit
 1939  ls ~/Desktop/
 1940  cd ~/Desktop/
 1941  ls
 1942  exit
 1943  minicom
 1944  ls /dev/tty*
 1945  ls /dev/ttyUSB*
 1946  minicom
 1947  ls /dev/ttyUSB*
 1948  sudo minicom -s
 1949  sudo minicom
 1950  ls /dev/ttyUSB*
 1951  sudo minicom
 1952  ls
 1953  esptool.py --chip esp32 -p /dev/ttyUSB0 erase_flash
 1954  sudo minicom
 1955  sudo minicom -s
 1956  sudo minicom
 1957  esptool.py --chip esp32 -p /dev/ttyUSB0 erase_flash
 1958  sudo minicom
 1959  ampy --help
 1960  cd workspace/
 1961  git clone https://github.com/adafruit/ampy.git
 1962  cd ampy/
 1963  ls
 1964  python3 setup.py install
 1965  ampy --help
 1966  sudo python3 setup.py install

#Flash firmware

Power reset ESP DEV board
Hold down button EN and momentariloy press button BOOT
cd ~/workspace/temperature-logger
sudo ampy -p /dev/ttyUSB0 put dhtRead.py 




