#define PULL_PIN 13
#define PUSH_PIN 12
#define PING_PIN 6
#define MOTION_PIN 8
int calibrationTime = 30;
bool moving = false;
long current_time, movement_time;
enum States {SUSPENDED, UP, DOWN, DROPPED};
States current_state = SUSPENDED;
void setup(){
    Serial.begin(9600);
    pinMode(PULL_PIN, OUTPUT);
    pinMode(PUSH_PIN, OUTPUT);
    pinMode(MOTION_PIN, INPUT);
    Serial.print("calibrating sensor ");
    for(int i = 0; i < calibrationTime; i++){
        Serial.print(".");
        delay(1000);
    }
    Serial.println(" done");
    Serial.println("SENSOR ACTIVE");
    delay(50);
}
void loop(){
    current_time = millis();
    Serial.println(current_state);
    switch (current_state){
        case SUSPENDED:
            stop();
            if(is_motion())
                current_state = DOWN;
        break;
        case DOWN:
            Serial.println("GOING DOOOWN");
            if(check_ping() > 5){
                push();
            }else{
                current_state = DROPPED;
            }
        break;
        case DROPPED:
            stop();
            delay(5000);
            current_state = UP;
        break;
        case UP:
            pull();
            delay(5000);
            current_state = SUSPENDED;
        break;
    }
}
bool is_motion(){
    digitalRead(MOTION_PIN);
}
void pull(){
    digitalWrite(PUSH_PIN,LOW);
    digitalWrite(PULL_PIN, HIGH);
}
void push(){
    digitalWrite(PULL_PIN, LOW);
    digitalWrite(PUSH_PIN, HIGH);
}
void stop(){
    digitalWrite(PUSH_PIN, HIGH);
    digitalWrite(PULL_PIN, HIGH);
}
int check_ping(){
    unsigned int duration, inches;
    pinMode(PING_PIN, OUTPUT);          // Set pin to OUTPUT
    digitalWrite(PING_PIN, LOW);        // Ensure pin is low
    delayMicroseconds(2);
    digitalWrite(PING_PIN, HIGH);       // Start ranging
    delayMicroseconds(5);              //   with 5 microsecond burst
    digitalWrite(PING_PIN, LOW);        // End ranging
    pinMode(PING_PIN, INPUT);           // Set pin to INPUT
    duration = pulseIn(PING_PIN, HIGH); // Read echo pulse
    inches = duration / 74 / 2;        // Convert to inches

    return inches;
}


int checkSonar(){
    static long pulse = 0;
    static int arraysize = 9;
    static int modE;
    static int rangevalue[] = {0,0,0,0,0,0,0,0,0};
    for(int i = 0; i < arraysize; i++)
    {
        pulse = pulseIn(PING_PIN, HIGH);
        rangevalue[i] = pulse/147;
        delay(10);
    }
    modE = mode(rangevalue,arraysize);
    return modE;
}
int mode(int *x,int n){
    int i = 0;
    int count = 0;
    int maxCount = 0;
    int mode = 0;
    int bimodal;
    int prevCount = 0;
    while(i<(n-1)){
        prevCount=count;
        count=0;
        while(x[i]==x[i+1]){
            count++;
            i++;
        }
        if(count>prevCount&count>maxCount){
            mode=x[i];
            maxCount=count;
            bimodal=0;
        }
        if(count==0){
            i++;
        }
        if(count==maxCount){//If the dataset has 2 or more modes.
            bimodal=1;
        }
        if(mode==0||bimodal==1){//Return the median if there is no mode.
            mode=x[(n/2)];
        }
        return mode;
    }
}
