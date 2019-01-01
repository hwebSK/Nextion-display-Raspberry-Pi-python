# Nextion display - Raspberry Pi - Python
**sends_data.py** - Raspberry Pi 3 Model B+ read data from thingspeak and sends to Nextion display. 
**read_influxdb_data_to_nextion.py** - Read influxdb last row and send to Nextion display.

## Configuring The GPIO Serial Port On Raspbian Stretch Including Pi 3
- `sudo raspi-config`<br/>
*5 Interfacing Options* - Enter<br/>
*P6 Serial* - Enter<br/>
*Would you like a login shell to be accessible over serial?* - Entert NO<br/>
*Would you like the serial port hardware to be enabled?* - Enter YES<br/>

- `sudo nano /boot/cmdline.txt`<br/>
find:<br/>
*console=serial0*<br/>
 and replace:<br/>
*console=serial<span style="color:red">1</span>*<br/>

- `sudo nano /boot/config.txt`<br/>
write to the end:<br/>
*dtoverlay=pi3-disable-bt<br/>
enable_uart=1*<br/>

- `sudo reboot`

Correct to have a serial port working on a Pi 3B called `/dev/serial0
