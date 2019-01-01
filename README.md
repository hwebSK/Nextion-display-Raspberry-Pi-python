# Nextion display - Raspberry Pi - Python
**sends_data.py** - Raspberry Pi 3 Model B+ read data from thingspeak and sends to Nextion display. 
**read_influxdb_data_to_nextion.py** - Read influxdb last row and send to nextion display.

## Configuring The GPIO Serial Port On Raspbian Jessie and Stretch Including Pi 3
- `sudo raspi-config` 
*5 Interfacing Options* - Enter
*P6 Serial* - Enter
*Would you like a login shell to be accessible over serial?* - Enert NO
*Would you like the serial port hardware to be enabled? *- Enter YES

- `sudo nano /boot/cmdline.txt`
find:
*console=serial<span style="color:red">0</span>*
 and replace:
*console=serial<span style="color:red">1</span>*

- `sudo nano /boot/config.txt`
write to the end:
*dtoverlay=pi3-disable-bt
enable_uart=1*

- `sudo reboot`
