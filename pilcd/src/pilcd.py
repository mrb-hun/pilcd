#!/usr/bin/python
# Raspberry Pi Lcd class

from time import sleep

class PiLcd(object):
    def __init__(self, cs=18, sclk=17, sid=27, GPIO=None):
        if not GPIO:
            import RPi.GPIO as GPIO
            GPIO.setwarnings(False)
        self.GPIO = GPIO
        self.cs = cs
        self.sclk = sclk
        self.sid = sid
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(self.cs,self.GPIO.OUT)
        self.GPIO.setup(self.sclk,self.GPIO.OUT)
        self.GPIO.setup(self.sid,self.GPIO.OUT)
        
    
    def ledtest(self):
        self.GPIO.output(self.cs,self.GPIO.HIGH)
        sleep(3.e-7)
        sleep(0.2)
        self.GPIO.output(self.cs,self.GPIO.LOW)
        self.GPIO.output(self.sclk,self.GPIO.HIGH)
        sleep(0.2)
        self.GPIO.output(self.sclk,self.GPIO.LOW)
        self.GPIO.output(self.sid,self.GPIO.HIGH)
        sleep(0.2)
        self.GPIO.output(self.sid,self.GPIO.LOW)
 
if __name__ == "__main__":
    lcd = PiLcd()
    for _ in range(10):
        lcd.ledtest()
