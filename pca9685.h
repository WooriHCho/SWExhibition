#ifndef _PCA9685_H_
#define _PCA9685_H_

#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

#define MODE1 0x00
#define PRE_SCALE 0xFE
#define LED0_ON_L 0x06
#define LED0_OFF_L 0x08

#define AI 0x20
#define SLEEP 0x10
#define RESTART 0x08

typedef struct{
	int i2c_addr;
	int rMODE1;
	int rPRE_SCALE;
	int rLED0_ON_L;
	int rLED0_OFF_L;
	int i2c_port;
} pca9685_t;

static void setupAutoIncrement(pca9685_t& pca9685);
void init(pca9685_t& pca9685);
void setFrequency(pca9685_t& pca9685, int frequency);
void setDutyCycle(pca9685_t& pca9685, int duty_off);

#endif
