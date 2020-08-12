# To test Bluetooth beacon in Linux environment. By. GTO
=====================
# Target devices
  - Raspberry Pi 3 B+
  - OrangePi Zero
  - BananaPi M2 & P2 Zero

## 1. bluetooth stack install for target devices
_sudo apt-get update && sudo apt-get upgrade 

sudo apt-get install libusb-dev 

sudo apt-get install libdbus-1-dev 

sudo apt-get install libglib2.0-dev --fix-missing 

sudo apt-get install libudev-dev 

sudo apt-get install libical-dev 

sudo apt-get install libreadline-dev

sudo apt-get install libdbus-glib-1-dev 

sudo mkdir bluez cd bluez 

sudo wget www.kernel.org/pub/linux/bluetooth/bluez-5.19.tar.gz 

sudo gunzip bluez-5.19.tar.gz 

sudo tar xvf bluez-5.19.tar cd bluez-5.19

sudo ./configure --disable-systemd 

sudo make 

sudo make install 

sudo apt-get install python-bluez 

sudo shutdown -r now_


## 2. if you use to BLE dongle
check 'lsusb'

## 3. check 'hciconfig '
![image](https://user-images.githubusercontent.com/30851459/89870300-9401c780-dbf0-11ea-9842-8a4bab223bfb.png)

## 4. download for iBeacon source code(example)
_sudo apt-get install git

git clone https://github.com/switchdoclabs/iBeacon-Scanner-

sudo chown pi iBeacon-Scanner-

sudo chgrp pi iBeacon-Scanner-_

## 5. iBeacon scanning
![image](https://user-images.githubusercontent.com/30851459/89870651-1f7b5880-dbf1-11ea-9ed5-c4febe282620.png)



