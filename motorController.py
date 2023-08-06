import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

GPIO.output(32, False)
GPIO.output(36, False)
GPIO.output(38, False)
GPIO.output(40, False)



def foward():
    GPIO.output(32, True)
    GPIO.output(36, False)
    GPIO.output(38, False)
    GPIO.output(40, False)
    print("Delante")

def stop():
    GPIO.output(32, False)
    GPIO.output(36, True)
    GPIO.output(38, False)
    GPIO.output(40, False)
    print("stop")

def right():
    GPIO.output(32, False)
    GPIO.output(36, False)
    GPIO.output(38, True)
    GPIO.output(40, False)
    print("right")

def left():
    GPIO.output(32, False)
    GPIO.output(36, False)
    GPIO.output(38, False)
    GPIO.output(40, True)
    print("left")                

def kill():
    GPIO.output(32, False)
    GPIO.output(36, False)
    GPIO.output(38, False)
    GPIO.output(40, False)
    print("nada") 

if __name__ == '__main__':
    kill()
    print("start")
    foward()
    time.sleep(2)
    left()
    time.sleep(3)
    right()
    #GPIO.cleanup()
    print("Adios")

