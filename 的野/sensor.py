import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # ピン番号で指定
GPIO.setup(22, GPIO.INPUT)# 第一引数にGPIOの出力を設定

print("点灯")

for i in range(3):
    GPIO.output(22, GPIO.HIGH) # highが点灯、low消灯
    time.sleep(0.5) # この間は点灯し続ける
    GPIO.output(22, GPIO.LOW)
    time.sleep(0.5) # この間は消滅し続ける

GPIO.cleanup() # <- 消灯
