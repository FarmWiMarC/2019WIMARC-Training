//0106 timedelay depend on loracount

#include <SPI.h>
#include <LoRa.h>
////////////////

#include <SoftwareSerial.h> //Include the library
#include <Wire.h>

//Click here to get the library: http://librarymanager/All#SparkFun_SCD30
#include "SparkFun_SCD30_Arduino_Library.h" 

char rfID='A';
long freq =924E6;

int intCO2,inttemp,inthumid;

SCD30 airSensor;
SoftwareSerial nextion(8,7); // RX, TX

//sps30
int ret;
u8 auto_clean_days = 4;
u32 auto_clean;
int intpm25;

///////////////


int counter = 0;
int loopcount=0;
int packetSize=0;

int timedelay=180;


int e;
int loracount=0;



int minState=0;
boolean flagSend = true;

int i,j;
int Ptcount=0;

#define LORA_RESET 9
char InputRS232[40];
int ValueMT1,ValueMT2,ValueMT3,ValueMT4;

long Tempvoltage,Luxvoltage;
long Lux;
int v1,v2,v3,v4,v5,v6,v7,v8;
char ID;
char myVariable;
int bitIwantToCheck;
boolean isBitSet = (myVariable & (1 << bitIwantToCheck)) ? true : false;
//Addresses

//mois
float M;


int angle;
float OldTime;
int voltref=503;
int voltoffset=0;
float timecount =0;
float reftime =0;
char InputRPI[30];
char ValueSensor[50];

int indexchar;

unsigned long lastvalue;
unsigned long Supvoltage,RHvoltage,Windvoltage;
unsigned long RH = 0;
int sensorPin = 1; 
//int loopcount;
int inputcount=0;


byte CurrentDisplayPage = 0;
int relayPin = 4; //output pin 13

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
boolean FlagShutdown=false;
boolean FlagStart=false;
int RHint;
long temp;

/////////////////////////////////////////////////////////////
/////////////Serial
////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////

boolean ConvertData_CheckModeID(int measPoint)
{char i,data[3],checkchar;
 boolean FlagSearch;
 int tmp;
 char  Data1,Data2,Data3,Data4,Data5;
 int tmp1,tmp2;

 
 FlagSearch =1;i=0;//k=0;

//char x=InputRS232[1]+InputRS232[4]+InputRS232[7]+InputRS232[10]+InputRS232[13]+InputRS232[16]+InputRS232[19]+InputRS232[22]+InputRS232[25]+InputRS232[28]+InputRS232[31];
char x=InputRS232[1]+InputRS232[4]+InputRS232[7]+InputRS232[10]+InputRS232[13]+InputRS232[16]+InputRS232[19]+InputRS232[22]+InputRS232[25];
Serial.print("Input ="); Serial.println(InputRS232[26]);
Serial.print("check ="); Serial.println(x);
   if (InputRS232[26] != x)    {
//    char x =InputRS232[5]+InputRS232[8]+InputRS232[1]+InputRS232[2];
    
    delay(1000);
    
    return false;  
  } 
return true;




 
 
 
 
 
}





////////////////////////////////////////////////
/////////////Convert data send with LORA
///////////////////


