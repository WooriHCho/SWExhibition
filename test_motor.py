#!/usr/bin/env python
import time
from SunFounder_TB6612 import TB6612
import RPi.GPIO as GPIO

def main():
	import time

	print "********************************************"
	print "*                                          *"
	print "*           SunFounder TB6612              *"
	print "*                                          *"
	print "*          Connect MA to BCM17             *"
	print "*          Connect MB to BCM18             *"
	print "*         Connect PWMA to BCM27            *"
	print "*         Connect PWMB to BCM22            *"
	print "*                                          *"
	print "********************************************"
	GPIO.setmode(GPIO.BCM)
	GPIO.setup((5, 4), GPIO.OUT)
	a = GPIO.PWM(5, 60)
	b = GPIO.PWM(4, 60)
	a.start(0)
	b.start(0)

	def a_speed(value):
		a.ChangeDutyCycle(value)

	def b_speed(value):
		b.ChangeDutyCycle(value)

	motorA = TB6612.Motor(17)
	motorB = TB6612.Motor(27)
	motorA.debug = True
	motorB.debug = True
	motorA.pwm = a_speed
	motorB.pwm = b_speed

	delay = 0.05

	motorA.forward()
	for i in range(0, 101):
		motorA.speed = i
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorA.speed = i
		time.sleep(delay)

	motorA.backward()
	for i in range(0, 101):
		motorA.speed = i
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorA.speed = i
		time.sleep(delay)

	motorB.forward()
	for i in range(0, 101):
		motorB.speed = i
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorB.speed = i
		time.sleep(delay)

	motorB.backward()
	for i in range(0, 101):
		motorB.speed = i
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorB.speed = i
		time.sleep(delay)

def destroy():
	motorA.stop()
	motorB.stop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		destroy()
