#include <SPI.h>
#include <LoRa.h>
#include <SoftwareSerial.h> //Include the library
#include <Wire.h>
//Click here to get the library: http://librarymanager/All#SparkFun_SCD30
#include "SparkFun_SCD30_Arduino_Library.h" 

long freq=924E6;
SCD30 airSensor;
SoftwareSerial nextion(8,7); // RX, TX
//sps30
int ret;
u8 auto_clean_days = 4;
u32 auto_clean;
int intpm25;


int counter = 0;
int loopcount=0;
int packetSize=0;
char rfID='M';

int e;
int loracount=0;

char addr[8];
char netpiepublish[50];
//char timestate[30];
int minState=0;
int BitcheckA=0xFF;
int BitcheckB=0xFF;
boolean flagSend = true;

int i,j;
int Ptcount=0;

#define LORA_RESET 9
char InputRS232[40];
int ValueMT1,ValueMT2,ValueMT3,ValueMT4;
int intCO2,inttemp,inthumid;
long Tempvoltage,Luxvoltage,Lux;

int v1,v2,v3,v4,v5,v6,v7,v8;

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
//Rain gauge
unsigned long RainMeasurement = 0;
unsigned long LastRainReset = 0;
volatile byte Hit = 1;

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
void serialEvent() {
int i,j;     
      for (i=1;i<500;i++){ 
  char inChar = (char)Serial.read(); 
   
     if ((inChar == 'P')) 
     { InputRPI[0]=inChar;
    for (j=1;j<30;j++){  InputRPI[j] = Serial.read(); }  
//for (i=0;i<20;i++) { Serial.print(InputRPI[i],HEX); Serial.print(','); } Serial.println();
//Serial.println(InputRPI);


 
  if(( ((InputRPI[0] == 'P')&&(InputRPI[1] == 't'))&&(InputRPI[4] == '-')&&(InputRPI[7] == '-') )||((InputRPI[0] == 'P')&&((InputRPI[1] == 'T')||(InputRPI[1] == 'S'))))
  {
     stringComplete=true;
     
  
  i=1000;
  
   
      } // if 
     }  //if 
     }//for 
  

while (Serial.available()) 
     Serial.read();


  
}

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

   if (InputRS232[32] != x)    {
//    char x =InputRS232[5]+InputRS232[8]+InputRS232[1]+InputRS232[2];
    Serial.print("Input ="); Serial.println(InputRS232[26]);
    Serial.print("check ="); Serial.println(x);
    delay(1000);
    
  //  return false;  
  } 


 /////////////////v1  
  i=InputRS232[1];
  Data1=InputRS232[2];
  Data2=InputRS232[3];
  Data3=InputRS232[4];

  checkchar=i+Data1+Data2;
 if (Data3 == checkchar )
    {  v1 =0;
  tmp =Data1;
  tmp <<= 8;
  tmp &= 0xff00;//
  v1=Data2;
 
  v1 &= 0x00ff;
  v1 |= tmp;   
 
//v1=InputRS232[3]+InputRS232[4];
  v1-=1000;
tmp1 = v1/10000;                tmp2 = v1%10000; 
       Data1 = tmp1;
       tmp1 = tmp2/1000;                     tmp2 %= 1000;               
       Data2 = tmp1;
       tmp1 = tmp2/100;                     tmp2 %= 100;               
       Data3 = tmp1;
       tmp1 = tmp2/10;                     tmp2 %= 10;               
       Data4 = tmp1;
              
       Data5 = tmp2;
       
       Data1 += 0x30;  Data2 += 0x30;  Data3 += 0x30; Data4 += 0x30;  Data5 += 0x30;    
//ValueSensor[2] = 0x41; // "A"
netpiepublish[0] = Data1;
netpiepublish[1] = Data2;
netpiepublish[2] = Data3;
netpiepublish[3] = Data4;
netpiepublish[4] = Data5;
netpiepublish[5] = ';';

}

 // if (data[2] == (InputRS232[3]&&InputRS232[4]) )
 else { return false;}



 



