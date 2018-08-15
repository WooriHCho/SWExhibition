#include <stdio.h>
#include <wiringPi.h>
#define left 3

int main(void){
	wiringPiSetup();
	
	pinMode(left, PWM_OUTPUT);
	while(1)
	{
		int speed;
		printf("motor start\n");
		for(speed=0; speed<=1024; speed+=200)
		{
			pwmWrite(left, speed);
			delay(500);
		}
		for(speed = 1024; speed >= 0; speed-=200)
		{
			pwmWrite(left, speed);
			delay(500);
		}
		printf("motor end\n");
	}
}


