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
import paramiko,sys
import pysftp
import RPi.GPIO as GPIO
import logging
import smbus
import base64
import cv2
import zmq
import numpy as np

camera = cv2.VideoCapture(0)  # init the camera


headerfilename='wimarc'




writepath = '/media/usb0/data.txt'

writepathlocal = '/home/pi/data.txt'

from time import strftime
rcvH=strftime("%Y-%m-%d ")
rcvSR=strftime("%H:%M:%S ")
lastTime = datetime.datetime.now()
recordLastTime = lastTime.minute



devicename = 'wimarc'

urlimage='https://opasnectec.000webhostapp.com/Insertpic.php/'

save=0
imagecount =0
imagerecord=1
while save == 0 :

#### record image here
    from time import strftime
    rcvH=strftime("%Y%m%d")
    Hour=int(strftime("%H"))
    headertime=strftime("%H:%M:%S ")
    if Hour > 24 :
             imagerecord = 0
    if Hour < 0 :
             imagerecord = 0
             
    if imagerecord == 1 :
         #camera.release()
         if Hour > 19 :
             imagerecord = 0
             

         rcvSR=strftime("H%H")
         filename = rcvSR+'.jpg'
         #filename = rcvH+rcvSR+'.jpg'
         if filename == 'H12.jpg' :
              filename = rcvH+rcvSR+'.jpg'
              
              
         try :
              print filename
              ret, frame = camera.read()
              removefile = 'sudo rm '+filename
              os.system(removefile)
              start_point = (0, 460) 
              end_point = (640,480 )
                # Blue color in BGR 
              color = (255, 0, 0)
              # Line thickness of 2 px 
              thickness = -1
              cv2.imwrite(filename, frame)
              source = cv2.imread(filename)
                   #source = cv2.rectangle(source, start_point, end_point, color, thickness) 

              font = cv2.FONT_HERSHEY_SIMPLEX
            
              cv2.putText(source,str(headerfilename), (2, 15), font, 0.5, (200, 200, 200), 2)
              
              cv2.putText(source,str(headertime), (500, 15), font, 0.5, (200, 200, 200), 2)
              cv2.imwrite(filename,source)
              cv2.imwrite('/var/www/html/ESP32CAM.jpg',source)
              #date = 'sudo fswebcam -S 100 -r 1280x720 '+filename
              #print date
              #a = 'sudo fswebcam image.jpg'
              #time.sleep (5);
              #os.system(date)
              #time.sleep (5)
              import subprocess
              from SimpleCV import Image
              img = Image(filename)

              pixel0 = img[10, 200]
              #print pixel0
              pixel1 = img[100, 200]
              #print pixel1
              if pixel0 == pixel1 :
                   #imagereord =0
                   imagecount = imagecount+1
                   if imagecount > 3 :
                        #imagerecord =0
                        imagecount =0
                        FlagSleep =1
                        #camera = cv2.VideoCapture(1)  # init the camera
                   print 'image file failed'
                   #uploadfile = 'sudo ncftpput -u opasnectec.orgfree.com  -p opas4870 opasnectec.orgfree.com /images '+filename
                   #os.system(uploadfile)
              else :
                   imagerecord =0
                   #camera = cv2.VideoCapture(1)  # init the camera
                   imagecount =0 
                   print 'image file ok'
                   #data = open(filename,'rb').read()
                   #r = requests.post(urlimage,data=data)
                   
                   
                   #os.system(removefile)
                   FlagSleep =1
                   
         except:
              print 'send file error.'

              FlagSleep =1

         #filename ='/var/www/html/ESP32CAM.jpg'
         #filename ='/home/pi/test.jpg'
    try :
         print (filename)
         import os
         import requests
         import pycurl
         from StringIO import StringIO

         import requests
         import os
 
         #function send_data_to_server(image_path, temperature):
         
         import requests
         #from requests_toolbelt.multipart.encoder import MultipartEncoder
         
         buffer = StringIO()
         f=open(filename, "rb")
         if f.mode == 'rb':
            data =f.read()
            #print contents
         url = urlimage
         c = pycurl.Curl()
         c.setopt(c.URL,urlimage)
         c.setopt(c.POSTFIELDS, data)
         c.setopt(c.WRITEFUNCTION, buffer.write)
    
         c.perform()
   
        
         c.close()
         body = buffer.getvalue()
         print(body)
         time.sleep(5)
         imagerecord=1
    except :
         print ('upload image failed.....')