/////////////////v2  
   Data1=InputRS232[5];
   Data2=InputRS232[6];
   Data3=InputRS232[7];

  checkchar=i+Data1+Data2;
 if (Data3 == checkchar )
 {
  v2 =0;
  tmp = Data1;
  tmp <<= 8;
  tmp &= 0xff00;//
  v2=Data2;
 
  v2 &= 0x00ff;
  v2 |= tmp;   
 
 v2-=1000;

tmp1 = v2/10000;                tmp2 = v2%10000; 
       Data1 = tmp1;
       tmp1 = tmp2/1000;                     tmp2 %= 1000;               
       Data2 = tmp1;
       tmp1 = tmp2/100;                     tmp2 %= 100;               
       Data3 = tmp1;
       tmp1 = tmp2/10;                     tmp2 %= 10;               
       Data4 = tmp1;
              
       Data5 = tmp2;
       
       Data1 += 0x30;  Data2 += 0x30;  Data3 += 0x30; Data4 += 0x30;  Data5 += 0x30;    
//ValueSensor[2] = 0x41; // "A"
netpiepublish[6] = Data1;
netpiepublish[7] = Data2;
netpiepublish[8] = Data3;
netpiepublish[9] = Data4;
netpiepublish[10] = Data5;
netpiepublish[11] = ';';

 }
 // if (data[2] == (InputRS232[3]&&InputRS232[4]) )
 else { return false;}

 
/////////////////v3  
    Data1=InputRS232[8];
    Data2=InputRS232[9];
    Data3=InputRS232[10];
   checkchar=i+Data1+Data2;
 if (Data3 == checkchar )
 {v3 =0;
  tmp =  Data1;
  tmp <<= 8;
  tmp &= 0xff00;//
  v3= Data2;
 
  v3 &= 0x00ff;
  v3 |= tmp;   
v3-=1000;
tmp1 = v3/10000;                tmp2 = v3%10000; 
       Data1 = tmp1;
       tmp1 = tmp2/1000;                     tmp2 %= 1000;               
       Data2 = tmp1;
       tmp1 = tmp2/100;                     tmp2 %= 100;               
       Data3 = tmp1;
       tmp1 = tmp2/10;                     tmp2 %= 10;               
       Data4 = tmp1;
              
       Data5 = tmp2;
       
       Data1 += 0x30;  Data2 += 0x30;  Data3 += 0x30; Data4 += 0x30;  Data5 += 0x30;    
//ValueSensor[2] = 0x41; // "A"
netpiepublish[12] = Data1;
netpiepublish[13] = Data2;
netpiepublish[14] = Data3;
netpiepublish[15] = Data4;
netpiepublish[16] = Data5;
netpiepublish[17] = ';';

 }
 // if (data[2] == (InputRS232[3]&&InputRS232[4]) )
 else { return false;}

/////////////////v4  
    Data1=InputRS232[11];
    Data2=InputRS232[12];
    Data3=InputRS232[13];
   checkchar=i+Data1+Data2;
 if (Data3 == checkchar )
 {v4 =0;
  tmp =  Data1;
  tmp <<= 8;
  tmp &= 0xff00;//
  v4= Data2;
 
  v4 &= 0x00ff;
  v4 |= tmp;   

 v4-=1000;

tmp1 = v4/10000;                tmp2 = v4%10000; 
       Data1 = tmp1;
       tmp1 = tmp2/1000;                     tmp2 %= 1000;               
       Data2 = tmp1;
       tmp1 = tmp2/100;                     tmp2 %= 100;               
       Data3 = tmp1;
       tmp1 = tmp2/10;                     tmp2 %= 10;               
       Data4 = tmp1;
              
       Data5 = tmp2;
       
       Data1 += 0x30;  Data2 += 0x30;  Data3 += 0x30; Data4 += 0x30;  Data5 += 0x30;    
//ValueSensor[2] = 0x41; // "A"
netpiepublish[18] = Data1;
netpiepublish[19] = Data2;
netpiepublish[20] = Data3;
netpiepublish[21] = Data4;
netpiepublish[22] = Data5;
netpiepublish[23] = ';';

 }
 // if (data[2] == (InputRS232[3]&&InputRS232[4]) )
 else { return false;}


