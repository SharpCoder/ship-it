import boto3
from gpiozero import LED, Button
from time import sleep
import S3Client

button = LED(2)
armed = LED(17)
working = LED(18)
finished = LED(19)

done = False
blinked = False
blink_working = False

blink_period = 1
blink_current = blink_period

while True:
    if button.is_pressed:
        blink_working = True
        blink_period = 18
    
    if blink_working:
        blinked = not blinked
        if blinked:
            working.on()
        else:
            working.off()

    if done:
        finished.on()
        blink_working = False
    
    sleep(blink_current)

    blink_current -= 1
    if blink_current < 0:
        blink_current = blink_period
