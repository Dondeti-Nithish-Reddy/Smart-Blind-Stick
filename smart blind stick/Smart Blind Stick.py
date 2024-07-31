#include<string.h>
#include <WiFiClientSecure.h>   // Include the HTTPS library
#include <ESP8266WiFi.h>        // Include the Wi-Fi library
#include <ESP8266WiFiMulti.h>   // Include the Wi-Fi-Multi library
#include "Arduino.h"
#include <EMailSender.h>
ESP8266WiFiMulti wifiMulti;     // Create an instance of the ESP8266WiFiMulti class, called 'wifiMulti'
uint8_t connection_state = 0;
uint16_t reconnect_interval = 10000;
WiFiClient  client;
String data1="";
String data2="cmd";
String data=" MESSAGE";
EMailSender emailSend("sivaprasadpilla7@gmail.com", "tvgcjlhvnpdetvvq");
void gmail()
{
  EMailSender::EMailMessage message;
    
    message.subject = "This is an email from hardware system :  "+data1;
    message.message = "This is an email from hardware system : "+data1;

    EMailSender::Response resp = emailSend.send("nithishreddy908@gmail.com", message);

    Serial.println("Sending status: ");

    Serial.println(resp.status);
    Serial.println(resp.code);
    Serial.println(resp.desc);  
}
void upload()
{
const char* server4 = "api.thingspeak.com";
const char* _getLink4 = "https://api.thingspeak.com/update?api_key=PWX6Z0ZH2CQXFG3X&field1="; // Thingspeak.com
//const char* _getLink4 = "https://api.thingspeak.com/update?api_key=4GAW4V46WO2L007U&field1="; // Thingspeak.com

 // Serial.println("data uploading");delay(1000);  
  client.connect(server4,80);
 if (client.connect(server4,80))     // "184.106.153.149" or api.thingspeak.com  https://api.thingspeak.com/apps/thinghttp/send_request?api_key=CT9B331KB5PLM1G5
  { 
    String getStr4 = _getLink4;
    client.print("GET "+getStr4+data1+"\n");
    client.print("HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n\n\n");
  }
  client.stop();

}

void readdata()
{
  data1="";delay(1000);
const char* server4 = "api.thingspeak.com";
const char* _getLink4 = " https://api.thingspeak.com/channels/562742/fields/1/last.txt"; // Thingspeak.com


  //Serial.println("data uploading");delay(1000);  
  client.connect(server4,80);
 if (client.connect(server4,80))     // "184.106.153.149" or api.thingspeak.com  https://api.thingspeak.com/apps/thinghttp/send_request?api_key=CT9B331KB5PLM1G5
  { 
    String getStr4 = _getLink4;
    client.print("GET "+getStr4+"\n");
    client.print("HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n\n\n");
    client.available();
    data1=client.readString();delay(1000);
    //Serial.println(data1);delay(1000);

if(data1[0]=='*')
{
  if(data2==data1)
  {
    
  }
  else
  {
  Serial.println(data1);upload();
  }
  data2=data1;
}
/*

 if((data1=="light1on")||(data1=="light1off")||(data1=="light2on")||(data1=="light2off")||(data1=="fan1on")||(data1=="fan1off")||(data1=="fan2on")||(data1=="fan2off"))
{
  Serial.print(data1);delay(1000);upload();
}
  
    if(data1[0]=='*')
    {
   Serial.println(data1);delay(10000);upload();
    }
    if((data1=="1")||(data1=="2")||(data1=="3")||(data1=="4")||(data1=="0"))
    {
   Serial.print(data1);delay(10000);
      }
      */
  }
  client.stop();
}



void setup()
{
  Serial.begin(9600);         // Start the Serial communication to send messages to the computer
  delay(10);
  //Serial.println('\n');

  wifiMulti.addAP("consciencetechnologies", "484conscience777");   // add Wi-Fi networks you want to connect to
  wifiMulti.addAP("sivaji", "sivaji.123");
  wifiMulti.addAP("ZTE-sUQdqa", "5hjgxyh9");
  wifiMulti.addAP("project", "project.123");
  wifiMulti.addAP("123456789", "123456789");

  //Serial.println("Connecting ...");
  int i = 0;
  while (wifiMulti.run() != WL_CONNECTED) { // Wait for the Wi-Fi to connect: scan for Wi-Fi networks, and connect to the strongest of the networks above
    delay(250);
    //Serial.print('.');
  }
  //Serial.println('\n');
  //Serial.print("Connected to ");
  //Serial.println(WiFi.SSID());              // Tell us what network we're connected to
  //Serial.print("IP address:\t");
 Serial.println(WiFi.localIP());           // Send the IP address of the ESP8266 to the computer
  //Serial.println('\n');

  //readdata();
//gmail();
}


