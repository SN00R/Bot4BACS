// Use this Arduino script in the Arduino IDE to flash the Arduino Nano on the head of the robot.
// Make sure the two brightness sensors are connected to the Nano.
// Also make sure that both brightness sensors have different addresses (on one the ADDR Pin is grounded, on the other with VCC)  

#include <Wire.h>
#include <BH1750.h>

BH1750 lightMeter1(0x23);
BH1750 lightMeter2(0x5C);
long int t1, t2;

unsigned long previousMillis = 0; 
const long interval = 2000; 

void setup()
{
  Serial.begin(9600);  // start serial for output
  while (!Serial) delay(10); 
  Wire.begin();        // join i2c bus (address optional for master)

  lightMeter1.begin(BH1750::CONTINUOUS_LOW_RES_MODE, 0x23, &Wire);
  lightMeter2.begin(BH1750::CONTINUOUS_LOW_RES_MODE, 0x5C, &Wire);
  //Serial.println(F("BH1750 Test 2 Sensors"));
  delay(5000);
  //t1 = millis();
}

void loop()
{
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) 
  {
    //Serial.print("time in s: "); Serial.println(currentMillis);
    previousMillis = currentMillis;
    float lux1 = lightMeter1.readLightLevel();              // BH1750 0x23 Measurements
    float lux2 = lightMeter2.readLightLevel();              // BH1750 0x5A Measurements
    Serial.print(lux1); Serial.print(",");
    Serial.println(lux2);
  }

}

