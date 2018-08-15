#include "pca9685.h"
extern pca9685_t pca9685;
int main(void)
{
	const int servo_chan=0;
	const int servo_frequency = 50;

	wiringPiSetup();

	init(pca9685);
	
	setFrequency(pca9685, servo_frequency);

	int cnt;
	for(cnt-0; cnt<=2; cnt++){
		setDutyCycle(pca9685, servo_chan, (4096/20)*0.6);
		delay(1000);
		setDutyCycle(pca9685, servo_chan, (4096/20)*2.5);
		delay(1000);
	}
	setDutyCycle(pca9685, servo_chan, 0);
}