void loop() 
{

while(1)
{
 while(Serial.available())
 {
 
  data1=Serial.readString();delay(1000);
   upload();
 /* if((data1[0]=='P')||(data1[0]=='p')||(data1[0]=='1')||(data1[1]=='p')||(data1[2]=='P')||(data1[2]=='p')||(data1[3]=='P')||(data1[3]=='p'))
  {
  upload();
  }*/
  //data1.replace("&field2=", " , Voltege= ");delay(1000);
  //data1.replace("&field3=", " , Temperature= ");delay(1000);
  //data1="Current="+data1;delay(1000);
gmail();
  
 }

}

}


/*code 2

#include <LiquidCrystal.h>
const int rs = A0, en = A1, d4 = A2, d5 = A3, d6 = A4, d7 = A5;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

#include <Servo.h>
Servo servo;
int ii=0;
int buzzer=9;
#define echoPin1 7 // Echo Pin
#define trigPin1 6 // Trigger Pin
int maximumRange1 = 200; // Maximum range needed
int minimumRange1 = 0; // Minimum range needed
long duration1, distance1; // Duration used to calculate distance

#define echoPin2 5 // Echo Pin
#define trigPin2 4 // Trigger Pin
int maximumRange2 = 200; // Maximum range needed
int minimumRange2 = 0; // Minimum range needed
long duration2, distance2; // Duration used to calculate distance
int sw=12;
#include<SoftwareSerial.h>
SoftwareSerial gps(10,11);
int i=0,k=0;
int  gps_status=0;
float latitude=17.562172; //17.562172, 78.446031
float logitude=78.446031;  
//float latitude=0; 
//float logitude=0;                     
String Speed="";
String gpsString="";
char *test="$GPRMC";
String location=" http://maps.google.com/maps?&z=15&mrt=yp&t=k&q="+String(latitude,6)+"+"+String(logitude,6);
void gpsinit()
{
  gps.begin(9600);
  lcd.clear();lcd.print("GPS is Ready");delay(1000);
  lcd.clear(); lcd.print("System Ready");
}
void gpsEvent()
{
  gpsString="";
  while(1)
  {
   while (gps.available()>0)            //Serial incoming data from GPS
   {
    char inChar = (char)gps.read();
     gpsString+= inChar;                    //store incoming data from GPS to temparary string str[]
     i++;
    // Serial.print(inChar);
     if (i < 7)                      
     {
      if(gpsString[i-1] != test[i-1])         //check for right string
      {
        i=0;
        gpsString="";
      }
     }
    if(inChar=='\r')
    {
     if(i>60)
     {
       gps_status=1;
       break;
     }
     else
     {
       i=0;
     }
    }
  }
   if(gps_status)
    break;
  }
}
void get_gps()
{
  lcd.clear();
  lcd.print("Getting GPS Data");
  lcd.setCursor(0,1);
  lcd.print("Please Wait.....");
   gps_status=0;
   int x=0;
   while(gps_status==0)
   {
    gpsEvent();
    int str_lenth=i;
    //coordinate2dec();
    i=0;x=0;
    str_lenth=0;
   }
}
void gpsdata()
{
    lcd.clear();
    lcd.print("Lat:");
    lcd.print(latitude);
    lcd.setCursor(0,1);
    lcd.print("Log:");
    lcd.print(logitude);
    delay(2000);
    lcd.clear();
    
}
void coordinate2dec()
{
  String lat_degree="";
    for(i=19;i<=20;i++)         
      lat_degree+=gpsString[i];
      Serial.println(lat_degree);
  String lat_minut="";
     for(i=21;i<=30;i++)         
      lat_minut+=gpsString[i];
      Serial.println(lat_minut);
  String log_degree="";
    for(i=32;i<=34;i++)
      log_degree+=gpsString[i];
      Serial.println(log_degree);
  String log_minut="";
    for(i=35;i<=44;i++)
      log_minut+=gpsString[i];
      Serial.println(log_minut);
    
    Speed="";
    for(i=45;i<48;i++)          //extract longitude from string
      Speed+=gpsString[i];
      
     float minut= lat_minut.toFloat();
     minut=minut/60;
     float degree=lat_degree.toFloat();
     latitude=degree+minut;
     Serial.println(latitude);
     
     minut= log_minut.toFloat();
     minut=minut/60;
     degree=log_degree.toFloat();
     logitude=degree+minut;
     Serial.println(logitude);
}

void setup()
{
  pinMode(sw,INPUT_PULLUP);
  lcd.begin(16, 2);
  pinMode(buzzer,OUTPUT);digitalWrite(buzzer,HIGH);
  digitalWrite(buzzer,LOW);delay(1000);digitalWrite(buzzer,HIGH);
servo.attach(8);delay(100);
 pinMode(trigPin1, OUTPUT); pinMode(echoPin1, INPUT);
 pinMode(trigPin2, OUTPUT);pinMode(echoPin2, INPUT); 
 Serial.begin(9600);delay(1000);
 }

void loop()
{
while(1)
{
int swval=digitalRead(sw);
if(swval==LOW)
{
Serial.println("PANIC ALERT" + location);delay(1000);
digitalWrite(buzzer,LOW);delay(100);digitalWrite(buzzer,HIGH);
digitalWrite(buzzer,LOW);delay(100);digitalWrite(buzzer,HIGH);  
}
for(ii=0;ii<178;ii=ii+10)
{
digitalWrite(trigPin2, LOW);delay(2); 
digitalWrite(trigPin2, HIGH);delay(10); 
 digitalWrite(trigPin2, LOW);
 duration2 = pulseIn(echoPin2, HIGH);
 distance2 = duration2/58.2;delay(1000);



digitalWrite(trigPin1, LOW);delay(2); 
digitalWrite(trigPin1, HIGH);delay(10); 
 digitalWrite(trigPin1, LOW);
 duration1 = pulseIn(echoPin1, HIGH);
 distance1 = duration1/58.2;delay(500);

 if(distance1<30)
 {
 // Serial.println("OBJECT ALERT" + location);delay(1000);
  digitalWrite(buzzer,LOW);delay(100);digitalWrite(buzzer,HIGH);
 }
 if(distance2>30)
 {
  //Serial.println("PATH HOLE ALERT" + location);delay(1000);
  digitalWrite(buzzer,LOW);delay(1000);digitalWrite(buzzer,HIGH);
 }
servo.write(ii);delay(100);
int swval=digitalRead(sw);
if(swval==LOW)
{
Serial.println("PANIC ALERT" + location);delay(1000);
digitalWrite(buzzer,LOW);delay(100);digitalWrite(buzzer,HIGH);
digitalWrite(buzzer,LOW);delay(100);digitalWrite(buzzer,HIGH);  
}

}


for(ii=178;ii>0;ii=ii-10)
{
digitalWrite(trigPin2, LOW);delay(2); 
digitalWrite(trigPin2, HIGH);delay(10); 
 digitalWrite(trigPin2, LOW);
 duration2 = pulseIn(echoPin2, HIGH);
 distance2 = duration2/58.2;delay(500);


digitalWrite(trigPin1, LOW);delay(2); 
digitalWrite(trigPin1, HIGH);delay(10); 
 digitalWrite(trigPin1, LOW);
 duration1 = pulseIn(echoPin1, HIGH);
 distance1 = duration1/58.2;delay(1000);
 if(distance1<30)
 {
  //Serial.println("OBJECT ALERT" + location);delay(1000);
  digitalWrite(buzzer,LOW);delay(100);digitalWrite(buzzer,HIGH);
 }
 if(distance2>30)
 {
  //Serial.println("PATH HOLE ALERT" + location);delay(1000);
  digitalWrite(buzzer,LOW);delay(1000);digitalWrite(buzzer,HIGH);
 }
servo.write(ii);delay(100);

int swval=digitalRead(sw);
if(swval==LOW)
{
Serial.println("PANIC ALERT" + location);delay(1000);
digitalWrite(buzzer,LOW);delay(100);digitalWrite(buzzer,HIGH);
digitalWrite(buzzer,LOW);delay(100);digitalWrite(buzzer,HIGH);  
}
}

}

}