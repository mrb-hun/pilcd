#!/usr/bin/python
# Raspberry Pi Lcd class

from time import sleep

class PiLcd(object):
    def __init__(self, cs=17, sclk=18, sid=27, GPIO=None):
        if not GPIO:
            import RPi.GPIO as GPIO
            GPIO.setwarnings(False)
        self.GPIO = GPIO
        self.cs = cs
        self.sclk = sclk
        self.sid = sid
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(self.pin.cs,GPIO.OUT)
        self.GPIO.setup(self.pin.sclk,GPIO.OUT)
        self.GPIO.setup(self.pin.sid,GPIO.OUT)
        
    
    def ledtest(self):
        self.GPIO.output(self.cs,GPIO.HIGH)
        sleep(3.e-7)
        sleep(0.2)
        self.GPIO.output(self.cs,GPIO.LOW)
        self.GPIO.output(self.sclk,GPIO.HIGH)
        sleep(0.2)
        self.GPIO.output(self.sclk,GPIO.LOW)
        self.GPIO.output(self.sdi,GPIO.HIGH)
        sleep(0.2)
        self.GPIO.output(self.sdi,GPIO.LOW)
 
if __name__ == "__main__":
    lcd = PiLcd()
    for _ in range(10):
        lcd.ledtest()
