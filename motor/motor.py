from __future__ import division
import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()

center = 307
right = 410
left = 210

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)
pwm.set_pwm(0, 0, center)
pwm.set_pwm(4, 0, 1400)
pwm.set_pwm(5, 0, 1400)

i=0
while True:
        f1=open('/home/pi/SWExhibition/output.txt', 'r')
        s = f1.readlines()
        x = int(s[i])
	if x < 100 or x > 600:
		continue
        if x >= center - 150 and x <= center + 150:
                pwm.set_pwm(0, 0, center)
                time.sleep(1)
        elif center-150 > x:
                k=int((center - x)/6)
                pwm.set_pwm(0, 0, center + k)
                time.sleep(1)
        elif center+150 < x:
                k= int((x - center)/6)
                pwm.set_pwm(0, 0, center - k)
                time.sleep(1)
        print(x)
        i+=1
pwm.set_pwm(4, 0, 0)
pwm.set_pwm(5, 0, 0)