void ProcessSendLORA(char idex)
{ 
int i;
int Data1,Data2,Data3;
   int tmp;
char sum1,sum2,sum3,sum4,sum5,sum6,sum7,sum8,sum9,sum10;
ValueSensor[0] = 'P';
ValueSensor[1] = idex;
//////////////////v1 Send
 

 
 tmp =v1+1000; 
  tmp = tmp & 0xff00;
  tmp >>= 8; 
  Data1 = tmp;

  
 tmp =v1+1000; 
 
  tmp = tmp & 0x00ff;
  Data2 = tmp;



  
sum1=idex+Data1+Data2;
Data3=Data1+Data2;


//Data1='A';

ValueSensor[2] = Data1;
ValueSensor[3] = Data2;
ValueSensor[4] = sum1;

//////////////////v2 Send
  tmp =v2+1000; 
  tmp = tmp & 0xff00;
  tmp >>= 8; 
  Data1 = tmp;

  
 tmp =v2+1000; 
 
  tmp = tmp & 0x00ff;
  Data2 = tmp;
  
sum2=idex+Data1+Data2;

Data3=Data1+Data2;
ValueSensor[5] = Data1;
ValueSensor[6] = Data2;
ValueSensor[7] = sum2;
//////////////////v3 Send
  tmp =v3+1000; 
  tmp = tmp & 0xff00;
  tmp >>= 8; 
  Data1 = tmp;

  
 tmp =v3+1000; 
 
  tmp = tmp & 0x00ff;
  Data2 = tmp;
sum3=idex+Data1+Data2;


Data3=Data1+Data2;

ValueSensor[8] = Data1;
ValueSensor[9] = Data2;
ValueSensor[10] = sum3;
//////////////////v4 Send
 tmp =v4+1000; 
  tmp = tmp & 0xff00;
  tmp >>= 8; 
  Data1 = tmp;

  
 tmp =v4+1000; 
 
  tmp = tmp & 0x00ff;
  Data2 = tmp;
sum4=idex+Data1+Data2;
Data3=Data1+Data2;
ValueSensor[11] = Data1;
ValueSensor[12] = Data2;
ValueSensor[13] =sum4;
//////////////////v5 Send
  tmp =v5+1000; 
  tmp = tmp & 0xff00;
  tmp >>= 8; 
  Data1 = tmp;

  
 tmp =v5+1000; 
 
  tmp = tmp & 0x00ff;
  Data2 = tmp;
sum5=idex+Data1+Data2;
Data3=Data1+Data2;
ValueSensor[14] = Data1;
ValueSensor[15] = Data2;
ValueSensor[16] = sum5;
//////////////////v6 Send
 tmp =v6+1000; 
  tmp = tmp & 0xff00;
  tmp >>= 8; 
  Data1 = tmp;

  
 tmp =v6+1000; 
 
  tmp = tmp & 0x00ff;
  Data2 = tmp;
sum6=idex+Data1+Data2;
Data3=Data1+Data2;
ValueSensor[17] = Data1;
ValueSensor[18] = Data2;
ValueSensor[19] =sum6;
//////////////////v7 Send
 tmp =v7+1000; 
  tmp = tmp & 0xff00;
  tmp >>= 8; 
  Data1 = tmp;

  
 tmp =v7+1000; 
 
  tmp = tmp & 0x00ff;
  Data2 = tmp;
sum7=idex+Data1+Data2;
Data3=Data1+Data2;
ValueSensor[20] = Data1;
ValueSensor[21] = Data2;
ValueSensor[22] = sum7;


//////////////////v8 Send
 tmp =v8+1000; 
  tmp = tmp & 0xff00;
  tmp >>= 8; 
  Data1 = tmp;

  
 tmp =v8+1000; 
 
  tmp = tmp & 0x00ff;
  Data2 = tmp;
sum8=idex+Data1+Data2;

Data3=Data1+Data2;
ValueSensor[23] = Data1;
ValueSensor[24] = Data2;
ValueSensor[25] = sum8;




ValueSensor[26]=ValueSensor[1]+ValueSensor[4]+ValueSensor[7]+ValueSensor[10]+ValueSensor[13]+ValueSensor[16]+ValueSensor[19]+ValueSensor[22]+ValueSensor[25];
//ValueSensor[32]=idex+sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8+sum9+sum10;//
 
//ValueSensor[27]='\n';

//for (i=1;i<30;i++) { Serial.print(ValueSensor[i],HEX); Serial.print(','); }   
for (i=0;i<5;i++){
  for (int j=0;j<30;j++)
  Serial.print(ValueSensor[j]); 
  Serial.println();
  delay(500);
}



}

