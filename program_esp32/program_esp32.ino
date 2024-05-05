// Include the DHT11 library for interfacing with the sensor.
#include <DHT11.h>

// Create an instance of the DHT11 class and connect it to pin 23
DHT11 dht11(23);

void setup() {
    
    Serial.begin(9600);
  
    pinMode(4, INPUT); // POT 1
    pinMode(2, INPUT); // POT 2
    pinMode(34, INPUT); // POT 3
    pinMode(35, INPUT); // POT 4
    pinMode(32, INPUT); // POT 5
    pinMode(33, INPUT); // PHOTO RESISTOR
    pinMode(26, INPUT); // BUTTON
    pinMode(16, OUTPUT); // BUTTON
    pinMode(17, OUTPUT); // BUTTON
}

int temperature = 0;
int humidity = 0;
void loop() {
    
    // Attempt to read the temperature and humidity values from the DHT11 sensor.
    int result = dht11.readTemperatureHumidity(temperature, humidity);
    
    if (result == 0) { // llegit correctament
        Serial.print("Sensor_temperatura: ");
        Serial.println(temperature);
        Serial.print("Sensor_humitat: ");
        Serial.println(humidity);
    } else{ // error
        Serial.print("Sensor_temperatura: ");
        Serial.println(-1);
        Serial.print("Sensor_humitat: ");
        Serial.println(-1);
    }

    Serial.print("Potenciometre1: ");
    Serial.println((float(analogRead(4))/4096.0));
    Serial.print("Potenciometre2: ");
    Serial.println((float(analogRead(2))/4096.0));
    Serial.print("Potenciometre3: ");
    Serial.println((float(analogRead(34))/4096.0));
    Serial.print("Potenciometre4: ");
    Serial.println((float(analogRead(35))/4096.0));
    Serial.print("Potenciometre5: ");
    Serial.println((float(analogRead(32))/4096.0));
    Serial.print("Sensor_de_llum: ");
    Serial.println((float(analogRead(33))/4096.0));
    
    if (digitalRead(26) == LOW){
      Serial.print("consumint_molt: ");
      Serial.println("0");
    }
    else{
      Serial.print("consumint_molt: ");
      Serial.println("1");
    }

    digitalWrite(17, LOW);
    digitalWrite(16, HIGH);

    Serial.println("end");
    
    delay(5000); // fer delay pot ser que no sigui bona idea perque el process anterior al delay s'afegeix al temps total. Fer la diferencia entre millis() donaria la precisio necessaria pero pot fer overflow i llavors no se que passa.

    digitalWrite(16, LOW);
    digitalWrite(17, HIGH);
}
