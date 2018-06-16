import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(25, GPIO.OUT)

for i in reange(3):
    GPIO.output(25, GPIO.HIGH)
    time.sleep(0.5) # この間は点灯し続ける
    GPIO.output(25, GPIO.LOW)
    time.sleep(0.5) # この間は点灯し続ける

GPIO.cleanup() # <- 消灯