/////////////////v5  
    Data1=InputRS232[14];
    Data2=InputRS232[15];
    Data3=InputRS232[16];
    checkchar=i+Data1+Data2;
 if (Data3 == checkchar )
 {v5 =0;
  tmp =  Data1;
  tmp <<= 8;
  tmp &= 0xff00;//
  v5= Data2;
 
  v5 &= 0x00ff;
  v5 |= tmp;   
 v5-=1000;
tmp1 = v5/10000;                tmp2 = v5%10000; 
       Data1 = tmp1;
       tmp1 = tmp2/1000;                     tmp2 %= 1000;               
       Data2 = tmp1;
       tmp1 = tmp2/100;                     tmp2 %= 100;               
       Data3 = tmp1;
       tmp1 = tmp2/10;                     tmp2 %= 10;               
       Data4 = tmp1;
              
       Data5 = tmp2;
       
       Data1 += 0x30;  Data2 += 0x30;  Data3 += 0x30; Data4 += 0x30;  Data5 += 0x30;    
//ValueSensor[2] = 0x41; // "A"
netpiepublish[24] = Data1;
netpiepublish[25] = Data2;
netpiepublish[26] = Data3;
netpiepublish[27] = Data4;
netpiepublish[28] = Data5;
netpiepublish[29] = ';';

 }
 // if (data[2] == (InputRS232[3]&&InputRS232[4]) )
 else { return false;}


/////////////////v6  
    Data1=InputRS232[17];
    Data2=InputRS232[18];
    Data3=InputRS232[19];
    checkchar=i+Data1+Data2;
 if (Data3 == checkchar )
 {v6 =0;
  tmp =  Data1;
  tmp <<= 8;
  tmp &= 0xff00;//
  v6= Data2;
 
  v6 &= 0x00ff;
  v6 |= tmp;   
 v6-=1000;
tmp1 = v6/10000;                tmp2 = v6%10000; 
       Data1 = tmp1;
       tmp1 = tmp2/1000;                     tmp2 %= 1000;               
       Data2 = tmp1;
       tmp1 = tmp2/100;                     tmp2 %= 100;               
       Data3 = tmp1;
       tmp1 = tmp2/10;                     tmp2 %= 10;               
       Data4 = tmp1;
              
       Data5 = tmp2;
       
       Data1 += 0x30;  Data2 += 0x30;  Data3 += 0x30; Data4 += 0x30;  Data5 += 0x30;    
//ValueSensor[2] = 0x41; // "A"
netpiepublish[30] = Data1;
netpiepublish[31] = Data2;
netpiepublish[32] = Data3;
netpiepublish[33] = Data4;
netpiepublish[34] = Data5;
netpiepublish[35] = ';';

 }
 // if (data[2] == (InputRS232[3]&&InputRS232[4]) )
 else { return false;}



/////////////////v7  
    Data1=InputRS232[20];
    Data2=InputRS232[21];
    Data3=InputRS232[22];
 checkchar=i+Data1+Data2;
 if (Data3 == checkchar )
 {v7 =0;
  tmp =  Data1;
  tmp <<= 8;
  tmp &= 0xff00;//
  v7= Data2;
 
  v7 &= 0x00ff;
  v7 |= tmp;   
 v7-=1000;
tmp1 = v7/10000;                tmp2 = v7%10000; 
       Data1 = tmp1;
       tmp1 = tmp2/1000;                     tmp2 %= 1000;               
       Data2 = tmp1;
       tmp1 = tmp2/100;                     tmp2 %= 100;               
       Data3 = tmp1;
       tmp1 = tmp2/10;                     tmp2 %= 10;               
       Data4 = tmp1;
              
       Data5 = tmp2;
       
       Data1 += 0x30;  Data2 += 0x30;  Data3 += 0x30; Data4 += 0x30;  Data5 += 0x30;    
//ValueSensor[2] = 0x41; // "A"
netpiepublish[36] = Data1;
netpiepublish[37] = Data2;
netpiepublish[38] = Data3;
netpiepublish[39] = Data4;
netpiepublish[40] = Data5;
netpiepublish[41] = ';';

 }
 // if (data[2] == (InputRS232[3]&&InputRS232[4]) )
 else { return false;}

/////////////////v8  
    Data1=InputRS232[23];
    Data2=InputRS232[24];
    Data3=InputRS232[25];
