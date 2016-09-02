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
        
    def hextest(self, num):
        mask = 0x80
        for _ in range(8):
            if mask&num == 0:
                print 0,
            else:
                print 1,
            mask = mask >> 1
        print
            
    def bout(self, b):
        mask = 0x80
        for _ in range(8):
            self.GPIO.output(self.sclk,self.GPIO.LOW)
            if mask&b:
                self.GPIO.output(self.sid,self.GPIO.HIGH)
            else:
                self.GPIO.output(self.sid,self.GPIO.LOW)
            mask = mask >> 1
            sleep(0.5)
            self.GPIO.output(self.sclk,self.GPIO.HIGH)
            sleep(0.5)
            self.GPIO.output(self.sclk,self.GPIO.LOW)
            
    def bser(self,b,rs=0):
        self.GPIO.output(self.sclk,self.GPIO.LOW)
        self.GPIO.output(self.sid,self.GPIO.LOW)
        self.GPIO.output(self.cs,self.GPIO.HIGH)
        if rs:
            self.bout(0xf8)
        else:
            self.bout(0xfa)
        self.bout(b&0xf0)
        self.bout((b&0x0f)<<4)
        self.GPIO.output(self.sid,self.GPIO.LOW)
        self.GPIO.output(self.cs,self.GPIO.LOW)
        
            
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
    lcd.bser(0xa5)
