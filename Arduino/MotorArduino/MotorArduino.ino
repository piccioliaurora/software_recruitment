const int joyPin = A2;
int joyVal;
int motorPos;
const int minMotorPos = 511;
const int maxMotorPos = 818;
uint8_t buffer[3];

void setup() {
    Serial.begin(19200);
}

void loop() {
    joyVal = analogRead(joyPin);
    motorPos = map(joyVal, 0, 1023, minMotorPos, maxMotorPos);
    motorPos = constrain(motorPos, minMotorPos, maxMotorPos);

    printf("Joystick Value: %d, Mapped Motor Position: %d\n", joyVal, motorPos);

    buffer[0] = 0x1E; 
    buffer[1] = lowByte(motorPos);
    buffer[2] = highByte(motorPos);

    Serial.write(buffer, sizeof(buffer));
    delay(100);
}