checkchar=i+Data1+Data2;
 if (Data3 == checkchar )
 {v8 =0;
  tmp =  Data1;
  tmp <<= 8;
  tmp &= 0xff00;//
  v8= Data2;
 
  v8 &= 0x00ff;
  v8 |= tmp;   
 v8-=1000;
tmp1 = v8/10000;                tmp2 = v8%10000; 
       Data1 = tmp1;
       tmp1 = tmp2/1000;                     tmp2 %= 1000;               
       Data2 = tmp1;
       tmp1 = tmp2/100;                     tmp2 %= 100;               
       Data3 = tmp1;
       tmp1 = tmp2/10;                     tmp2 %= 10;               
       Data4 = tmp1;
              
       Data5 = tmp2;
       
       Data1 += 0x30;  Data2 += 0x30;  Data3 += 0x30; Data4 += 0x30;  Data5 += 0x30;    
//ValueSensor[2] = 0x41; // "A"
netpiepublish[42] = Data1;
netpiepublish[43] = Data2;
netpiepublish[44] = Data3;
netpiepublish[45] = Data4;
netpiepublish[46] = Data5;
netpiepublish[47] = ';';

 }
else { return false;}
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

void checkBit(char ID)
{
  switch (ID){
    case 'A': BitcheckA = BitcheckA & B01111111; break;
    case 'B': BitcheckA = BitcheckA & B10111111; break;
    case 'C': BitcheckA = BitcheckA & B11011111; break;
    case 'D': BitcheckA = BitcheckA & B11101111; break;
    case 'E': BitcheckA = BitcheckA & B11110111; break;
    case 'F': BitcheckA = BitcheckA & B11111011; break;
    case 'G': BitcheckA = BitcheckA & B11111101; break;
    case 'H': BitcheckA = BitcheckA & B11111110; break;
    case 'I': BitcheckB = BitcheckB & B01111111; break;
    case 'J': BitcheckB = BitcheckB & B10111111; break;
    case 'K': BitcheckB = BitcheckB & B11011111; break;
    case 'L': BitcheckB = BitcheckB & B11101111; break;
    case 'M': BitcheckB = BitcheckB & B11110111; break;
    case 'N': BitcheckB = BitcheckB & B11111011; break;
    case 'O': BitcheckB = BitcheckB & B11111101; break;
    case 'P': BitcheckB = BitcheckB & B11111110; break;
    }
  
  
  }

void ControlBit(char ID)
{
  switch (ID){
    case 'A': BitcheckA = BitcheckA & B01111111; break;
    case 'B': BitcheckA = BitcheckA & B10111111; break;
    case 'C': BitcheckA = BitcheckA & B11011111; break;
    case 'D': BitcheckA = BitcheckA & B11101111; break;
    case 'E': BitcheckA = BitcheckA & B11110111; break;
    case 'F': BitcheckA = BitcheckA & B11111011; break;
    case 'G': BitcheckA = BitcheckA & B11111101; break;
    case 'H': BitcheckA = BitcheckA & B11111110; break;
    case 'I': BitcheckB = BitcheckB & B01111111; break;
    case 'J': BitcheckB = BitcheckB & B10111111; break;
    case 'K': BitcheckB = BitcheckB & B11011111; break;
    case 'L': BitcheckB = BitcheckB & B11101111; break;
    case 'M': BitcheckB = BitcheckB & B11110111; break;
    case 'N': BitcheckB = BitcheckB & B11111011; break;
    case 'O': BitcheckB = BitcheckB & B11111101; break;
    case 'P': BitcheckB = BitcheckB & B11111110; break;
    }
  
  
  }


boolean flagdust = false;
boolean flagairsensor=false;

int inputlight=0;
boolean flaglight = false;

////////////////////////////////////


void setup() { 


  Wire.begin();
  Serial.begin(9600);
Serial.println("SCD30 Example");
 
  while (!Serial);

  Serial.println("LoRa Sender");

  if (!LoRa.begin(freq)) {
    int i=0;
    Serial.println("Starting LoRa failed!");
    while (i<100); {i++;delay(10);}
    
  }

  LoRa.setTxPower(20);

/////////////////////////////////
airSensor.begin(); //This will cause readings to occur every two seconds
 
  delay(1000);
 pinMode(3, INPUT);
 inputlight = digitalRead(3);
 if (inputlight == LOW)
 { flaglight = true;
  }
 //while (sps30_probe() != 0) {

  
  pinMode(relayPin, OUTPUT); // output
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);digitalWrite(6,HIGH);
  pinMode(9, OUTPUT);digitalWrite(9, HIGH);

  loopcount=0;
  
  reftime = millis();     
  
 
  Supvoltage = analogRead(7);
 Supvoltage = Supvoltage*voltref;
