from __future__ import division
import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()

center = 307
right = 410
left = 210

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 20       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)

print('Moving servo on channel 0, press Ctrl-C to quit...')

pwm.set_pwm(0, 0, center)
pwm.set_pwm(4, 0, 1400)
pwm.set_pwm(5, 0, 1400)

i=0
while i<3:
        pwm.set_pwm(0, 0, left)
	time.sleep(1) 
	pwm.set_pwm(0, 0, center)
	time.sleep(1)
        pwm.set_pwm(0, 0, left)
	time.sleep(1)
        pwm.set_pwm(0, 0, center)
        time.sleep(1)
	pwm.set_pwm(0, 0, right)
	time.sleep(1)
	pwm.set_pwm(0, 0, center)
	time.sleep(1)
	pwm.set_pwm(0, 0, right)
	time.sleep(1)
	pwm.set_pwm(0, 0, center)
	time.sleep(1)
	i+=1
pwm.set_pwm(4, 0, 0)
pwm.set_pwm(5, 0, 0)

