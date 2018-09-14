from __future__ import division
import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()

center = 307
right = 410
left = 210

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)

print('Moving servo on channel 0, press Ctrl-C to quit...')

pwm.set_pwm(0, 0, center)
pwm.set_pwm(4, 0, 1400)
pwm.set_pwm(5, 0, 1400)

i=0
while i<=3:
	f=open('temp.txt', 'r')
	s = f.readline()
	x = int(s)
	if x >= center - 50 and x <= center + 50:
		pwm.set_pwm(0, 0, center)
		time.sleep(1)
	elif center >= x:
		k=int((center - x)/6)
		pwm.set_pwm(0, 0, center - k)
		time.sleep(1)
	elif center <= x:
		k= int((center - x)/6)
		pwm.set_pwm(0, 0, center + k)
		time.sleep(1)
	pwm.set_pwm(0, 0, center)
	i+=1
pwm.set_pwm(4, 0, 0)
pwm.set_pwm(5, 0, 0)
