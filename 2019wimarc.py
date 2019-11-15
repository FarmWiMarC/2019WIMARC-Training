#! /usr/bin/python
import serial
import MySQLdb
import pprint
import string
#import urllib2
import urllib
import datetime
import time
import pycurl
import os

import RPi.GPIO as GPIO


import httplib
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
from itertools import count



devicename = 'wimarc'
URLlocation = 'https://opasnectec.000webhostapp.com/2019WIMARC/'#-----------Connect to wvdial------------------------

from time import strftime
rcvH=strftime("%Y-%m-%d ")
rcvSR=strftime("%H:%M:%S ")
lastTime = datetime.datetime.now()
recordLastTime = lastTime.minute



#devicename = 'mp1weather'
#URLlocation = 'http://thaismartfarm.com/water/StationMoisture/'#os.system("sudo wvdial 3gconnect

#-----------Connect to SerialPort----------------------------------------
#ser = serial.Serial('COM28') 
try :
    ser = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)
    ser.close()
except:     print 'ERROR: Port not found '
try:          ser.open()
except:       print 'ERROR : Port open '
#-----------------------------------------------------------------------
# Specify the url
#urltestnetwork = 'http://opasnectec.orgfree.com/InsertIn_testnetwork.php'
urlA = URLlocation+'InsertIn_a.php'
urlB = URLlocation+'InsertIn_b.php'
#urltest2 = 'http://203.150.37.159/InsertIn_test.php'
#urlA2 = 'http://203.150.37.159/InsertIn_home1.php'
#urlB2 = 'http://203.150.37.159/InsertIn_home2.php'

urlC = URLlocation+'InsertIn_c.php'
urlD = URLlocation+'InsertIn_d.php'
urlE = URLlocation+'InsertIn_e.php'
urlF = URLlocation+'InsertIn_f.php'

urlsensor=URLlocation+'InsertIn_sensor.php'
urlG = URLlocation+'InsertIn_g.php'
urlH = URLlocation+'InsertIn_h.php'
urlI = URLlocation+'InsertIn_i.php'
urlJ = URLlocation+'InsertIn_j.php'




#---------------MQTT mosquitto--------------------------
connectMQTT=0
checkmessage =''
global checkmessageMQTT
checkmessageMQTT =''
global SendmessageMQTT
SendmessageMQTT =''
global pumpstatus
pumpstatus =''
global MQTTcount
MQTTcount =0
MQTTmain=""

