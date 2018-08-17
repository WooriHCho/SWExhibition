import RPi.GPIO as GPIO

import Tkinter

GPIO.setmode(GPIO.BOARD)

AIN1 = 13
AIN2 = 15
PWMA = 12

GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(PWMA, 100)

root = Tkinter.Tk()

dir = Tkinter.IntVar()

dir.set(1)

spd = Tkinter.DoubleVar()

spd.set(0)

p.start(0)

def change_dir(dr):
	if(dir.get() == 0):
		GPIO.output(AIN1, GPIO.LOW)
		GPIO.output(AIN2, GPIO.HIGH)
	elif(dir.get() == 1):
		GPIO.output(AIN1, GPIO.LOW)
		GPIO.output(AIN2, GPIO.LOW)
	elif(dir.get() == 2):
		GPIO.output(AIN1, GPIO.HIGH)
		GPIO.output(AIN2, GPIO.LOW)

def change_pw(pw):
	p.ChangeDutyCycle(spd.get())

s1 = Tkinter.Scale(root, label = 'Direction', orient = 'h', \
		from_ = 0, to = 2, variable = dir, command = change_dir)

s1.pack()

s2 = Tkinter.Scale(root, label = 'Speed', orient = 'h', \
		from_ = 0, to = 100, variable = spd, command = change_pw)

s2.pack()

root.mainloop()

p.stop()

GPIO.cleanup()

