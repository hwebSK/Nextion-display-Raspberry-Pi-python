import influxdb
import serial
import time
from datetime import datetime

host = ''
port = 8086
database = ''
username = ''
password = ''
device1 = ''
device2 = ''
device3 = ''
measurement = ''
t = 'time'

while True:
	client = influxdb.InfluxDBClient(host=host, port=port, database=database, 
	username=username, password=password)

	results = client.query(("SELECT time, %s,%s,%s FROM %s ORDER BY time DESC LIMIT 1") % 
							(device1, device2, device3, measurement)
							)
	points = results.get_points()


	for item in points:
	    a = (item[device1])
	    b = (item[device2])
	    c = (item[device3])
	    tm = (item[t])
	    
	    #print "Udaje boli namerane " + tm
	    #print a
	    #print b
	    #print c

	client.close()

#---------Display-----------#
	
	#Set end of file
	eof = "\xff\xff\xff"

	con = serial.Serial(

	    port='/dev/serial0',
	    baudrate=9600,
	    parity=serial.PARITY_NONE,
	    stopbits=serial.STOPBITS_ONE,
	    bytesize=serial.EIGHTBITS,
	)

	alt1 = 'page0.t5.txt="'+str(a)+'"'+eof
	alt2 = 'page0.t6.txt="'+str(b)+'"'+eof

	con.write(alt1)
	con.write(alt2)
	
	#undimCmd = "dim=30"
	#con.write(undimCmd + eof) #set screen brightness to 30%

	time.sleep(60)