boolean checkID()
{    Serial.println("..............................................................check ID");
     if (InputRS232[0] == 'I')
     {
      if (InputRS232[3]==(InputRS232[1]+InputRS232[2]))
        { 
          if( isBitSet = (InputRS232[1] & (1 << 3))) {ID='A';Serial.print("ID:A send"); if (ID==rfID) {return true;exit;}}
          //else {return false;exit;}  
          bitIwantToCheck=4;
          if( isBitSet = (InputRS232[1] & (1 << 2))) {ID='B';Serial.print("ID:B send"); if (ID==rfID) {return true;exit;}}
          //else {return false;exit;}
          bitIwantToCheck=4;
          if( isBitSet = (InputRS232[1] & (1 << 1))) {ID='C';Serial.print("ID:C send"); if (ID==rfID) {return true;exit;}}
          //else {return false;exit;}
          bitIwantToCheck=4;
          if( isBitSet = (InputRS232[1] & (1 << 0))) {ID='D';Serial.print("ID:D send"); if (ID==rfID) {return true;exit;}}
          //else {return false;exit;}
          if( isBitSet = (InputRS232[2] & (1 << 3))) {ID='E';Serial.print("ID:E send"); if (ID==rfID) {return true;exit;}}
          //else {return false;exit;}  
          bitIwantToCheck=4;
          if( isBitSet = (InputRS232[2] & (1 << 2))) {ID='F';Serial.print("ID:F send"); if (ID==rfID) {return true;exit;}}
          //else {return false;exit;}
          bitIwantToCheck=4;
          if( isBitSet = (InputRS232[2] & (1 << 1))) {ID='G';Serial.print("ID:G send"); if (ID==rfID) {return true;exit;}}
          //else {return false;exit;}
          bitIwantToCheck=4;
          if( isBitSet = (InputRS232[2] & (1 << 0))) {ID='H';Serial.print("ID:H send"); if (ID==rfID) {return true;exit;}}
        
        }
        
       Serial.print(rfID); Serial.println("...already sent" );
       nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print("Sent already");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
       
       return false;  
     }  
   else 
   {
   nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print("Sent already");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
   return false;
   }
}

boolean flagdust = false;
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

 


  
  Serial.begin(9600);
   pinMode(9, LORA_RESET);
  
  while (!Serial);
 
  Serial.println("LoRa Reciever.................");

  if (!LoRa.begin(freq)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  
  
  }

  LoRa.setTxPower(20);
/////////////////////////////////

 //Wind_Init();
 // Rain_Init();
  delay(1000);
  pinMode(relayPin, OUTPUT); // output
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);digitalWrite(6, HIGH);
  pinMode(9, OUTPUT);digitalWrite(9, HIGH);
 //  digitalWrite(relayPin, HIGH); // output pin 13
  loopcount=0;
 
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





  /////////////////////////////////////////////////////////
  
  





  
}

