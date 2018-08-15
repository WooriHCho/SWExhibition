#include "pca9685.h"

pca9685_t pca9685 = {
	.i2c_addr = 0x40,
	.rMODE1 = MODE1,
	.rPRE_SCALE = PRE_SCALE,
	.rLED0_ON_L = LED0_ON_L,
	.rLED0_OFF_L = LED0_OFF_L,
};

static void setupAutoIncrement(pca9685_t& pca9685){
	int i2c_port = pca9685.i2c_port;
	int mode1;

	mode1 = wiringPiI2CReadReg8(i2c_port, pca9685.rMODE1)&0xFF;
	wiringPiI2CWriteReg8(i2c_port, pca9685.rMODE1, mode1|AI);
}

void init(pca9685_t& pca9685){
	int i2c_port;

	if((i2c_port = wiringPiI2CSetup(pca9685.i2c_addr)) < 0){
		fprintf(stderr, "Unable to open pca9685 device: %s\n", strerror(errno));
		exit(0);
	}
	
	pca9685.i2c_port = i2c_port;
	
	setupAutoIncrement(pca9685);
}

void setFrequency(pca9685_t& pca9685, int frequency){
	int i2c_port = pca9685.i2c_port;
	int mode1;
	int prescale;

	mode1 = wiringPiI2CReadReg8(i2c_port, pca9685.rMODE1)&0xFF;
	wiringPiI2CWriteReg8(i2c_port, pca9685.rMODE1, mode1|SLEEP);

	prescale = (int)(2500000.0f/(4096*frequency)+0.5f)-1;
	wiringPiI2CWriteReg8(i2c_port, pca9685.rPRE_SCALE, prescale);

	mode1 = wiringPiI2CReadReg8(i2c_port, pca9685.rMODE1)&0xFF;
	wiringPiI2CWriteReg8(i2c_port, pca9685.rMODE1, mode1&~SLEEP);

	delay(1);
	
	mode1 = wiringPiI2cReadReg8(i2c_port, pca9685.rMODE1)&0xFF;
	wiringPiI2CWriteReg8(i2c_port, pca9685.rMODE1, mode1|RESTART);
}

void setDutyCycle(pca9685_t& pca9685, int pin, int duty_off)
	int i2c_port = pca9685.i2c_port;
	int chan = pin*4;

	wiringPiI2cWriteReg16(i2c_port, pca9685.rLED0_OFF_L + chan, duty_off&0x1FFF);
}
