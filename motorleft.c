#include <stdio.h>
#include <wiringPi.h>
#define left 3

int main(void){
	if(wiringPiSetup() == -1)
		return 1;
	pinMode(left, OUTPUT);
	while(1)
	{
		digitalWrite(left, 1);
		delay(1000);
		digitalWrite(left, 0);
		delay(1000);
	}
	return 0;
}
