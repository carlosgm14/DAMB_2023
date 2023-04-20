// int ledPin = 11;

// void setup() {
//   pinMode(ledPin, OUTPUT);
//   Serial.begin(9600);
// }

// void loop() {
//   if (Serial.available() > 0) {
//     int intensity = Serial.read();
//     analogWrite(ledPin, intensity);
//   }
// }

const int sensor_pin = A0;
const int led_pin = 11;
int intensity;

void setup() {
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);
}

void loop() {
  // Lectura del valor del sensor analógico
  float voltage = analogRead(sensor_pin) * (5.0 / 1023.0);

  // Envío del valor del sensor por el puerto serie
  Serial.print("Sensor voltage: ");
  Serial.print(voltage);
  Serial.println(" V");

  // Lectura de la intensidad enviada
  if (Serial.available() > 0) {
    intensity = Serial.read();
    analogWrite(led_pin, intensity);
  }
}