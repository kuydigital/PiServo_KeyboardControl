#Pi Servo Keyboard Control by Oliver Kuy a.k.a. kuydigital

#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from PCA9685 import PCA9685
import curses

pwm = PCA9685()
r = 90
l = 90
u = 90
d = 90

# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)
 
try:
    pwm.setPWMFreq(50)
    pwm.setRotationAngle(1, 90)
    pwm.setRotationAngle(0, 90)
    
    while True:
        char = screen.getch()
        if char == ord('q'):
            pwm.setRotationAngle(1, 90)
            pwm.setRotationAngle(0, 90)
            break
        
        if char == curses.KEY_RIGHT:
            r=r+1
            l=l+1
            screen.addstr(0, 0, 'right')
            pwm.setRotationAngle(0, r)
            
        if char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
            l=l-1
            r=r-1
            pwm.setRotationAngle(0, l)
            
        if char == curses.KEY_UP:
            screen.addstr(0, 0, 'up   ')
            u=u-1
            d=d-1
            pwm.setRotationAngle(1, u)
                   
        if char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
            d=d+1
            u=u+1
            pwm.setRotationAngle(1, d)
            
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()