Supvoltage = Supvoltage/102.3-voltoffset;
//Supvoltage = Supvoltage*11;

 reftime =millis();
////////////////

bitSet(addr[1],0);
bitSet(addr[1],1);
bitSet(addr[1],2);
bitSet(addr[1],3);
bitSet(addr[1],4);
bitSet(addr[1],5);
bitSet(addr[1],6);
bitSet(addr[1],7);

  ////////////////////////////////////////////////////////
nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("p0.pic=6");
  
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("img END");
nextion.end(); 

delay(3000);  
nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("p0.pic=10");
  //nextion.print("1"); //You don't need this
  //nextion.print("\""); //Or this
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("img END");
  delay(2000);
nextion.print("p0.pic=9");
  //nextion.print("1"); //You don't need this
  //nextion.print("\""); //Or this
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("img END");
 delay(2000);
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
////////////////////////

   nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print(String(rfID)+String(freq/1E6));
  //nextion.print("-update");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
 
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

  lastvalue=Luxvoltage;
  Luxvoltage = analogRead(2); 
  Luxvoltage = Luxvoltage*voltref;
  Luxvoltage = Luxvoltage/102.3-voltoffset;
 
 
   Luxvoltage = (Luxvoltage+lastvalue)/2;
     Lux = (Luxvoltage*14/50);
  Serial.print("Lux  ="); 
 
 
 Serial.print(Luxvoltage);
 Serial.println(" lLux");


//////////////////////////////////////////

 nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
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



///////////////////////////////////////////


v1=inttemp;        
v2=inthumid;            
v3=Lux;       
v4=intCO2;        
v5=intpm25;    
v6=0;       
v7=0;       
v8=Supvoltage;        




 
ProcessSendLORA('V');
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

//////////////read input///////////////////



float timecount = (millis()-reftime)/1000; 
Serial.print("timecount = "); Serial.println(timecount);
if ((timecount > (loracount*10))&&(loracount > 5)) {
  BitcheckA=0xFF; BitcheckB=0xFF;
  }
 /////////////////////////////////////////////////////////////
   
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


//////////////////////////////////////////////////
  
  delay(1000);




v1=inttemp;        
v2=inthumid;            
v3=Lux;       
v4=intCO2;        
v5=intpm25;    
v6=0;       
v7=0;       
v8=Supvoltage;       




Serial.print("Header:");Serial.println("M");
Serial.print("v1:");Serial.println(v1);
Serial.print("v2:");Serial.println(v2);
Serial.print("v3:");Serial.println(v3);
Serial.print("v4:");Serial.println(v4);
Serial.print("v5:");Serial.println(v5);
Serial.print("v6:");Serial.println(v6);
Serial.print("v7:");Serial.println(v7);
Serial.print("v8:");Serial.println(v8);

 

ProcessSendLORA('M');
 delay(1500);

//int packetSize = LoRa.parsePacket();
  

Serial.println(BitcheckA,BIN);
Serial.println(BitcheckA&0b00001111,BIN);
Serial.println(BitcheckA>>4,BIN);
addr[0]='I';

addr[1]=(BitcheckA>>4)+'0';
addr[2]=(BitcheckA&0b00001111)+'0';
addr[3]=addr[1]+addr[2];
addr[4]=(BitcheckB>>4)+'0';
addr[5]=(BitcheckB&0b00001111)+'0';
addr[6]=addr[4]+addr[5];

if ((addr[2]=='0') && (addr[3]=='0'))
 {BitcheckA=0xff;
 }
if ((addr[4]=='0') && (addr[5]=='0'))
 {BitcheckB=0xff;
 }

if (loracount%2 ==0)
{
 for(int i=0; i<5;i++)
 {

 

///////////////////////  
 //  for(int j=0; j<3;j++) {Serial.print(addr[j],BIN);Serial.print(',');Serial.println();}
 Serial.println(addr);
 LoRa.beginPacket();
  LoRa.print(addr);
 // LoRa.print(counter);
  LoRa.endPacket();
 int randomdelay = random(500, 2000);
 Serial.println(randomdelay);
nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print("Request");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");

  
  delay(randomdelay/2);
  nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print(String(addr));
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");
  delay(randomdelay/2);
  /////////////////////

  //////////////////////
 
 
 } 
}
  
 
 
  
  
  Serial.print("waiting for Input packet loopcount ");
    Serial.println(loopcount);

