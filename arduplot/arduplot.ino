int antennaPin = A0;
int speaker = 3;

int bg;

int media(int pin) { // Takes the median background interference
  int all;
  for(int i=0; i<100; i++) {
    all += int(analogRead(pin));
    delay(10);
  }
  return int(all/100); 
}

void setup() {
  Serial.begin(9600);
  pinMode(antennaPin, INPUT); // Antenna on A5
  // pinMode(speaker, OUTPUT); // Output signal to speaker on PIN3
  delay(3000); // Analog cooldown delay
  bg = media(antennaPin);
}

void loop() {
  int Read = int(analogRead(antennaPin)-bg);
  Serial.println(int((analogRead(antennaPin)-bg)/5));
  //tone(speaker, int( analogRead(antennaPin)-bg));
  delay(1);
}
