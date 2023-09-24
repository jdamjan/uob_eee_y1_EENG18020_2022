from machine import Pin
import utime

pinA1 = Pin(15, Pin.OUT, value=0) #a1
pinB1 = Pin(19, Pin.OUT, value=0) #b1
pinC1 = Pin(1, Pin.OUT, value=0) #c1
pinD1 = Pin(0, Pin.OUT, value=0) #d1
pinE1 = Pin(22, Pin.OUT, value=0) #e1
pinF1 = Pin(21, Pin.OUT, value=0) #f1
pinG1 = Pin(20, Pin.OUT, value=0) #g1

pinA2 = Pin(16, Pin.OUT, value=0) #a2
pinB2 = Pin(18, Pin.OUT, value=0) #b2
pinC2 = Pin(27, Pin.OUT, value=0) #c2
pinD2 = Pin(13, Pin.OUT, value=0) #d2
pinE2 = Pin(14, Pin.OUT, value=0) #e2
pinF2 = Pin(17, Pin.OUT, value=0) #f2
pinG2 = Pin(26, Pin.OUT, value=0) #g2

pins = [
    [pinA1, pinB1, pinC1, pinD1, pinE1, pinF1, pinG1] ,
    [pinA2, pinB2, pinC2, pinD2, pinE2, pinF2, pinG2]
]

digits = [
    [1, 1, 1, 1, 1, 1, 0] ,
    [0, 1, 1, 0, 0, 0, 0] ,
    [1, 1, 0, 1, 1, 0, 1] ,
    [1, 1, 1, 1, 0, 0, 1] ,
    [0, 1, 1, 0, 0, 1, 1] ,
    [1, 0, 1, 1, 0, 1, 1] ,
    [1, 0, 1, 1, 1, 1, 1] ,
    [1, 1, 1, 0, 0, 0, 0] ,
    [1, 1, 1, 1, 1, 1, 1] ,
    [1, 1, 1, 1, 0, 1, 1]
]

def setDigitSegment(digit, value):
    for i in range(0, 7):
        pins[digit][i].value(digits[value][i])

def setDisplay(value):
    digits = []
    dig = 0
    if value == 0:
        setDigitSegment(1, 0)
    else:
        while value > 0:
            if dig < 2: digits = [value % 10] + digits
            value //= 10
            dig += 1
        if dig > 1:
            for i in range(0, 2):
                setDigitSegment(i, digits[i])
        else: setDigitSegment(1, digits[0])

def myISR(pin):
    global countISR
    countISR += increment

increment = 1
countISR = 0
button = Pin(3, Pin.IN, Pin.PULL_DOWN)
button.irq(handler=myISR, trigger=Pin.IRQ_RISING)

while True:
    setDisplay(countISR)