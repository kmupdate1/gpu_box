import sys
from threading import Thread

import Jetson.GPIO as GPIO

from user_event import detect_click as listener
from user_event import controll_sys as action

pin_types = {
	'bcm'   : GPIO.BCM,
	'board' : GPIO.BOARD,
}

click = {
	'1' : True,
	'2' : False,
}

args = sys.argv

pin_type   = pin_types[args[1]]
input_pin  = int(args[2])
output_pin = int(args[3])
click_type = args[4]

def main():
	listener.PowerListener(listener.PowerHandler(action.LedBlink(pin_type, output_pin), click[click_type]), pin_type, input_pin).run()

if __name__ == '__main__':
	main()
