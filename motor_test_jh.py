from __future__ import division
import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

pwm_pin = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100)
angle = 3
pwm.start(angle)

while True:
	cmd = raw_input("Command, f/r :")
	direction = cmd[0];
	if direction == "f":
		angle+=1
	else:
		angle-=1
	if angle < 3:
		angle = 3
	elif angle > 20:
		angle = 20
	print "angle=", (angle-3)*10
	pwm.ChangeDutyCycle(angle)
