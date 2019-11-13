//0106 timedelay depend on loracount



#include <SoftwareSerial.h> //Include the library
#include <Wire.h>

//Click here to get the library: http://librarymanager/All#SparkFun_SCD30
#include "SparkFun_SCD30_Arduino_Library.h" 


int intCO2,inttemp,inthumid;

SCD30 airSensor;
SoftwareSerial nextion(8,7); // RX, TX
int voltref=503;
int voltoffset=0;
float reftime =0;

int minState=0;
boolean flagSend = true;

int i,j;
int Ptcount=0;
#define rxPin 12
#define txPin 11


long Tempvoltage,Luxvoltage,Lux;

int v1,v2,v3,v4,v5,v6,v7,v8;



unsigned long lastvalue;
unsigned long Supvoltage,RHvoltage,Windvoltage;
unsigned long RH = 0;
int sensorPin = 1; 
//int loopcount;
int inputcount=0;


int relayPin = 4; //output pin 13

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
boolean FlagShutdown=false;
boolean FlagStart=false;
int RHint;
long temp;

boolean flagairsensor=false;

int inputlight=0;
boolean flaglight = false;



void setup() {

///////////////////////
 Wire.begin();
  Serial.begin(9600);
Serial.println("SCD30 Example");
 /////////////////////////////////
airSensor.begin(); //This will cause readings to occur every two seconds
  delay(1000);
  pinMode(3, INPUT);
  inputlight = digitalRead(3);
 if (inputlight == LOW)
 { flaglight = true;
  } 

 

  delay(1000);
  pinMode(relayPin, OUTPUT); // output
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);digitalWrite(6, HIGH);
  pinMode(9, OUTPUT);digitalWrite(9, HIGH);
   
 

  Supvoltage = analogRead(7);
 Supvoltage = Supvoltage*voltref;
Supvoltage = Supvoltage/102.3-voltoffset;
//Supvoltage = Supvoltage*11;

 reftime =millis();
/////////////////
nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("p0.pic=6");
  //nextion.print("1"); //You don't need this
  //nextion.print("\""); //Or this
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("img END");
nextion.end(); 

delay(3000);  
nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("p0.pic=8");
  //nextion.print("1"); //You don't need this
  //nextion.print("\""); //Or this
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("img END");
nextion.end();  

  
}

void loop() {


 if (airSensor.dataAvailable())
  { flagairsensor = true;
    Serial.print("co2(ppm):");
    intCO2=(int) airSensor.getCO2();
    Serial.print(intCO2);

    Serial.print(" temp(C):");
    inttemp= (int)(airSensor.getTemperature()*100);
    Serial.print(inttemp);

    Serial.print(" humidity(%):");
    inthumid=(int) (airSensor.getHumidity()*100);
    Serial.print(inthumid);

    Serial.println();
  }
  else
    Serial.println("No data");

  delay(1000);

///////////////////////////////////////

// lastvalue=Luxvoltage;
Luxvoltage = analogRead(2); 

Serial.print(Luxvoltage);

 Luxvoltage = Luxvoltage*voltref;
Luxvoltage = Luxvoltage/102.3-voltoffset;
 
    //Luxvoltage = (Luxvoltage+lastvalue)/2;
     Lux = (Luxvoltage*14) /50;
  Serial.print("Light  ="); 
 
 
 Serial.print(Lux);
 Serial.println(" Lux");

 lastvalue=Supvoltage;

  Supvoltage = analogRead(7);
 Supvoltage = Supvoltage*voltref;
Supvoltage = Supvoltage/102.3-voltoffset;
//Supvoltage = Supvoltage*11+700;
 

 
   Supvoltage = (Supvoltage+lastvalue)/2;
   
  Serial.print("Supply  ="); 
 
 
 Serial.print(Supvoltage,1);
 Serial.println("V");
//////////////////////////////////////////

  delay(100);

 
//////////////////////////////////////////
if (flagairsensor) 
{  
  float val=inttemp/100.0;
   Serial.print("Temp:");Serial.println(val);
  char buff[10];
  dtostrf(val, 4, 1, buff); 
  
  // We change the txt value of text box t0
  nextion.print("t0.txt=\"");
  nextion.print(String(buff));
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
///////////////////////////////////////////////////////
  val=inthumid/100.0;
  Serial.print("Humid:");Serial.println(val);
  buff[10];
  dtostrf(val, 4, 1, buff); 
  // We change the txt value of text box t0
  nextion.print("t1.txt=\"");
  nextion.print(String(buff));
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
  v4= intCO2;
   // We change the txt value of text box t0
  nextion.print("t3.txt=\"");
  nextion.print(String(v4));
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
}
else
{
 inttemp=0;
 inthumid=0;
 intCO2=0; 
  
}


  if (flaglight)
  {
   v3=Lux; 
    // We change the txt value of text box t0
  nextion.print("t2.txt=\"");
  nextion.print(String(v3));
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
  }
 else 
 {
  
  Lux=0;
  }

nextion.end(); 


}



  


 
