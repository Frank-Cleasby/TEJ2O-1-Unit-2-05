"""
Created by: Frank
Created on: Sep 2025
This module declares the temperature in Kelvin
"""

from microbit import *


display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        temperature = temperature()
        display.clear()
        display.show("The Temperature is:" + (temperature + 273) + "K.")
        display.show(Image.HAPPY)
