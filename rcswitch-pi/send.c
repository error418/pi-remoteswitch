#include "RCSwitch.h"
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    /*
     output PIN is hardcoded for testing purposes
     see https://projects.drogon.net/raspberry-pi/wiringpi/pins/
     for pin mapping of the raspberry pi GPIO connector
     */

    int PIN = 6; // this is a wiringPi pin number! (Just to add more confusion to using the wiringPi library)
    char* code = argv[1];

    if (wiringPiSetup () == -1) return 1;

    printf("sending code [%s] via pin %i", code, PIN);

    RCSwitch mySwitch = RCSwitch();
    mySwitch.enableTransmit(PIN);

    mySwitch.sendTriState(code);

    return 0;
}
