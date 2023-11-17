// Wire Master Reader
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Reads data from an I2C/TWI slave device
// Refer to the "Wire Slave Sender" example for use with this

// Created 29 March 2005

// This example code is in the public domain.

#include <Wire.h>
#include <Adafruit_SCD30.h>
#include <Adafruit_MLX90614.h>

Adafruit_SCD30  scd30;
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
long int t1, t2;
unsigned long previousMillis = 0; 
const long interval = 2000; 
const long setupinterval = 5000; 
void setup()
{
  //unsigned long currentMillis = millis();
  Serial.begin(9600);  // start serial for output
  while (!Serial) delay(10);
  Wire.begin();        // join i2c bus (address optional for master)
  mlx.begin();
  scd30.begin();
  delay(6000);  
  //if (millis() >= setupinterval)
  {
    //continue;
  }
}

void loop()
{
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval)
  {
    previousMillis = currentMillis;
    if (scd30.dataReady()){                                 // SCD30 Measurements
      if (!scd30.read()){ return; }
      Serial.print(mlx.readAmbientTempC()); Serial.print(",");       // MLX Measurements 
      Serial.print(mlx.readObjectTempC()); Serial.print(",");   
      Serial.print(scd30.temperature); Serial.print(",");
      Serial.print(scd30.relative_humidity); Serial.print(",");
      Serial.print(scd30.CO2, 3); Serial.print(",");
      Serial.println(currentMillis);
    } else {
        Serial.println("NaN");
    } 
  }

}