void loop() {

/////////////////////////////////////////////////

nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print(String(rfID)+String(freq/1E6));
  nextion.print("-update");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");

/////////////////////// 
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
  Serial.print("Lux  ="); 
 
 
 Serial.print(Luxvoltage);
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
// Serial.println();
   //   delay(3000);

 

 
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
  {// We change the txt value of text box t0
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
if (flagdust)
{  
 float  val=intpm25/100.0;
  Serial.print("PM2.5:");Serial.println(val);
  char buff[10];
  dtostrf(val, 4, 1, buff);
  
  // We change the txt value of text box t0
  nextion.print("t4.txt=\"");
  nextion.print(String(buff));
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
}
else
{
 intpm25=0; 
  
 }
nextion.end(); 


 //////////////read input///////////////////
v1=inttemp;        
v2=inthumid;            
v3=Lux;       
v4=intCO2;        
v5=intpm25;    
v6=0;       
v7=0;       
v8=Supvoltage;        

ProcessSendLORA(rfID);
  delay(1500);

Serial.print("Header:");Serial.println("V");
Serial.print("v1:");Serial.println(v1);
Serial.print("v2:");Serial.println(v2);
Serial.print("v3:");Serial.println(v3);
Serial.print("v4:");Serial.println(v4);
Serial.print("v5:");Serial.println(v5);
Serial.print("v6:");Serial.println(v6);
Serial.print("v7:");Serial.println(v7);
Serial.print("v8:");Serial.println(v8);

////////////////////////////////////////////

timecount = (millis()-reftime)/1000; 
Serial.print("timecount = "); Serial.println(timecount);
if (loracount > 5) {timedelay=300-loracount*10;if (timedelay<0) timedelay=300;}
if (timecount > timedelay)
 {  
  nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print("Sending");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
  for (int j=0;j<5;j++)
 {
 Serial.print("...........send rfID:");
 Serial.println(rfID);
  LoRa.beginPacket();
  LoRa.print(ValueSensor);
 // LoRa.print(counter);
  LoRa.endPacket();
  int randomdelay = random(500, 2000);
 Serial.println(randomdelay);
  delay(randomdelay);
 
 }
 reftime= millis();
 }
 
   //////////////////////////////////////////////////////////////
   
  // Supply measurement....................
 
 //////////////////////////////////////////////////////////////////
 
 
  lastvalue=Supvoltage;

  Supvoltage = analogRead(7);
 Supvoltage = Supvoltage*voltref;
Supvoltage = Supvoltage/102.3-voltoffset;
//Supvoltage = Supvoltage*11+700;
 

 
   Supvoltage = (Supvoltage+lastvalue)/2;
   
  Serial.print("Supply  ="); 
 
 
 Serial.print(Supvoltage,1);
 Serial.println("V");

 nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print("Waiting");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
 

  
//int packetSize = LoRa.parsePacket();
  Serial.print("waiting for Input packet loracount ");
  
    Serial.println(loracount);
    int loopnumber = 1000;
    if (loracount > 3) loopnumber = loracount*500;
    if (loopnumber > 20000) loopnumber = 20000;
  while ((packetSize == 0)&&(loopcount < loopnumber)) 
  {
 
  loopcount++;
    if(loopcount%100 == 0) Serial.print(".");
  
     packetSize = LoRa.parsePacket();
    // received a packet
  if ((packetSize > 0)&&(packetSize < 40))
  {
    Serial.print("Received packet '");

    // read packet
    int i=0;
    
    while (LoRa.available()) {
      InputRS232[i]=((char)LoRa.read());
      i++;
    }
   Serial.println(InputRS232);
   
    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
    Serial.print(" loopcount ");
    Serial.println(loopcount);
    Serial.print(" packetSize  ");
    Serial.println(packetSize);
    //loracount =0;

  if (checkID())
    {
    nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print("Sending");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
    for (int j=0;j<10;j++)
 {
 Serial.print("...........send rfID:");
 Serial.println(rfID);
  LoRa.beginPacket();
  LoRa.print(ValueSensor);
 // LoRa.print(counter);
  LoRa.endPacket();
  int randomdelay = random(500, 2000);
 Serial.println(randomdelay);
  delay(randomdelay);
 }
  loracount=0;   
    }


else{
    if (ConvertData_CheckModeID(0))
{
 nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print("Receive");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END"); 

 Serial.println(InputRS232);
 if (loracount >1) loracount--;
 }

 // loracount=0;  
  }
  }
  delay(10);
  }//while
  loracount++;
  Serial.print("loracounnt: ");Serial.println(loracount);
loopcount=0;
packetSize=0;
LoRa.sleep();
delay(random(3000, 5000));

if (loracount%6 == 0)
  {
   digitalWrite(LORA_RESET, LOW); // output pin 13
   delay(5000);
   digitalWrite(LORA_RESET, HIGH); // output pin 13
    if (!LoRa.begin(freq)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  
  
  }

  LoRa.setTxPower(20);
Serial.println("RESET LORA");
  
  }
if (loracount > 100)
  { digitalWrite(5, LOW); // output pin 13
    delay(5000);
    digitalWrite(5, HIGH);
     
  }
LoRa.sleep();
}



  


 
