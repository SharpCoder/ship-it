import json
import boto3
from gpiozero import LED, Button
from time import sleep
from libs import S3Client
from libs import Api

# define the gpio things
arm_button = Button(1)
deploy_button = Button(2)
armed = LED(17)
working = LED(18)
finished = LED(19)

# Setup the clients
api = Api.Api()
client = S3Client.S3Client()

def do_action():
    commands = json.loads(client.get_object("mudon", "ship-it/rest.json").read())
    for command in commands:
        api.invoke(command)
    finished.on()

# Wait for the arm button to be pressed and then turn on the armed LED
# and then wait for the button to be released and blink the button a bit then
# do the action
arm_button.wait_for_press()
armed.on()
deploy_button.wait_for_release()

done = False
blinked = False
invoked = False
blink_period = 18
blink_current = blink_period
blink_working = True

while True:
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
        if not invoked:
            invoked = True
            do_action()