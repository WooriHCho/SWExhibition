import Adafruit_PCA9685
import RPi.GPIO as GPIO

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

back_left =12 
back_right = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(back_left, GPIO.OUT)
GPIO.setup(back_right, GPIO.OUT)

while True:
	GPIO.output(back_left, GPIO.LOW)
	GPIO.output(back_right, GPIO.LOW)

pwm.set_pwm(0,0,0)
GPIO.cleanup()
