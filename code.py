import board
import time
import simpleio
import pulseio

buzzer = pulseio.PWMOut(board.D3, frequency=5000, duty_cycle=0)
pump = simpleio.DigitalOut(board.D13)

def cyclePump():
    # Ultimately the timing for on/off will be more like 30 on and 3600 off.
    pump.value = True
    time.sleep(1)
    pump.value = False

def makeBeep():
    #mostly for learning purposes, but emits a quick beep pattern - disable when running via battery?
    buzzer.duty_cycle = 65535
    time.sleep(0.08)
    buzzer.duty_cycle = 0
    time.sleep(0.1)
    buzzer.duty_cycle = 65535
    time.sleep(0.08)
    buzzer.duty_cycle = 0

def generateO2():
    makeBeep()
    cyclePump()

while True:
    generateO2()
    time.sleep(10)


