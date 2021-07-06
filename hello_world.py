from gpiozero import Button
from time import sleep

button = Button(2)

while True:
    if button.is_pressed:
        print("Hello world")
    else:
        print("Released")
    sleep(1)
