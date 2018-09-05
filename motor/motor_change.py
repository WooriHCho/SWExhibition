from __future__ import division
import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150;
servo_max = 400;
servo_center = 200;

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
pwm.set_pwm_freq(60)

i= servo_center;
print('Moving servo on channel 0, press Ctrl-C to quit...')

pwm.set_pwm(4, 0, 1500)
pwm.set_pwm(5, 0, 1500)

while i < servo_max:
	pwm.set_pwm(0, 0, i)
	time.sleep(1)
	i+= 20
	print(i)
pwm.set_pwm(4, 0, 0)
pwm.set_pwm(5, 0, 0)
