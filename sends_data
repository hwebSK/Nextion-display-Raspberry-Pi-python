import serial
import urllib2
import json
import time

READ_API_KEY=' '
CHANNEL_ID= ' '

#Set end of file
eof = "\xff\xff\xff"

con = serial.Serial(

    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)

while True:
    TS = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                       % (CHANNEL_ID,READ_API_KEY))

    response = TS.read()
    data=json.loads(response)

    a = data['created_at']
    b = data['field1'].encode('utf-8')
    c = data['field2'].encode('utf-8')
    print a + "    " + b + "    " + c

    alt1 = 'page0.t5.txt="'+b+'"'+eof
    alt2 = 'page0.t6.txt="'+c+'"'+eof

    #zapis do nextion plus ukoncovaci EOF
    con.write(alt1)
    con.write(alt2)
    
    time.sleep(180)   
    TS.close()
