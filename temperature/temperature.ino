#include "DHT.h"

#define DHTPIN A1 // Pin connected to sensor
#define DHTTYPE DHT11 // Sensor model: DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  //float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.println(int(t));
  delay(1);
}