def on_connect(clientMQTT, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    
    clientMQTT.subscribe("MQTTcam")
    
 
# The callback for when a message is received from the server.
def on_message(clientMQTT, userdata, msg):
    global checkmessageMQTT
    global pumpstatus
    global MQTTcount
    print("recieved: "+msg.topic+" "+str(msg.payload))
    #words = msg.payload.split()
    #if words[0] == 'run': #  If 'run' is the first word of the message
    #   globals()[words[1]]() #  Run the function named by the second word in the message
    
    if msg.topic == "MQTTcam" :
            checkmessageMQTT =msg.topic+":"+str(msg.payload)+':'+str(MQTTcount)
            MQTTcount=0
            print checkmessageMQTT        
        #netpiecount = 0
def publish_mqtt(payload):
    """
    Send an MQTT mesage to javaScript client
    """
    topic = 'MQTTwimarc'
    try:
        publish.single(topic, payload, hostname='127.0.0.1', port=1883, retain=False, qos=0)
        print "publish_mqtt"
    except Exception as err:
            print "Couldn't publish :" + str(err)
            pass    




#####################################################3








tempAtop = 0      
tempAmid = 0      #recieve A Data Second part
        
tempAbot = 0

humidA = 0
      
clientcount=0        
connectcount=0
       
tempBtop = 0
       
tempBmid = 0
        
tempBbot = 0
        

humidB = 0
               



rcv=''
time.sleep (500.0 / 1000.0)
indexGetA=0
indexGetB=0
TimeToSave=0;
TimeCount=0
rcvAH =0
rcvBH=0
nodata=0
status =0 
rcvAF = 0      #recieve A Data Second part
rcvAS = 0      #recieve A Data Second part
#rcvBF = 0    #recieve B Data First part
#rcvCF = 0      #recieve A Data Second part
#rcvCS = 0      #recieve A Data Second part
#rcvDF = 0    #recieve B Data First part
#rcvDS = 0    #recieve B Data Second part

a_rcvAF = 0      #recieve A Data Second part
a_rcvAS = 0      #recieve A Data Second part
a_rcvBF = 0    #recieve B Data First part
a_rcvBS = 0    #recieve B Data Second part
a_rcvCF = 0      #recieve A Data Second part
a_rcvCS = 0      #recieve A Data Second part
a_rcvDF = 0    #recieve B Data First part
a_rcvDS = 0    #recieve B Data Second part


b_rcvAF = 0      #recieve A Data First part
b_rcvAS = 0      #recieve A Data Second part
b_rcvBF = 0    #recieve B Data First part
b_rcvBS = 0    #recieve B Data Second part
b_rcvCF = 0      #recieve A Data First part
b_rcvCS = 0      #recieve A Data Second part
b_rcvDF = 0    #recieve B Data First part
b_rcvDS = 0    #recieve B Data Second part




c_rcvAF = 0      #recieve A Data First part
c_rcvAS = 0      #recieve A Data Second part
c_rcvBF = 0    #recieve B Data First part
c_rcvBS = 0    #recieve B Data Second part
c_rcvCF = 0      #recieve A Data First part
c_rcvCS = 0      #recieve A Data Second part
c_rcvDF = 0    #recieve B Data First part
c_rcvDS = 0    #recieve B Data Second part



d_rcvAF = 0      #recieve A Data First part
d_rcvAS = 0      #recieve A Data Second part
d_rcvBF = 0    #recieve B Data First part
d_rcvBS = 0    #recieve B Data Second part
d_rcvCF = 0      #recieve A Data First part
d_rcvCS = 0      #recieve A Data Second part
d_rcvDF = 0    #recieve B Data First part
d_rcvDS = 0    #recieve B Data Second part




e_rcvAF = 0      #recieve A Data First part
e_rcvAS = 0      #recieve A Data Second part
e_rcvBF = 0    #recieve B Data First part
e_rcvBS = 0    #recieve B Data Second part
e_rcvCF = 0      #recieve A Data First part
e_rcvCS = 0      #recieve A Data Second part
e_rcvDF = 0    #recieve B Data First part
e_rcvDS = 0    #recieve B Data Second part
                          

f_rcvAF = 0      #recieve A Data First part
f_rcvAS = 0      #recieve A Data Second part
f_rcvBF = 0    #recieve B Data First part
f_rcvBS = 0    #recieve B Data Second part
f_rcvCF = 0      #recieve A Data First part
f_rcvCS = 0      #recieve A Data Second part
f_rcvDF = 0    #recieve B Data First part
f_rcvDS = 0    #recieve B Data Second part

g_rcvAF = 0      #recieve A Data First part
g_rcvAS = 0      #recieve A Data Second part
g_rcvBF = 0    #recieve B Data First part
g_rcvBS = 0    #recieve B Data Second part
g_rcvCF = 0      #recieve A Data First part
g_rcvCS = 0      #recieve A Data Second part
g_rcvDF = 0    #recieve B Data First part
g_rcvDS = 0    #recieve B Data Second part


h_rcvAF = 0      #recieve A Data First part
h_rcvAS = 0      #recieve A Data Second part
h_rcvBF = 0    #recieve B Data First part
h_rcvBS = 0    #recieve B Data Second part
h_rcvCF = 0      #recieve A Data First part
h_rcvCS = 0      #recieve A Data Second part
h_rcvDF = 0    #recieve B Data First part
h_rcvDS = 0    #recieve B Data Second part


i_rcvAF = 0      #recieve A Data First part
i_rcvAS = 0      #recieve A Data Second part
i_rcvBF = 0    #recieve B Data First part
i_rcvBS = 0    #recieve B Data Second part
i_rcvCF = 0      #recieve A Data First part
i_rcvCS = 0      #recieve A Data Second part
i_rcvDF = 0    #recieve B Data First part
i_rcvDS = 0    #recieve B Data Second part


j_rcvAF = 0      #recieve A Data First part
j_rcvAS = 0      #recieve A Data Second part
j_rcvBF = 0    #recieve B Data First part
j_rcvBS = 0    #recieve B Data Second part
j_rcvCF = 0      #recieve A Data First part
j_rcvCS = 0      #recieve A Data Second part
j_rcvDF = 0    #recieve B Data First part
j_rcvDS = 0    #recieve B Data Second part



ax_rcvAF = 0      #recieve A Data Second part
ax_rcvAS = 0      #recieve A Data Second part
ax_rcvBF = 0    #recieve B Data First part
ax_rcvBS = 0    #recieve B Data Second part
ax_rcvCF = 0      #recieve A Data Second part
ax_rcvCS = 0      #recieve A Data Second part
ax_rcvDF = 0    #recieve B Data First part
ax_rcvDS = 0    #recieve B Data Second part


bx_rcvAF = 0      #recieve A Data First part
bx_rcvAS = 0      #recieve A Data Second part
bx_rcvBF = 0    #recieve B Data First part
bx_rcvBS = 0    #recieve B Data Second part
bx_rcvCF = 0      #recieve A Data First part
bx_rcvCS = 0      #recieve A Data Second part
bx_rcvDF = 0    #recieve B Data First part
bx_rcvDS = 0    #recieve B Data Second part




cx_rcvAF = 0      #recieve A Data First part
cx_rcvAS = 0      #recieve A Data Second part
cx_rcvBF = 0    #recieve B Data First part
cx_rcvBS = 0    #recieve B Data Second part
cx_rcvCF = 0      #recieve A Data First part
cx_rcvCS = 0      #recieve A Data Second part
cx_rcvDF = 0    #recieve B Data First part
cx_rcvDS = 0    #recieve B Data Second part



dx_rcvAF = 0      #recieve A Data First part
dx_rcvAS = 0      #recieve A Data Second part
dx_rcvBF = 0    #recieve B Data First part
dx_rcvBS = 0    #recieve B Data Second part
dx_rcvCF = 0      #recieve A Data First part
dx_rcvCS = 0      #recieve A Data Second part
dx_rcvDF = 0    #recieve B Data First part
dx_rcvDS = 0    #recieve B Data Second part




ex_rcvAF = 0      #recieve A Data First part
ex_rcvAS = 0      #recieve A Data Second part
ex_rcvBF = 0    #recieve B Data First part
ex_rcvBS = 0    #recieve B Data Second part
ex_rcvCF = 0      #recieve A Data First part
ex_rcvCS = 0      #recieve A Data Second part
ex_rcvDF = 0    #recieve B Data First part
ex_rcvDS = 0    #recieve B Data Second part
                          

fx_rcvAF = 0      #recieve A Data First part
fx_rcvAS = 0      #recieve A Data Second part
fx_rcvBF = 0    #recieve B Data First part
fx_rcvBS = 0    #recieve B Data Second part
fx_rcvCF = 0      #recieve A Data First part
fx_rcvCS = 0      #recieve A Data Second part
fx_rcvDF = 0    #recieve B Data First part
fx_rcvDS = 0    #recieve B Data Second part

gx_rcvAF = 0      #recieve A Data First part
gx_rcvAS = 0      #recieve A Data Second part
gx_rcvBF = 0    #recieve B Data First part
gx_rcvBS = 0    #recieve B Data Second part
gx_rcvCF = 0      #recieve A Data First part
gx_rcvCS = 0      #recieve A Data Second part
gx_rcvDF = 0    #recieve B Data First part
gx_rcvDS = 0    #recieve B Data Second part


hx_rcvAF = 0      #recieve A Data First part
hx_rcvAS = 0      #recieve A Data Second part
hx_rcvBF = 0    #recieve B Data First part
hx_rcvBS = 0    #recieve B Data Second part
hx_rcvCF = 0      #recieve A Data First part
hx_rcvCS = 0      #recieve A Data Second part
hx_rcvDF = 0    #recieve B Data First part
hx_rcvDS = 0    #recieve B Data Second part


ix_rcvAF = 0      #recieve A Data First part
ix_rcvAS = 0      #recieve A Data Second part
ix_rcvBF = 0    #recieve B Data First part
ix_rcvBS = 0    #recieve B Data Second part
ix_rcvCF = 0      #recieve A Data First part
ix_rcvCS = 0      #recieve A Data Second part
ix_rcvDF = 0    #recieve B Data First part
ix_rcvDS = 0    #recieve B Data Second part


jx_rcvAF = 0      #recieve A Data First part
jx_rcvAS = 0      #recieve A Data Second part
jx_rcvBF = 0    #recieve B Data First part
jx_rcvBS = 0    #recieve B Data Second part
jx_rcvCF = 0      #recieve A Data First part
jx_rcvCS = 0      #recieve A Data Second part
jx_rcvDF = 0    #recieve B Data First part
jx_rcvDS = 0    #recieve B Data Second part





m_rcvAF = 0      #recieve A Data First part
m_rcvAS = 0      #recieve A Data Second part
m_rcvBF = 0    #recieve B Data First part
m_rcvBS = 0    #recieve B Data Second part
m_rcvCF = 0      #recieve A Data First part
m_rcvCS = 0      #recieve A Data Second part
m_rcvDF = 0    #recieve B Data First part
m_rcvDS = 0    #recieve B Data Second part

v_rcvAF = 0      #recieve A Data First part
v_rcvAS = 0      #recieve A Data Second part
v_rcvBF = 0    #recieve B Data First part
v_rcvBS = 0    #recieve B Data Second part
v_rcvCF = 0      #recieve A Data First part
v_rcvCS = 0      #recieve A Data Second part
v_rcvDF = 0    #recieve B Data First part
v_rcvDS = 0    #recieve B Data Second part



a2_rcvAF = 0      #recieve A Data Second part
a2_rcvAS = 0      #recieve A Data Second part
a2_rcvBF = 0    #recieve B Data First part
a2_rcvBS = 0    #recieve B Data Second part
a2_rcvCF = 0      #recieve A Data Second part
a2_rcvCS = 0      #recieve A Data Second part
a2_rcvDF = 0    #recieve B Data First part
a2_rcvDS = 0    #recieve B Data Second part


b2_rcvAF = 0      #recieve A Data First part
b2_rcvAS = 0      #recieve A Data Second part
b2_rcvBF = 0    #recieve B Data First part
b2_rcvBS = 0    #recieve B Data Second part
b2_rcvCF = 0      #recieve A Data First part
b2_rcvCS = 0      #recieve A Data Second part
b2_rcvDF = 0    #recieve B Data First part
b2_rcvDS = 0    #recieve B Data Second part




c2_rcvAF = 0      #recieve A Data First part
c2_rcvAS = 0      #recieve A Data Second part
c2_rcvBF = 0    #recieve B Data First part
c2_rcvBS = 0    #recieve B Data Second part
c2_rcvCF = 0      #recieve A Data First part
c2_rcvCS = 0      #recieve A Data Second part
c2_rcvDF = 0    #recieve B Data First part
c2_rcvDS = 0    #recieve B Data Second part



d2_rcvAF = 0      #recieve A Data First part
d2_rcvAS = 0      #recieve A Data Second part
d2_rcvBF = 0    #recieve B Data First part
d2_rcvBS = 0    #recieve B Data Second part
d2_rcvCF = 0      #recieve A Data First part
d2_rcvCS = 0      #recieve A Data Second part
d2_rcvDF = 0    #recieve B Data First part
d2_rcvDS = 0    #recieve B Data Second part




e2_rcvAF = 0      #recieve A Data First part
e2_rcvAS = 0      #recieve A Data Second part
e2_rcvBF = 0    #recieve B Data First part
e2_rcvBS = 0    #recieve B Data Second part
e2_rcvCF = 0      #recieve A Data First part
e2_rcvCS = 0      #recieve A Data Second part
e2_rcvDF = 0    #recieve B Data First part
e2_rcvDS = 0    #recieve B Data Second part

f2_rcvAF = 0      #recieve A Data First part
f2_rcvAS = 0      #recieve A Data Second part
f2_rcvBF = 0    #recieve B Data First part
f2_rcvBS = 0    #recieve B Data Second part
f2_rcvCF = 0      #recieve A Data First part
f2_rcvCS = 0      #recieve A Data Second part
f2_rcvDF = 0    #recieve B Data First part
f2_rcvDS = 0    #recieve B Data Second part

g2_rcvAF = 0      #recieve A Data First part
g2_rcvAS = 0      #recieve A Data Second part
g2_rcvBF = 0    #recieve B Data First part
g2_rcvBS = 0    #recieve B Data Second part
g2_rcvCF = 0      #recieve A Data First part
g2_rcvCS = 0      #recieve A Data Second part
g2_rcvDF = 0    #recieve B Data First part
g2_rcvDS = 0    #recieve B Data Second part


h2_rcvAF = 0      #recieve A Data First part
h2_rcvAS = 0      #recieve A Data Second part
h2_rcvBF = 0    #recieve B Data First part
h2_rcvBS = 0    #recieve B Data Second part
h2_rcvCF = 0      #recieve A Data First part
h2_rcvCS = 0      #recieve A Data Second part
h2_rcvDF = 0    #recieve B Data First part
h2_rcvDS = 0    #recieve B Data Second part


cAA=0
cAB=0
cAC=0
cAD=0
cBA=0
cBB=0
cBC=0
cBD=0
cCA=0
cCB=0
cCC=0
cCD=0
cDA=0
cDB=0
cDC=0
cDD=0
cEA=0
cEB=0
cEC=0
cED=0
cFA=0
cFB=0
cFC=0
cFD=0
cGA=0
cGB=0
cGC=0
cGD=0

FlagSleep =0
FlagSendTime =0
strOutput=0
strHeader = 'PTA'
FlagOnOffdevice = 0
device = '0'
On='00'
Off='00'
duration ='0'
set_duration=0
imagerecord =0
count_ValueError=0
temp=0
humid=0
rain=0
winds=0
windd=0
mois1=0
mois2=0
lux=0
record =0
imagerecord =0                    
recordmp =0
imagerecordmp =0 

time.sleep (500.0 / 1000.0)
          
#-----------Connect to Database----------------------------------------
conn = MySQLdb.connect( host='localhost', db='sensorA', user='root', passwd='1234' )
#conn = MySQLdb.connect( host='localhost', db='moistureA', user='root', passwd='' )
curs = conn.cursor()
print 'Local MySQL conneted...'

#-----------------------------------------------------------------------
# record index
record =0
# time check variable
recordtime=0
#-----------Sent data to database-----------[ALL database]--------------

#-------------NETPIE------------------
import microgear.client as client

gearkey = 'OeaapzYXiibyhBH'
gearsecret =   'q1w9VTGF3Ik8ImlnCQMefcxp0'
appid =  '2019wimarc' 
global connect
connect =0
global netpiecount
netpiecount=0
checkmessage =''
def connection():
    print "Now I am connected with netpie"
    
def callback_present(gearkey) :
    print gearkey+" become online."

def callback_error(msg) :
    print msg

def subscription(topic,message):
    global checkmessage
    global netpiecount
    #logging.debug(topic+" "+message)
    print topic+" "+message
    if topic == "/tmec/wimarc/station" :
        checkmessage = message
        print checkmessage
        netpiecount = 0 
    

def disconnect():
    global connect
    connect=0
    print "disconnect"
    logging.debug("disconnected")

timestamp = "0:0:0"

connect =0
#///////////////////////////////////////////////////

#/////////read ser 
def read_serial(ser):
    print "Read serial:"
    buf = ''
    i=0
    j=0
    
    while True:
        j=j+1
        try :
            inp = ser.read(size=1) #read a byte
        except :
            print "no input"
            #break
        if inp == 'P' :
            buf = inp
            while i < 26:
                inp = ser.read(size=1) #read a byte
                #print inp.encode("hex") #gives me the correct bytes, each on a newline
                buf = buf + inp #accumalate the response
                i=i+1
                j=0
        #if '\xFF' == inp:
        #if i > 25 :
        #        print inp.encode("hex") # never here
            break
        if j > 10 :
            print "No input"
            break
    return buf
    
    



while True:
        
    #  get date and time
    netpiecount=netpiecount+1
    print 'netpiecount= '+str(netpiecount)
    print 'connectcount= '+str(connectcount)
    from time import strftime
    rcvH=strftime("%Y-%m-%d ")
    rcvSR=strftime("%H:%M:%S ")
    if netpiecount > 500 :
        
        query_args = { 'date': rcvH, 'time':rcvSR,'A':netpiecount, 'B':connectcount,'C':a_rcvBF,'D':a_rcvBS,'E':a_rcvCF, 'F':a_rcvCS,'G':a_rcvDF,'H':a_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
        data = urllib.urlencode(query_args)
         # Send HTTP POST request
        FlagSave =1
        count =0
        while (FlagSave == 1) :
            count=count+1
            try :
                c = pycurl.Curl()
                c.setopt(c.URL,urlRESET)
                c.setopt(c.POSTFIELDS, data)
                c.perform()
                c.close()
                FlagSave =0
            except:
                print 'write to server error..try again'
                curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                conn.commit()
                time.sleep (3)
            if count >1 :
                FlagSave =0
        
        time.sleep (5);
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        input_value = GPIO.input(17)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        time.sleep (10);
        GPIO.output(23, GPIO.LOW)
    
     
    from time import strftime
    rcvH=strftime("%Y-%m-%d ")
    rcvSR=strftime("%H:%M:%S ")
    timestamp = rcvSR
    now = datetime.datetime.now()
    nowyear = now.year
    #if nowyear < 2015 :
    #     os.system("sudo reboot")
    nowhour = now.hour
    nowminute = now.minute
    nowsecond = now.second


    if recordLastTime == now.minute :
         pprint.pprint('RPI WAITING ')
    else:
         recordLastTime = now.minute
         TimeToCheck = recordLastTime % 1;
         TimeToSave = recordLastTime % 3
         


         if TimeToSave == 0 :
              record =1
              #imagerecord =1
              recordmp =1
              
              
    
    if record == 1 :
         
         try :
              curs.execute('INSERT INTO a (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,a_rcvAF,a_rcvAS,a_rcvBF,a_rcvBS,a_rcvCF,a_rcvCS,a_rcvDF,a_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0)
               #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO b (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,b_rcvAF,b_rcvAS,b_rcvBF,b_rcvBS,b_rcvCF,b_rcvCS,b_rcvDF,b_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0)
         except :
              pprint.pprint('access local a b database denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO c (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,c_rcvAF,c_rcvAS,c_rcvBF,c_rcvBS,c_rcvCF,c_rcvCS,c_rcvDF,c_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local c database denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO d (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,d_rcvAF,d_rcvAS,d_rcvBF,d_rcvBS,d_rcvCF,d_rcvCS,d_rcvDF,d_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access database local d denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO e (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,e_rcvAF,e_rcvAS,e_rcvBF,e_rcvBS,e_rcvCF,e_rcvCS,e_rcvDF,e_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local database e denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO f (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,f_rcvAF,f_rcvAS,f_rcvBF,f_rcvBS,f_rcvCF,f_rcvCS,f_rcvDF,e_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local database f denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO g (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,g_rcvAF,g_rcvAS,g_rcvBF,g_rcvBS,g_rcvCF,g_rcvCS,g_rcvDF,g_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local database g denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO h (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,h_rcvAF,h_rcvAS,h_rcvBF,h_rcvBS,h_rcvCF,h_rcvCS,h_rcvDF,h_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
              curs.execute('INSERT INTO i (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,i_rcvAF,i_rcvAS,i_rcvBF,i_rcvBS,i_rcvCF,i_rcvCS,i_rcvDF,i_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);

              curs.execute('INSERT INTO j (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,j_rcvAF,j_rcvAS,j_rcvBF,j_rcvBS,j_rcvCF,j_rcvCS,j_rcvDF,j_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local database h denied')
              #os.system("sudo reboot")       

         try :
              curs.execute('INSERT INTO humid (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,a2_rcvAF,a2_rcvAS,a2_rcvBF,a2_rcvBS,a2_rcvCF,a2_rcvCS,a2_rcvDF,a2_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0)
               #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO rain (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,b2_rcvAF,b2_rcvAS,b2_rcvBF,b2_rcvBS,b2_rcvCF,b2_rcvCS,b2_rcvDF,b2_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0)
         except :
              pprint.pprint('access local a b database denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO temp (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,m_rcvAF,m_rcvAS,m_rcvBF,m_rcvBS,m_rcvCF,m_rcvCS,m_rcvDF,m_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local c database denied')
              #os.system("sudo reboot")


         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO wind (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,d2_rcvAF,d2_rcvAS,d2_rcvBF,d2_rcvBS,d2_rcvCF,d2_rcvCS,d2_rcvDF,d2_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access database local d denied')
              #os.system("sudo reboot")

         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO moisture (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,e2_rcvAF,e2_rcvAS,e2_rcvBF,e2_rcvBS,e2_rcvCF,e2_rcvCS,e2_rcvDF,e2_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local database e denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO volt (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,v_rcvAF,v_rcvAS,v_rcvBF,v_rcvBS,v_rcvCF,v_rcvCS,v_rcvDF,v_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local database f denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO lux (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,g2_rcvAF,g2_rcvAS,g2_rcvBF,g2_rcvBS,g2_rcvCF,g2_rcvCS,g2_rcvDF,g2_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local database g denied')
              #os.system("sudo reboot")
         try :
              #INSERT All DATA TO MySQL DATABASE
              curs.execute('INSERT INTO status (date, time, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(rcvH,rcvSR,h2_rcvAF,h2_rcvAS,h2_rcvBF,h2_rcvBS,h2_rcvCF,h2_rcvCS,h2_rcvDF,h2_rcvDS))
              conn.commit()
              time.sleep (500.0 / 1000.0);
         except :
              pprint.pprint('access local database h denied')
              #os.system("sudo reboot")
         record =0;

         query_args = { 'date': rcvH, 'time':rcvSR,'Temp':m_rcvAF, 'Humid':m_rcvAS,'Rain':m_rcvBF,'WindS':m_rcvBS,'WindD':m_rcvCF, 'M1':m_rcvCS,'M2':m_rcvDF,'Lux':m_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlsensor)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
                   strHeader ="PSA"
              except:
                   print 'write to server error..try again'
                   
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);



         query_args = { 'date': rcvH, 'time':rcvSR,'A':v_rcvAF, 'B':v_rcvAS,'C':v_rcvBF,'D':v_rcvBS,'E':v_rcvCF, 'F':v_rcvCS,'G':v_rcvDF,'H':v_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlF2)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);



         
         
         query_args = { 'date': rcvH, 'time':rcvSR,'A':a_rcvAF, 'B':a_rcvAS,'C':a_rcvBF,'D':a_rcvBS,'E':a_rcvCF, 'F':a_rcvCS,'G':a_rcvDF,'H':a_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlA)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         
         
         time.sleep (500.0 / 1000.0);

         
         
         # Prepare 
         query_args = { 'date': rcvH, 'time':rcvSR,'A':b_rcvAF, 'B':b_rcvAS,'C':b_rcvBF,'D':b_rcvBS,'E':b_rcvCF, 'F':b_rcvCS,'G':b_rcvDF,'H':b_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlB)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);

         FlagSleep = 1

         

         
         # Prepare the data
         query_args = { 'date': rcvH, 'time':rcvSR,'A':c_rcvAF, 'B':c_rcvAS,'C':c_rcvBF,'D':c_rcvBS,'E':c_rcvCF, 'F':c_rcvCS,'G':c_rcvDF,'H':c_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlC)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count > 1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);

         # Prepare the data
         query_args = { 'date': rcvH, 'time':rcvSR,'A':d_rcvAF, 'B':d_rcvAS,'C':d_rcvBF,'D':d_rcvBS,'E':d_rcvCF, 'F':d_rcvCS,'G':d_rcvDF,'H':d_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlD)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);

         # Prepare the data
         query_args = { 'date': rcvH, 'time':rcvSR,'A':e_rcvAF, 'B':e_rcvAS,'C':e_rcvBF,'D':e_rcvBS,'E':e_rcvCF, 'F':e_rcvCS,'G':e_rcvDF,'H':e_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlE)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);
         
          # Prepare the data
         query_args = { 'date': rcvH, 'time':rcvSR,'A':f_rcvAF, 'B':f_rcvAS,'C':f_rcvBF,'D':f_rcvBS,'E':f_rcvCF, 'F':f_rcvCS,'G':f_rcvDF,'H':f_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlF)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);
          # Prepare the data
         query_args = { 'date': rcvH, 'time':rcvSR,'A':g_rcvAF, 'B':g_rcvAS,'C':g_rcvBF,'D':g_rcvBS,'E':g_rcvCF, 'F':g_rcvCS,'G':g_rcvDF,'H':g_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlG)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);

         query_args = { 'date': rcvH, 'time':rcvSR,'A':h_rcvAF, 'B':h_rcvAS,'C':h_rcvBF,'D':h_rcvBS,'E':h_rcvCF, 'F':h_rcvCS,'G':h_rcvDF,'H':h_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlH)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
              if count >1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);
         #os.system("sudo reboot")


         query_args = { 'date': rcvH, 'time':rcvSR,'A':i_rcvAF, 'B':i_rcvAS,'C':i_rcvBF,'D':i_rcvBS,'E':i_rcvCF, 'F':i_rcvCS,'G':i_rcvDF,'H':i_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlI)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
                   FlagSleep =1
              if count > 1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);


         query_args = { 'date': rcvH, 'time':rcvSR,'A':j_rcvAF, 'B':j_rcvAS,'C':j_rcvBF,'D':j_rcvBS,'E':j_rcvCF, 'F':j_rcvCS,'G':j_rcvDF,'H':j_rcvDS}
         # This urlencodes your data (that's why we need to import urllib at the top)
         data = urllib.urlencode(query_args)
         # Send HTTP POST request
         FlagSave =1
         count =0
         while (FlagSave == 1) :
              count=count+1
              try :
                   c = pycurl.Curl()
                   c.setopt(c.URL,urlJ)
                   c.setopt(c.POSTFIELDS, data)
                   c.perform()
                   c.close()
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','1',device))
                   conn.commit()
                   time.sleep (500.0 / 1000.0)
                   FlagSave =0
              except:
                   print 'write to server error..try again'
                   curs.execute("""UPDATE device SET date=%s,time=%s,B=%s,C=%s,D=%s,status=%s WHERE A=%s""",(rcvH,rcvSR,'humid','1','1','0',device))
                   conn.commit()
                   time.sleep (3)
                   FlagSleep =1
              if count > 1 :
                   FlagSave =0
         
         time.sleep (500.0 / 1000.0);
          
         count_ValueError=0

         rcvAF = 0      #recieve A Data Second part
         rcvAS = 0      #recieve A Data Second part
         rcvBF = 0    #recieve B Data First part
         rcvBS = 0    #recieve B Data Second part
         rcvCF = 0      #recieve A Data Second part
         rcvCS = 0      #recieve A Data Second part
         rcvDF = 0    #recieve B Data First part
         rcvDS = 0    #recieve B Data Second part

         a_rcvAF = 0      #recieve A Data Second part
         a_rcvAS = 0      #recieve A Data Second part
         a_rcvBF = 0    #recieve B Data First part
         a_rcvBS = 0    #recieve B Data Second part
         a_rcvCF = 0      #recieve A Data Second part
         a_rcvCS = 0      #recieve A Data Second part
         a_rcvDF = 0    #recieve B Data First part
         a_rcvDS = 0    #recieve B Data Second part

         b_rcvAF = 0      #recieve A Data First part
         b_rcvAS = 0      #recieve A Data Second part
         b_rcvBF = 0    #recieve B Data First part
         b_rcvBS = 0    #recieve B Data Second part
         b_rcvCF = 0      #recieve A Data First part
         b_rcvCS = 0      #recieve A Data Second part
         b_rcvDF = 0    #recieve B Data First part
         b_rcvDS = 0    #recieve B Data Second part

         c_rcvAF = 0      #recieve A Data First part
         c_rcvAS = 0      #recieve A Data Second part
         c_rcvBF = 0    #recieve B Data First part
         c_rcvBS = 0    #recieve B Data Second part
         c_rcvCF = 0      #recieve A Data First part
         c_rcvCS = 0      #recieve A Data Second part
         c_rcvDF = 0    #recieve B Data First part
         c_rcvDS = 0    #recieve B Data Second part



         d_rcvAF = 0      #recieve A Data First part
         d_rcvAS = 0      #recieve A Data Second part
         d_rcvBF = 0    #recieve B Data First part
         d_rcvBS = 0    #recieve B Data Second part
         d_rcvCF = 0      #recieve A Data First part
         d_rcvCS = 0      #recieve A Data Second part
         d_rcvDF = 0    #recieve B Data First part
         d_rcvDS = 0    #recieve B Data Second part


         e_rcvAF = 0      #recieve A Data First part
         e_rcvAS = 0      #recieve A Data Second part
         e_rcvBF = 0    #recieve B Data First part
         e_rcvBS = 0    #recieve B Data Second part
         e_rcvCF = 0      #recieve A Data First part
         e_rcvCS = 0      #recieve A Data Second part
         e_rcvDF = 0    #recieve B Data First part
         e_rcvDS = 0    #recieve B Data Second part



         f_rcvAF = 0      #recieve A Data First part
         f_rcvAS = 0      #recieve A Data Second part
         f_rcvBF = 0    #recieve B Data First part
         f_rcvBS = 0    #recieve B Data Second part
         f_rcvCF = 0      #recieve A Data First part
         f_rcvCS = 0      #recieve A Data Second part
         f_rcvDF = 0    #recieve B Data First part
         f_rcvDS = 0    #recieve B Data Second part

         g_rcvAF = 0      #recieve A Data First part
         g_rcvAS = 0      #recieve A Data Second part
         g_rcvBF = 0    #recieve B Data First part
         g_rcvBS = 0    #recieve B Data Second part
         g_rcvCF = 0      #recieve A Data First part
         g_rcvCS = 0      #recieve A Data Second part
         g_rcvDF = 0    #recieve B Data First part
         g_rcvDS = 0    #recieve B Data Second part


         h_rcvAF = 0      #recieve A Data First part
         h_rcvAS = 0      #recieve A Data Second part
         h_rcvBF = 0    #recieve B Data First part
         h_rcvBS = 0    #recieve B Data Second part
         h_rcvCF = 0      #recieve A Data First part
         h_rcvCS = 0      #recieve A Data Second part
         h_rcvDF = 0    #recieve B Data First part
         h_rcvDS = 0    #recieve B Data Second part


         i_rcvAF = 0      #recieve A Data First part
         i_rcvAS = 0      #recieve A Data Second part
         i_rcvBF = 0    #recieve B Data First part
         i_rcvBS = 0    #recieve B Data Second part
         i_rcvCF = 0      #recieve A Data First part
         i_rcvCS = 0      #recieve A Data Second part
         i_rcvDF = 0    #recieve B Data First part
         i_rcvDS = 0    #recieve B Data Second part


         j_rcvAF = 0      #recieve A Data First part
         j_rcvAS = 0      #recieve A Data Second part
         j_rcvBF = 0    #recieve B Data First part
         j_rcvBS = 0    #recieve B Data Second part
         j_rcvCF = 0      #recieve A Data First part
         j_rcvCS = 0      #recieve A Data Second part
         j_rcvDF = 0    #recieve B Data First part
         j_rcvDS = 0    #recieve B Data Second part

         m_rcvAF = 0      #recieve A Data First part
         m_rcvAS = 0      #recieve A Data Second part
         m_rcvBF = 0    #recieve B Data First part
         m_rcvBS = 0    #recieve B Data Second part
         m_rcvCF = 0      #recieve A Data First part
         m_rcvCS = 0      #recieve A Data Second part
         m_rcvDF = 0    #recieve B Data First part
         m_rcvDS = 0    #recieve B Data Second part

         v_rcvAF = 0      #recieve A Data First part
         v_rcvAS = 0      #recieve A Data Second part
         v_rcvBF = 0    #recieve B Data First part
         v_rcvBS = 0    #recieve B Data Second part
         v_rcvCF = 0      #recieve A Data First part
         v_rcvCS = 0      #recieve A Data Second part
         v_rcvDF = 0    #recieve B Data First part
         v_rcvDS = 0    #recieve B Data Second part
           

         a2_rcvAF = 0      #recieve A Data Second part
         a2_rcvAS = 0      #recieve A Data Second part
         a2_rcvBF = 0    #recieve B Data First part
         a2_rcvBS = 0    #recieve B Data Second part
         a2_rcvCF = 0      #recieve A Data Second part
         a2_rcvCS = 0      #recieve A Data Second part
         a2_rcvDF = 0    #recieve B Data First part
         a2_rcvDS = 0    #recieve B Data Second part

         b2_rcvAF = 0      #recieve A Data First part
         b2_rcvAS = 0      #recieve A Data Second part
         b2_rcvBF = 0    #recieve B Data First part
         b2_rcvBS = 0    #recieve B Data Second part
         b2_rcvCF = 0      #recieve A Data First part
         b2_rcvCS = 0      #recieve A Data Second part
         b2_rcvDF = 0    #recieve B Data First part
         b2_rcvDS = 0    #recieve B Data Second part

         c2_rcvAF = 0      #recieve A Data First part
         c2_rcvAS = 0      #recieve A Data Second part
         c2_rcvBF = 0    #recieve B Data First part
         c2_rcvBS = 0    #recieve B Data Second part
         c2_rcvCF = 0      #recieve A Data First part
         c2_rcvCS = 0      #recieve A Data Second part
         c2_rcvDF = 0    #recieve B Data First part
         c2_rcvDS = 0    #recieve B Data Second part



         d2_rcvAF = 0      #recieve A Data First part
         d2_rcvAS = 0      #recieve A Data Second part
         d2_rcvBF = 0    #recieve B Data First part
         d2_rcvBS = 0    #recieve B Data Second part
         d2_rcvCF = 0      #recieve A Data First part
         d2_rcvCS = 0      #recieve A Data Second part
         d2_rcvDF = 0    #recieve B Data First part
         d2_rcvDS = 0    #recieve B Data Second part


         e2_rcvAF = 0      #recieve A Data First part
         e2_rcvAS = 0      #recieve A Data Second part
         e2_rcvBF = 0    #recieve B Data First part
         e2_rcvBS = 0    #recieve B Data Second part
         e2_rcvCF = 0      #recieve A Data First part
         e2_rcvCS = 0      #recieve A Data Second part
         e2_rcvDF = 0    #recieve B Data First part
         e2_rcvDS = 0    #recieve B Data Second part

         f2_rcvAF = 0      #recieve A Data First part
         f2_rcvAS = 0      #recieve A Data Second part
         f2_rcvBF = 0    #recieve B Data First part
         f2_rcvBS = 0    #recieve B Data Second part
         f2_rcvCF = 0      #recieve A Data First part
         f2_rcvCS = 0      #recieve A Data Second part
         f2_rcvDF = 0    #recieve B Data First part
         f2_rcvDS = 0    #recieve B Data Second part

         g2_rcvAF = 0      #recieve A Data First part
         g2_rcvAS = 0      #recieve A Data Second part
         g2_rcvBF = 0    #recieve B Data First part
         g2_rcvBS = 0    #recieve B Data Second part
         g2_rcvCF = 0      #recieve A Data First part
         g2_rcvCS = 0      #recieve A Data Second part
         g2_rcvDF = 0    #recieve B Data First part
         g2_rcvDS = 0    #recieve B Data Second part


         h2_rcvAF = 0      #recieve A Data First part
         h2_rcvAS = 0      #recieve A Data Second part
         h2_rcvBF = 0    #recieve B Data First part
         h2_rcvBS = 0    #recieve B Data Second part
         h2_rcvCF = 0      #recieve A Data First part
         h2_rcvCS = 0      #recieve A Data Second part
         h2_rcvDF = 0    #recieve B Data First part
         h2_rcvDS = 0    #recieve B Data Second part                   


         cAA=0
         cAB=0
         cAC=0
         cAD=0
         cBA=0
         cBB=0
         cBC=0
         cBD=0
         cCA=0
         cCB=0
         cCC=0
         cCD=0
         cDA=0
         cDB=0
         cDC=0
         cDD=0
         cEA=0
         cEB=0
         cEC=0
         cED=0
         cFA=0
         cFB=0
         cFC=0
         cFD=0
         cGA=0
         cGB=0
         cGC=0
         cGD=0
         
    else:
         #ser.write('\r\n ')
         pprint.pprint('Time :'+ str(now.hour) + ':'+str(now.minute)+':'+str(now.second))
         
         TimeToSave = 10-(now.minute % 10)
         pprint.pprint('waiting '+str(TimeToSave) + ' minute for next record')
    
############################################################################    
    
    from time import strftime
    rcvH=strftime("%d-%m-")
    rcvSR=strftime("%H:%M:%S ")
    #strOutput = strHeader+'0'+strhour+strminute+'B'+'00000'+'#'
    if strHeader == "PSA" :
        strOutput = strHeader+'0'+str(now.hour)+str(now.minute)+'B'+'00000'+'#'
        
    else :
        strOutput = "Pt"+rcvH+"19"+" "+rcvSR
    serialflag =0 
    while serialflag < 10 :
        serialflag=serialflag+1
        print serialflag
        try:
            ser.close()
            time.sleep(0.1) 
            #serialflag =1 
            ser.open()
            ser.write(strOutput)
            pprint.pprint('Send Time : '+strOutput)
            serialflag = 100 
               
    
        except:
            print 'ERROR : Port open '
            time.sleep(0.1) 
            
    
    time.sleep(0.1)
    try :
        ser.flushInput()
        ser.flushOutput()
        time.sleep(0.1)
        rcv = read_serial(ser)
    except :
        print "ERROR read serial"
    length = len(rcv)
    if length >5 :
        pprint.pprint(rcv)
        rcvH = rcv[0]       #recieve Header
        rcvSR = rcv[1]      #recieve SerialNumber
        pprint.pprint('RPI DATA: ' + rcvH+' - '+rcvSR)#+' - '+rcvAH +' - '+rcvAF+' - '+rcvAS +' --Recieved')
    if rcvSR == 'S':
        strHeader = "PTA"
    pprint.pprint(' Nodata ='+ str(nodata))
    

        
    if rcv == '' :
         #h_rcvAF =str(nodata)
         nodata = nodata+1
         time.sleep (1);
         
    
        
         if nodata > 500 :
             rcvH=strftime("%Y-%m-%d ")
             rcvSR=strftime("%H:%M:%S ")
             query_args = { 'date': rcvH, 'time':rcvSR,'A':h_rcvAF, 'B':h_rcvAS,'C':h_rcvBF,'D':h_rcvBS,'E':h_rcvCF, 'F':h_rcvCS,'G':h_rcvDF,'H':h_rcvDS}
             # This urlencodes your data (that's why we need to import urllib at the top)
             data = urllib.urlencode(query_args)
             # Send HTTP POST request
             try :
                 c = pycurl.Curl()
                 c.setopt(c.URL,urlstatus)
                 c.setopt(c.POSTFIELDS, data)
                 c.perform()
                 c.close()
             except:
                 print 'write to server error..try again'
             time.sleep (5);
             GPIO.setwarnings(False)
             GPIO.setmode(GPIO.BCM)
             GPIO.setup(17, GPIO.IN)
             GPIO.setup(18, GPIO.OUT)
             GPIO.setup(23, GPIO.OUT)
             input_value = GPIO.input(17)
             GPIO.output(18, GPIO.HIGH)
             GPIO.output(23, GPIO.HIGH)
             time.sleep (10);
             GPIO.output(23, GPIO.LOW)
              
    else :
         nodata =0
         pprint.pprint('nodata=0')
    pprint.pprint('rcvH='+ rcvH)
    pprint.pprint('rcvSR='+ rcvSR)
    rcvSep =';'
    if rcvH == 'P' :   #Check Header P
         #ser.write('\r\n Correct Header ---- P ')
         pprint.pprint('Correct Header ---- P ')
         if length > 26 :   #Check Serial Number
              #client.publish("/tmec01/input",timestamp+","+rcv)
               
              #ser.write('\r\n Get Separator')
              pprint.pprint(' Get Separator')
              if rcvSR  == 'A' : #Check A Header
                   a=ord(rcv[2])+ord(rcv[3])
                   pprint.pprint('a = '+str(a))


                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        a_rcvAF = ord(rcv[2])<<8
                        a_rcvAF = a_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(a_rcvAF))
                        ax_rcvAF=a_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        a_rcvAS = ord(rcv[5])<<8
                        a_rcvAS = a_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(a_rcvAS))
                        ax_rcvAS=a_rcvAS
                        
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        a_rcvBF = ord(rcv[8])<<8
                        a_rcvBF = a_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(a_rcvBF))
                        ax_rcvBF=a_rcvBF
                        
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        a_rcvBS = ord(rcv[11])<<8
                        a_rcvBS = a_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(a_rcvBS) )       
                        ax_rcvBS=a_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        a_rcvCF = ord(rcv[14])<<8
                        a_rcvCF = a_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(a_rcvCF))
                        ax_rcvCF=a_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        a_rcvCS = ord(rcv[17])<<8
                        a_rcvCS = a_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( a_rcvCS))
                        ax_rcvCS=a_rcvCS



                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        a_rcvDF = ord(rcv[20])<<8
                        a_rcvDF = a_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(a_rcvDF))
                        ax_rcvDF=a_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        a_rcvDS = ord(rcv[23])<<8
                        a_rcvDS = a_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( a_rcvDS))
                        ax_rcvDS=a_rcvDS
   #######################################################################################################################  
              if rcvSR  == 'B' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        b_rcvAF = ord(rcv[2])<<8
                        b_rcvAF = b_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(b_rcvAF))
                        bx_rcvAF=b_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        b_rcvAS = ord(rcv[5])<<8
                        b_rcvAS = b_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(b_rcvAS))
                        bx_rcvAS=b_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        b_rcvBF = ord(rcv[8])<<8
                        b_rcvBF = b_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(b_rcvBF))
                        bx_rcvBF=b_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        b_rcvBS = ord(rcv[11])<<8
                        b_rcvBS = b_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(b_rcvBS) )       
                        bx_rcvBS=b_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        b_rcvCF = ord(rcv[14])<<8
                        b_rcvCF = b_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(b_rcvCF))
                        bx_rcvCF=b_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        b_rcvCS = ord(rcv[17])<<8
                        b_rcvCS = b_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( b_rcvCS))
                        bx_rcvCS=b_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        b_rcvDF = ord(rcv[20])<<8
                        b_rcvDF = b_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(b_rcvDF))
                        bx_rcvDF=b_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        b_rcvDS = ord(rcv[23])<<8
                        b_rcvDS = b_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( b_rcvDS))
                        bx_rcvDS =b_rcvDS
   #######################################################################################################################
               #######################################################################################################################  
              if rcvSR  == 'C' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        c_rcvAF = ord(rcv[2])<<8
                        c_rcvAF = c_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(c_rcvAF))
                        cx_rcvAF=c_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        c_rcvAS = ord(rcv[5])<<8
                        c_rcvAS = c_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(c_rcvAS))
                        cx_rcvAS=c_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        c_rcvBF = ord(rcv[8])<<8
                        c_rcvBF = c_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(c_rcvBF))
                        cx_rcvBF=c_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        c_rcvBS = ord(rcv[11])<<8
                        c_rcvBS = c_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(c_rcvBS) )       
                        cx_rcvBS=c_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        c_rcvCF = ord(rcv[14])<<8
                        c_rcvCF = c_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(c_rcvCF))
                        cx_rcvCF=c_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        c_rcvCS = ord(rcv[17])<<8
                        c_rcvCS = c_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( c_rcvCS))
                        cx_rcvCS=c_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        c_rcvDF = ord(rcv[20])<<8
                        c_rcvDF = c_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(c_rcvDF))
                        cx_rcvDF=c_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        c_rcvDS = ord(rcv[23])<<8
                        c_rcvDS = c_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( c_rcvDS))
                        cx_rcvDS =c_rcvDS
   #######################################################################################################################
               #######################################################################################################################  
              if rcvSR  == 'D' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        d_rcvAF = ord(rcv[2])<<8
                        d_rcvAF = d_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(d_rcvAF))
                        dx_rcvAF=d_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        d_rcvAS = ord(rcv[5])<<8
                        d_rcvAS = d_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(d_rcvAS))
                        dx_rcvAS=d_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        d_rcvBF = ord(rcv[8])<<8
                        d_rcvBF = d_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(d_rcvBF))
                        dx_rcvBF=d_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        d_rcvBS = ord(rcv[11])<<8
                        d_rcvBS = d_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(d_rcvBS) )       
                        dx_rcvBS=d_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        d_rcvCF = ord(rcv[14])<<8
                        d_rcvCF = d_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(d_rcvCF))
                        dx_rcvCF=d_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        d_rcvCS = ord(rcv[17])<<8
                        d_rcvCS = d_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( d_rcvCS))
                        dx_rcvCS=d_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        d_rcvDF = ord(rcv[20])<<8
                        d_rcvDF = d_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(d_rcvDF))
                        dx_rcvDF=d_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        d_rcvDS = ord(rcv[23])<<8
                        d_rcvDS = d_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( d_rcvDS))
                        dx_rcvDS =d_rcvDS
                 #######################################################################################################################  
              if rcvSR  == 'E' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        e_rcvAF = ord(rcv[2])<<8
                        e_rcvAF = e_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(e_rcvAF))
                        ex_rcvAF=e_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        e_rcvAS = ord(rcv[5])<<8
                        e_rcvAS = e_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(e_rcvAS))
                        ex_rcvAS=e_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        e_rcvBF = ord(rcv[8])<<8
                        e_rcvBF = e_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(e_rcvBF))
                        ex_rcvBF=e_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        e_rcvBS = ord(rcv[11])<<8
                        e_rcvBS = e_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(e_rcvBS) )       
                        ex_rcvBS=e_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        e_rcvCF = ord(rcv[14])<<8
                        e_rcvCF = e_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(e_rcvCF))
                        ex_rcvCF=e_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        e_rcvCS = ord(rcv[17])<<8
                        e_rcvCS = e_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( e_rcvCS))
                        ex_rcvCS=e_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        e_rcvDF = ord(rcv[20])<<8
                        e_rcvDF = e_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(e_rcvDF))
                        ex_rcvDF=e_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        e_rcvDS = ord(rcv[23])<<8
                        e_rcvDS = e_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( e_rcvDS))
                        ex_rcvDS =e_rcvDS
                #######################################################################################################################  
              if rcvSR  == 'F' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        f_rcvAF = ord(rcv[2])<<8
                        f_rcvAF = f_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(f_rcvAF))
                        fx_rcvAF=f_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        f_rcvAS = ord(rcv[5])<<8
                        f_rcvAS = f_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(f_rcvAS))
                        fx_rcvAS=f_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        f_rcvBF = ord(rcv[8])<<8
                        f_rcvBF = f_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(f_rcvBF))
                        fx_rcvBF=f_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        f_rcvBS = ord(rcv[11])<<8
                        f_rcvBS = f_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(f_rcvBS) )       
                        fx_rcvBS=f_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        f_rcvCF = ord(rcv[14])<<8
                        f_rcvCF = f_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(f_rcvCF))
                        fx_rcvCF=f_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        f_rcvCS = ord(rcv[17])<<8
                        f_rcvCS = f_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( f_rcvCS))
                        fx_rcvCS=f_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        f_rcvDF = ord(rcv[20])<<8
                        f_rcvDF = f_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(f_rcvDF))
                        fx_rcvDF=f_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        f_rcvDS = ord(rcv[23])<<8
                        f_rcvDS = f_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( f_rcvDS))
                        fx_rcvDS =f_rcvDS                    
   #######################################################################################################################
                             #######################################################################################################################  
              if rcvSR  == 'G' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        g_rcvAF = ord(rcv[2])<<8
                        g_rcvAF = g_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(g_rcvAF))
                        gx_rcvAF=g_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        g_rcvAS = ord(rcv[5])<<8
                        g_rcvAS = g_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(g_rcvAS))
                        gx_rcvAS=g_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        g_rcvBF = ord(rcv[8])<<8
                        g_rcvBF = g_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(g_rcvBF))
                        gx_rcvBF=g_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        g_rcvBS = ord(rcv[11])<<8
                        g_rcvBS = g_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(g_rcvBS) )       
                        gx_rcvBS=g_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        g_rcvCF = ord(rcv[14])<<8
                        g_rcvCF = g_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(g_rcvCF))
                        gx_rcvCF=g_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        g_rcvCS = ord(rcv[17])<<8
                        g_rcvCS = g_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( g_rcvCS))
                        gx_rcvCS=g_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        g_rcvDF = ord(rcv[20])<<8
                        g_rcvDF = g_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(g_rcvDF))
                        gx_rcvDF=g_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        g_rcvDS = ord(rcv[23])<<8
                        g_rcvDS = g_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( g_rcvDS))
                        gx_rcvDS =g_rcvDS                    
   ###
                          #######################################################################################################################  
              if rcvSR  == 'H' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        h_rcvAF = ord(rcv[2])<<8
                        h_rcvAF = h_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(h_rcvAF))
                        hx_rcvAF=h_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        h_rcvAS = ord(rcv[5])<<8
                        h_rcvAS = h_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(h_rcvAS))
                        hx_rcvAS=h_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        h_rcvBF = ord(rcv[8])<<8
                        h_rcvBF = h_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(h_rcvBF))
                        hx_rcvBF=h_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        h_rcvBS = ord(rcv[11])<<8
                        h_rcvBS = h_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(h_rcvBS) )       
                        hx_rcvBS=h_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        h_rcvCF = ord(rcv[14])<<8
                        h_rcvCF = h_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(h_rcvCF))
                        hx_rcvCF=h_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        h_rcvCS = ord(rcv[17])<<8
                        h_rcvCS = h_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( h_rcvCS))
                        hx_rcvCS=h_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        h_rcvDF = ord(rcv[20])<<8
                        h_rcvDF = h_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(h_rcvDF))
                        hx_rcvDF=h_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        h_rcvDS = ord(rcv[23])<<8
                        h_rcvDS = h_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( h_rcvDS))
                        hx_rcvDS =h_rcvDS                    
   ################################################################################################################# 
              

              if rcvSR  == 'M' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        m_rcvAF = ord(rcv[2])<<8
                        m_rcvAF = m_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        m_rcvAF = (float(m_rcvAF))/100      #recieve A Data Second part
                        m_rcvAF = format(m_rcvAF, '.2f')
                        pprint.pprint('Get A '+str(m_rcvAF))
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        m_rcvAS = ord(rcv[5])<<8
                        m_rcvAS = m_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        m_rcvAS = (float(m_rcvAS))/100      #recieve A Data Second part
                        m_rcvAS = format(m_rcvAS, '.2f')
                        pprint.pprint('Get B '+str(m_rcvAS))
                        
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        m_rcvBF = ord(rcv[8])<<8
                        m_rcvBF = m_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        m_rcvBF = (float(m_rcvBF))/100      #recieve A Data Second part
                        m_rcvBF = format(m_rcvBF, '.2f')
                        pprint.pprint('Get C '+str(m_rcvBF))
                        
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        m_rcvBS = ord(rcv[11])<<8
                        m_rcvBS = m_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(m_rcvBS) )       



                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        m_rcvCF = ord(rcv[14])<<8
                        m_rcvCF = m_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        m_rcvCF = (float(m_rcvCF))/100      #recieve A Data Second part
                        m_rcvCF = format(m_rcvCF, '.2f')
                        pprint.pprint('Get E '+str(m_rcvCF))
                        
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        m_rcvCS = ord(rcv[17])<<8
                        m_rcvCS = m_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( m_rcvCS))



                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        m_rcvDF = ord(rcv[20])<<8
                        m_rcvDF = m_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(m_rcvDF))
                        
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        m_rcvDS = ord(rcv[23])<<8
                        m_rcvDS = m_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        m_rcvDS = (float(m_rcvDS))/10      #recieve A Data Second part
                        m_rcvDS = format(m_rcvDS, '.2f')
                        pprint.pprint('Get H '+str( m_rcvDS))        
     
                   
              ####################################################################################################
                             #######################################################################################################################  
              if rcvSR  == 'I' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        i_rcvAF = ord(rcv[2])<<8
                        i_rcvAF = i_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(i_rcvAF))
                        ix_rcvAF=i_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        i_rcvAS = ord(rcv[5])<<8
                        i_rcvAS = i_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(i_rcvAS))
                        ix_rcvAS=i_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        i_rcvBF = ord(rcv[8])<<8
                        i_rcvBF = i_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(i_rcvBF))
                        ix_rcvBF=i_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        i_rcvBS = ord(rcv[11])<<8
                        i_rcvBS = i_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(i_rcvBS) )       
                        ix_rcvBS=i_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        i_rcvCF = ord(rcv[14])<<8
                        i_rcvCF = i_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(i_rcvCF))
                        ix_rcvCF=i_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        i_rcvCS = ord(rcv[17])<<8
                        i_rcvCS = i_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( i_rcvCS))
                        ix_rcvCS=i_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        i_rcvDF = ord(rcv[20])<<8
                        i_rcvDF = i_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(i_rcvDF))
                        ix_rcvDF=i_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        i_rcvDS = ord(rcv[23])<<8
                        i_rcvDS = i_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( i_rcvDS))
                        ix_rcvDS =i_rcvDS                    
   ###
                          #######################################################################################################################  
              if rcvSR  == 'J' : #Check A Header
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        j_rcvAF = ord(rcv[2])<<8
                        j_rcvAF = j_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(j_rcvAF))
                        jx_rcvAF=j_rcvAF
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        j_rcvAS = ord(rcv[5])<<8
                        j_rcvAS = j_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(j_rcvAS))
                        jx_rcvAS=j_rcvAS
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        j_rcvBF = ord(rcv[8])<<8
                        j_rcvBF = j_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(j_rcvBF))
                        jx_rcvBF=j_rcvBF
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        j_rcvBS = ord(rcv[11])<<8
                        j_rcvBS = j_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(j_rcvBS) )       
                        jx_rcvBS=j_rcvBS


                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        j_rcvCF = ord(rcv[14])<<8
                        j_rcvCF = j_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(j_rcvCF))
                        jx_rcvCF=j_rcvCF
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        j_rcvCS = ord(rcv[17])<<8
                        j_rcvCS = j_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str( j_rcvCS))
                        jx_rcvCS=j_rcvCS


                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        j_rcvDF = ord(rcv[20])<<8
                        j_rcvDF = j_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(j_rcvDF))
                        jx_rcvDF=j_rcvDF
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        j_rcvDS = ord(rcv[23])<<8
                        j_rcvDS = j_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( j_rcvDS))
                        jx_rcvDS =j_rcvDS                    
   ######################################################################### 
             

              if rcvSR  == 'V' : #Check A Header
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvDS = ord(rcv[23])<<8
                        v_rcvDS = v_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( v_rcvDS))
                   #if v_rcvDS < 5000 :
                   #     rcvSR  = 'v'
                       


                        
              if rcvSR  == 'V' : #Check A Header
                   
                                      
                   a=ord(rcv[2])+ord(rcv[3])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256
                   if a == ord(rcv[4]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvAF = ord(rcv[2])<<8
                        v_rcvAF = v_rcvAF+ord(rcv[3])-1000      #recieve A Data First part
                        pprint.pprint('Get A '+str(v_rcvAF))
                        
                   a=ord(rcv[5])+ord(rcv[6])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[7]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvAS = ord(rcv[5])<<8
                        v_rcvAS = v_rcvAS+ord(rcv[6])-1000      #recieve B Data First part
                        pprint.pprint('Get B '+str(v_rcvAS))
                        
                   a=ord(rcv[8])+ord(rcv[9])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256

                   if a == ord(rcv[10]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvBF = ord(rcv[8])<<8
                        v_rcvBF = v_rcvBF+ord(rcv[9])-1000      #recieve C Data First part
                        pprint.pprint('Get C '+str(v_rcvBF))
                        
                   a=ord(rcv[11])+ord(rcv[12])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[13]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvBS = ord(rcv[11])<<8
                        v_rcvBS = v_rcvBS+ord(rcv[12])-1000      #recieve D Data First part
                        pprint.pprint('Get D '+str(v_rcvBS) )       



                   a=ord(rcv[14])+ord(rcv[15])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[16]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvCF = ord(rcv[14])<<8
                        v_rcvCF = v_rcvCF+ord(rcv[15])-1000      #recieve C Data First part
                        pprint.pprint('Get E '+str(v_rcvCF))
                        
                   a=ord(rcv[17])+ord(rcv[18])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[19]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvCS = ord(rcv[17])<<8
                        v_rcvCS = v_rcvCS+ord(rcv[18])-1000      #recieve D Data First part
                        pprint.pprint('Get F '+str(v_rcvCS))



                   a=ord(rcv[20])+ord(rcv[21])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if a == ord(rcv[22]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvDF = ord(rcv[20])<<8
                        v_rcvDF = v_rcvDF+ord(rcv[21])-1000      #recieve C Data First part
                        pprint.pprint('Get G '+ str(v_rcvDF))
                        
                   a=ord(rcv[23])+ord(rcv[24])
                   #pprint.pprint('a = '+str(a))
                   #pprint.pprint('rcv[4] = '+str(ord(rcv[4])))
                   if  a > 255:
                       a= a-256                   
                   a=ord(rcv[1])+a
                   if a>255:
                       a= a-256
                   if  a == ord(rcv[25]):
                        #ser.write('\r\n Get A Group')
                        
                        v_rcvDS = ord(rcv[23])<<8
                        v_rcvDS = v_rcvDS+ord(rcv[24])-1000      #recieve D Data First part
                        pprint.pprint('Get H '+str( v_rcvDS))
                        

              

              else :
                   #ser.write('\r\n INCorrect subHeader')
                   pprint.pprint('INCorrect subHeader')

         else :
              #ser.write('\r\n INCorrect Separator')
              pprint.pprint('INCorrect Separator')
              
             
    else:
         #Incorrect Header
         #ser.write('\r\n INCorrect Header')
         pprint.pprint('RPI INCorrect Header')
         #ser.write('\r\n P1A111:2222')
         #pprint.pprint('P1A111:2222')
    from time import strftime
    rcvH=strftime("%Y-%m-%d ")
    timestamp=strftime("%H:%M:%S ")
    
    if rcvSR == 'A':
        MQTTmain=timestamp+","+"A"+","+str(a_rcvAF)+","+str(a_rcvAS)+","+str(a_rcvBF)+","+str(a_rcvBS)+","+str(a_rcvCF)+","+str(a_rcvCS)+","+str(a_rcvDF)+","+str(a_rcvDS)

    if rcvSR == 'B':
        MQTTmain=timestamp+","+"B"+","+str(b_rcvAF)+","+str(b_rcvAS)+","+str(b_rcvBF)+","+str(b_rcvBS)+","+str(b_rcvCF)+","+str(b_rcvCS)+","+str(b_rcvDF)+","+str(b_rcvDS)
                  
    if rcvSR == 'C':
        MQTTmain=timestamp+","+"C"+","+str(c_rcvAF)+","+str(c_rcvAS)+","+str(c_rcvBF)+","+str(c_rcvBS)+","+str(c_rcvCF)+","+str(c_rcvCS)+","+str(c_rcvDF)+","+str(b_rcvDS)
     
    if rcvSR == 'V':
        MQTTmain=timestamp+","+"V"+","+str(v_rcvAF)+","+str(v_rcvAS)+","+str(v_rcvBF)+","+str(v_rcvBS)+","+str(v_rcvCF)+","+str(v_rcvCS)+","+str(v_rcvDF)+","+str(v_rcvDS)
       
    if  connectMQTT == 1 :
        if len(MQTTmain) > 10 :
            publish_mqtt(MQTTmain)
            print 'MQTTmain:'+MQTTmain
            time.sleep(1)
            MQTTmain=""
        
    else :
        try :
            clientMQTT = mqtt.Client()
            clientMQTT.on_connect = on_connect
            clientMQTT.on_message = on_message
            clientMQTT.connect("127.0.0.1")
            clientMQTT.loop_start()
            connectMQTT =1
        except Exception as err:
            print 'Error: ', err     

         
    if connect == 1 :
       
        if m_rcvAF > 0 :
             temp = m_rcvAF      #recieve A Data Second part

        if m_rcvAS > 0 :
             humid = m_rcvAS      #recieve A Data Second part
        if m_rcvBF > 0 :
             rain = m_rcvBF    #recieve B Data First part
        if m_rcvBS > 0 :
             winds = m_rcvBS    #recieve B Data Second part
        if m_rcvCF > 0 :
             windd = m_rcvCF      #recieve A Data Second part
        if m_rcvCS > 0 :
             mois1 = m_rcvCS      #recieve A Data Second part
        if m_rcvDF > 0 :
             mois2 = m_rcvDF    #recieve B Data First part
        if m_rcvDS > 0 :
             lux = m_rcvDS    #recieve B Data Second part 
        
        if a_rcvAF > 0 :
             ax_rcvAF = a_rcvAF      #recieve A Data Second part

        if a_rcvAS > 0 :
             ax_rcvAS = a_rcvAS      #recieve A Data Second part
        if a_rcvBF > 0 :
             ax_rcvBF = a_rcvBF    #recieve B Data First part
        if a_rcvBS > 0 :
             ax_rcvBS = a_rcvBS    #recieve B Data Second part
        if a_rcvCF > 0 :
             ax_rcvCF = a_rcvCF      #recieve A Data Second part
        if a_rcvCS > 0 :
             ax_rcvCS = a_rcvCS      #recieve A Data Second part
        if a_rcvDF > 0 :
             ax_rcvDF = a_rcvDF    #recieve B Data First part
        if a_rcvDS > 0 :
             ax_rcvDS = a_rcvDS    #recieve B Data Second part

        if b_rcvAF > 0 :
             bx_rcvAF = b_rcvAF      #recieve A Data First part
        if b_rcvAS > 0 :
             bx_rcvAS = b_rcvAS      #recieve A Data Second part
        if b_rcvBF > 0 :
             bx_rcvBF = b_rcvBF    #recieve B Data First part
        if b_rcvBS > 0 :
             bx_rcvBS = b_rcvBS    #recieve B Data Second part
        if b_rcvCF > 0 :
             bx_rcvCF = b_rcvCF      #recieve A Data First part
        if b_rcvCS > 0 :
             bx_rcvCS = b_rcvCS      #recieve A Data Second part
        if b_rcvDF > 0 :
             bx_rcvDF = b_rcvDF    #recieve B Data First part
        if b_rcvDS > 0 :
             bx_rcvDS = b_rcvDS    #recieve B Data Second part

        if c_rcvAF > 0 :
             cx_rcvAF = c_rcvAF      #recieve A Data First part
        if c_rcvAS > 0 :
             cx_rcvAS = c_rcvAS      #recieve A Data Second part
        if c_rcvBF > 0 :
             cx_rcvBF = c_rcvBF    #recieve B Data First part
        if c_rcvBS > 0 :
             cx_rcvBS = c_rcvBS    #recieve B Data Second part
        if c_rcvCF > 0 :
             cx_rcvCF = c_rcvCF      #recieve A Data First part
        if c_rcvCS > 0 :
             cx_rcvCS = c_rcvCS      #recieve A Data Second part
        if c_rcvDF > 0 :
             cx_rcvDF = c_rcvDF    #recieve B Data First part
        if c_rcvDS > 0 :
             cx_rcvDS = c_rcvDS    #recieve B Data Second part



        if d_rcvAF > 0 :
             dx_rcvAF = d_rcvAF      #recieve A Data First part
        if d_rcvAS > 0 :
             dx_rcvAS = d_rcvAS      #recieve A Data Second part
        if d_rcvBF > 0 :
             dx_rcvBF = d_rcvBF    #recieve B Data First part
        if d_rcvBS > 0 :
             dx_rcvBS = d_rcvBS    #recieve B Data Second part
        if d_rcvCF > 0 :
             dx_rcvCF = d_rcvCF      #recieve A Data First part
        if d_rcvCS > 0 :
             dx_rcvCS = d_rcvCS      #recieve A Data Second part
        if d_rcvDF > 0 :
             dx_rcvDF = d_rcvDF    #recieve B Data First part
        if d_rcvDS > 0 :
             dx_rcvDS = d_rcvDS    #recieve B Data Second part
                            

        if e_rcvAF > 0 :
             ex_rcvAF = e_rcvAF      #recieve A Data Second part

        if e_rcvAS > 0 :
             ex_rcvAS = e_rcvAS      #recieve A Data Second part
        if e_rcvBF > 0 :
             ex_rcvBF = e_rcvBF    #recieve B Data First part
        if e_rcvBS > 0 :
             ex_rcvBS = e_rcvBS    #recieve B Data Second part
        if e_rcvCF > 0 :
             ex_rcvCF = e_rcvCF      #recieve A Data Second part
        if e_rcvCS > 0 :
             ex_rcvCS = e_rcvCS      #recieve A Data Second part
        if e_rcvDF > 0 :
             ex_rcvDF = e_rcvDF    #recieve B Data First part
        if e_rcvDS > 0 :
             ex_rcvDS = e_rcvDS    #recieve B Data Second part

        if f_rcvAF > 0 :
             fx_rcvAF = f_rcvAF      #recieve A Data First part
        if f_rcvAS > 0 :
             fx_rcvAS = f_rcvAS      #recieve A Data Second part
        if f_rcvBF > 0 :
             fx_rcvBF = f_rcvBF    #recieve B Data First part
        if f_rcvBS > 0 :
             fx_rcvBS = f_rcvBS    #recieve B Data Second part
        if f_rcvCF > 0 :
             fx_rcvCF = f_rcvCF      #recieve A Data First part
        if f_rcvCS > 0 :
             fx_rcvCS = f_rcvCS      #recieve A Data Second part
        if f_rcvDF > 0 :
             fx_rcvDF = f_rcvDF    #recieve B Data First part
        if f_rcvDS > 0 :
             fx_rcvDS = f_rcvDS    #recieve B Data Second part

        if g_rcvAF > 0 :
             gx_rcvAF = g_rcvAF      #recieve A Data First part
        if g_rcvAS > 0 :
             gx_rcvAS = g_rcvAS      #recieve A Data Second part
        if g_rcvBF > 0 :
             gx_rcvBF = g_rcvBF    #recieve B Data First part
        if g_rcvBS > 0 :
             gx_rcvBS = g_rcvBS    #recieve B Data Second part
        if g_rcvCF > 0 :
             gx_rcvCF = g_rcvCF      #recieve A Data First part
        if g_rcvCS > 0 :
             gx_rcvCS = g_rcvCS      #recieve A Data Second part
        if g_rcvDF > 0 :
             gx_rcvDF = g_rcvDF    #recieve B Data First part
        if g_rcvDS > 0 :
             gx_rcvDS = g_rcvDS    #recieve B Data Second part



        if h_rcvAF > 0 :
             hx_rcvAF = h_rcvAF      #recieve A Data First part
        if h_rcvAS > 0 :
             hx_rcvAS = h_rcvAS      #recieve A Data Second part
        if h_rcvBF > 0 :
             hx_rcvBF = h_rcvBF    #recieve B Data First part
        if h_rcvBS > 0 :
             hx_rcvBS = h_rcvBS    #recieve B Data Second part
        if h_rcvCF > 0 :
             hx_rcvCF = h_rcvCF      #recieve A Data First part
        if h_rcvCS > 0 :
             hx_rcvCS = h_rcvCS      #recieve A Data Second part
        if h_rcvDF > 0 :
             hx_rcvDF = h_rcvDF    #recieve B Data First part
        if h_rcvDS > 0 :
             hx_rcvDS = h_rcvDS    #recieve B Data Second part


        if i_rcvAF > 0 :
             ix_rcvAF = i_rcvAF      #recieve A Data First part
        if i_rcvAS > 0 :
             ix_rcvAS = i_rcvAS      #recieve A Data Second part
        if i_rcvBF > 0 :
             ix_rcvBF = i_rcvBF    #recieve B Data First part
        if i_rcvBS > 0 :
             ix_rcvBS = i_rcvBS    #recieve B Data Second part
        if i_rcvCF > 0 :
             ix_rcvCF = i_rcvCF      #recieve A Data First part
        if i_rcvCS > 0 :
             ix_rcvCS = i_rcvCS      #recieve A Data Second part
        if i_rcvDF > 0 :
             ix_rcvDF = i_rcvDF    #recieve B Data First part
        if i_rcvDS > 0 :
             ix_rcvDS = i_rcvDS    #recieve B Data Second part
             

        if j_rcvAF > 0 :
             jx_rcvAF = j_rcvAF      #recieve A Data First part
        if j_rcvAS > 0 :
             jx_rcvAS = j_rcvAS      #recieve A Data Second part
        if j_rcvBF > 0 :
             jx_rcvBF = j_rcvBF    #recieve B Data First part
        if j_rcvBS > 0 :
             jx_rcvBS = j_rcvBS    #recieve B Data Second part
        if j_rcvCF > 0 :
             jx_rcvCF = j_rcvCF      #recieve A Data First part
        if j_rcvCS > 0 :
             jx_rcvCS = j_rcvCS      #recieve A Data Second part
        if j_rcvDF > 0 :
             jx_rcvDF = j_rcvDF    #recieve B Data First part
        if j_rcvDS > 0 :
             jx_rcvDS = j_rcvDS    #recieve B Data Second part

        
        clientcount=clientcount+1
        

        if length > 10:
            client.publish("/wimarc/station",timestamp+","+str(temp)+","+str(humid)+","+str(rain)+","+str(winds)+","+str(windd)+","+str(mois1)+","+str(mois2)+","+str(lux))
            time.sleep(1)
        if rcvSR == 'A':
            clientcount=0 
            time.sleep(0.5)
            client.publish("/wimarc/AB",timestamp+","+str(ax_rcvAF)+","+str(ax_rcvAS)+","+str(ax_rcvBF)+","+str(ax_rcvBS)+","+str(ax_rcvCF)+","+str(ax_rcvCS)+","+str(ax_rcvDF)+","+str(ax_rcvDS)+\
            ","+str(bx_rcvAF)+","+str(bx_rcvAS)+","+str(bx_rcvBF)+","+str(bx_rcvBS)+","+str(bx_rcvCF)+","+str(bx_rcvCS)+","+str(bx_rcvDF)+","+str(bx_rcvDS))
  
        if rcvSR == 'B':
            clientcount=0 
            #client.publish("/wimarc/A",timestamp+","+str(ax_rcvAF)+","+str(ax_rcvAS)+","+str(ax_rcvBF)+","+str(ax_rcvBS)+","+str(ax_rcvCF)+","+str(ax_rcvCS)+","+str(ax_rcvDF)+","+str(ax_rcvDS))
            time.sleep(0.5)
            client.publish("/wimarc/AB",timestamp+","+str(ax_rcvAF)+","+str(ax_rcvAS)+","+str(ax_rcvBF)+","+str(ax_rcvBS)+","+str(ax_rcvCF)+","+str(ax_rcvCS)+","+str(ax_rcvDF)+","+str(ax_rcvDS)+\
            ","+str(bx_rcvAF)+","+str(bx_rcvAS)+","+str(bx_rcvBF)+","+str(bx_rcvBS)+","+str(bx_rcvCF)+","+str(bx_rcvCS)+","+str(bx_rcvDF)+","+str(bx_rcvDS))
  
        
        if rcvSR == 'C':
            clientcount=0 
            client.publish("/wimarc/CD",timestamp+","+str(cx_rcvAF)+","+str(cx_rcvAS)+","+str(cx_rcvBF)+","+str(cx_rcvBS)+","+str(cx_rcvCF)+","+str(cx_rcvCS)+","+str(cx_rcvDF)+","+str(cx_rcvDS)+\
            ","+str(dx_rcvAF)+","+str(dx_rcvAS)+","+str(dx_rcvBF)+","+str(dx_rcvBS)+","+str(dx_rcvCF)+","+str(dx_rcvCS)+","+str(dx_rcvDF)+","+str(dx_rcvDS))
            time.sleep(1)
        if rcvSR == 'D':
            clientcount=0 
            client.publish("/wimarc/CD",timestamp+","+str(cx_rcvAF)+","+str(cx_rcvAS)+","+str(cx_rcvBF)+","+str(cx_rcvBS)+","+str(cx_rcvCF)+","+str(cx_rcvCS)+","+str(cx_rcvDF)+","+str(cx_rcvDS)+\
            ","+str(dx_rcvAF)+","+str(dx_rcvAS)+","+str(dx_rcvBF)+","+str(dx_rcvBS)+","+str(dx_rcvCF)+","+str(dx_rcvCS)+","+str(dx_rcvDF)+","+str(dx_rcvDS))
            time.sleep(1)
            
        if rcvSR == 'E':
            clientcount=0 
            client.publish("/wimarc/EF",timestamp+","+str(ex_rcvAF)+","+str(ex_rcvAS)+","+str(ex_rcvBF)+","+str(ex_rcvBS)+","+str(ex_rcvCF)+","+str(ex_rcvCS)+","+str(ex_rcvDF)+","+str(ex_rcvDS)+\
            ","+str(fx_rcvAF)+","+str(fx_rcvAS)+","+str(fx_rcvBF)+","+str(fx_rcvBS)+","+str(fx_rcvCF)+","+str(fx_rcvCS)+","+str(fx_rcvDF)+","+str(fx_rcvDS))
            time.sleep(1)
        if rcvSR == 'F':
            clientcount=0 
            client.publish("/wimarc/EF",timestamp+","+str(ex_rcvAF)+","+str(ex_rcvAS)+","+str(ex_rcvBF)+","+str(ex_rcvBS)+","+str(ex_rcvCF)+","+str(ex_rcvCS)+","+str(ex_rcvDF)+","+str(ex_rcvDS)+\
            ","+str(fx_rcvAF)+","+str(fx_rcvAS)+","+str(fx_rcvBF)+","+str(fx_rcvBS)+","+str(fx_rcvCF)+","+str(fx_rcvCS)+","+str(fx_rcvDF)+","+str(fx_rcvDS))
            time.sleep(1)
            
        if rcvSR == 'G':
            clientcount=0 
            client.publish("/wimarc/GH",timestamp+","+str(gx_rcvAF)+","+str(gx_rcvAS)+","+str(gx_rcvBF)+","+str(gx_rcvBS)+","+str(gx_rcvCF)+","+str(gx_rcvCS)+","+str(gx_rcvDF)+","+str(gx_rcvDS)+\
            ","+str(hx_rcvAF)+","+str(hx_rcvAS)+","+str(hx_rcvBF)+","+str(hx_rcvBS)+","+str(hx_rcvCF)+","+str(hx_rcvCS)+","+str(hx_rcvDF)+","+str(hx_rcvDS))
            time.sleep(1)
            
        if rcvSR == 'H':
            clientcount=0 
            client.publish("/wimarc/GH",timestamp+","+str(gx_rcvAF)+","+str(gx_rcvAS)+","+str(gx_rcvBF)+","+str(gx_rcvBS)+","+str(gx_rcvCF)+","+str(gx_rcvCS)+","+str(gx_rcvDF)+","+str(gx_rcvDS)+\
            ","+str(hx_rcvAF)+","+str(hx_rcvAS)+","+str(hx_rcvBF)+","+str(hx_rcvBS)+","+str(hx_rcvCF)+","+str(hx_rcvCS)+","+str(hx_rcvDF)+","+str(hx_rcvDS))
            time.sleep(1)
            
        if rcvSR == 'I':
            clientcount=0 
            client.publish("/wimarc/IJ",timestamp+","+str(ix_rcvAF)+","+str(ix_rcvAS)+","+str(ix_rcvBF)+","+str(ix_rcvBS)+","+str(ix_rcvCF)+","+str(ix_rcvCS)+","+str(ix_rcvDF)+","+str(ix_rcvDS)+\
            ","+str(jx_rcvAF)+","+str(jx_rcvAS)+","+str(jx_rcvBF)+","+str(jx_rcvBS)+","+str(jx_rcvCF)+","+str(jx_rcvCS)+","+str(jx_rcvDF)+","+str(jx_rcvDS))
            time.sleep(1)
            
        if rcvSR == 'J':
            clientcount=0 
            client.publish("/wimarc/IJ",timestamp+","+str(ix_rcvAF)+","+str(ix_rcvAS)+","+str(ix_rcvBF)+","+str(ix_rcvBS)+","+str(ix_rcvCF)+","+str(ix_rcvCS)+","+str(ix_rcvDF)+","+str(ix_rcvDS)+\
            ","+str(jx_rcvAF)+","+str(jx_rcvAS)+","+str(jx_rcvBF)+","+str(jx_rcvBS)+","+str(jx_rcvCF)+","+str(jx_rcvCS)+","+str(jx_rcvDF)+","+str(jx_rcvDS))
            time.sleep(1)
        if rcvSR == 'V':
            clientcount=0
            client.publish("/OPASstationA/sensor",str(v_rcvAF)+";"+str(v_rcvAS)+";"+str(v_rcvBF)+";"+str(v_rcvBS)+";"+str(v_rcvCF)+";"+str(v_rcvCS)+";"+str(v_rcvDF)+";"+str(v_rcvDS))
            #";"+str(jx_rcvAF)+";"+str(jx_rcvAS)+";"+str(jx_rcvBF)+";"+str(jx_rcvBS)+";"+str(jx_rcvCF)+";"+str(jx_rcvCS)+";"+str(jx_rcvDF)+";"+str(jx_rcvDS))
            time.sleep(1)
            client.publish("/wimarc/volt",timestamp+","+str(v_rcvAF)+","+str(v_rcvAS)+","+str(v_rcvBF)+","+str(v_rcvBS)+","+str(v_rcvCF)+","+str(v_rcvCS)+","+str(v_rcvDF)+","+str(v_rcvDS))
            #","+str(jx_rcvAF)+","+str(jx_rcvAS)+","+str(jx_rcvBF)+","+str(jx_rcvBS)+","+str(jx_rcvCF)+","+str(jx_rcvCS)+","+str(jx_rcvDF)+","+str(jx_rcvDS))
            time.sleep(1)
            
               
    else :
        print "connecting netpie"
        
        time.sleep(1)
        try:
            client.create(gearkey,gearsecret,appid,{'debugmode': True})
            time.sleep(1)
            
            client.setalias("wimarc")
            time.sleep(1)
            client.on_connect = connection
            time.sleep(1)
            client.on_message = subscription
            time.sleep(1)
            client.resettoken()
            time.sleep(1)
            client.connect(False)
            time.sleep(1)
            connect =1
            connectcount=0
            client.subscribe("/wimarc/station")
        except :
            print "No netpie"
            connectcount=connectcount+1
            