nextion.begin(9600);
  nextion.print("t5.txt=\"");
  nextion.print("Waiting...");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
nextion.end();
  
  while ((packetSize == 0)&&(loopcount < 1000)) 
  {

  
 
 // Serial.print("waiting for Inputpacket loopcount ");
 //   Serial.println(loopcount);
  loopcount++;
   if(loopcount%100 == 0) 
   {Serial.print(".");
    
   }
     packetSize = LoRa.parsePacket();
    // received a packet
  if ((packetSize > 0)&&(packetSize <40))
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

      
    checkBit(InputRS232[1]);
    Serial.print(F("Input ID"));
    Serial.println(BitcheckA,BIN);

  
    Serial.print(F("netpie: "));
    Serial.println(netpiepublish);
    for (int j=0;j<5;j++) 
     
    {
      
      
      
      for (int k=0;k<30;k++) 
    
      Serial.print(InputRS232[k]);
    
    Serial.println();
    delay(500);
    }
   
 
    
    
    loracount=1;  
    reftime=millis();
    }

  
  }//if (packetSize > 0)
  delay(10);
  } //while ((packetSize == 0)&&(loopcount < 1000)) 
  
  LoRa.sleep();
  
  //while
  loracount++; Serial.print("loracount:");Serial.println(loracount);
  inputcount++;

Serial.print("inputcount=");Serial.println(inputcount);
 if ((inputcount > 20)|| (inputcount < 0))
 
    { 
   
      digitalWrite(5, LOW); // output pin 13
    delay(5000);
    digitalWrite(5, HIGH); // output pin 1
    }

     if (stringComplete&&(FlagStart == false)) {

   
 //inputcount =0;   
     //inputString.toCharArray(InputRPI, 15);
    Serial.print("serial input = ");    Serial.println(InputRPI); 
     if( ((InputRPI[0] == 'P')&&(InputRPI[1] == 't'))&&(InputRPI[4] == '-')&&(InputRPI[7] == '-') )
     {
    inputcount =0;
     }
    if ((InputRPI[1] == 'T')|| ((InputRPI[1] == 'S')))
    {
      inputcount =0;
      loopcount =1; 
       Serial.flush();
       if (((InputRPI[0] == 'P')&&(InputRPI[1] == 'S')))
    { 
    for (j=0;j<10;j++)
      {
        Serial.println(InputRPI); 
        delay (500);
      }
                     loopcount =1; 
                     ValueMT1=0;ValueMT2=0;ValueMT3=0;ValueMT4=0;
                     Ptcount=0;
                      reftime =millis();
                    FlagShutdown =true;
                     Serial.flush(); 
                    BitcheckA=0xFF;
                    BitcheckB=0xFF;
                    
                  }


       
   //  for (j=0;j<30;j++){  InputRPI[j]= '0';  }  
    }
  
  stringComplete = false;
  for (j=0;j<30;j++){  InputRPI[j]= '0';  }
   }
  else
  {
   Serial.print("false serial count = ");
    Serial.println(InputRPI); 
  
   
  }

  
  if (loracount%6 ==0)
  {
   digitalWrite(LORA_RESET, LOW); // output pin 13
   delay(5000);
   digitalWrite(LORA_RESET, HIGH); // output pin 13
    if (!LoRa.begin(freq)) {
    int i=0;
    Serial.println("Starting LoRa failed!");
    while (i<100); {i++;delay(10);}
    
  }

  LoRa.setTxPower(20);
 Serial.println("RESET LoRa ");

nextion.begin(9600); // set the data rate for the SoftwareSerial port
 
  // We change the image of image box p0
  nextion.print("t5.txt=\"");
  nextion.print("Reset");
  nextion.print("\"");
  nextion.write(0xff);  // We always have to send this three lines after each command sent to the nextion display.
  nextion.write(0xff);
  nextion.write(0xff);
  Serial.print("txt END");  

  
  }
  if (loracount > 100)
  { digitalWrite(5, LOW); // output pin 13
    delay(5000);
    digitalWrite(5, HIGH);
     
  }
loopcount=0;
packetSize=0;
delay(random(3000, 5000));

}



  


 
