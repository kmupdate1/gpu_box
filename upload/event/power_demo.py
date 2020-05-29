import sys
from threading import Thread

import Jetson.GPIO as GPIO

#from user_event import detect_click as listener
#from user_event import controll_sys as action

from user_event.event_listener import EventNotify
from user_event.event_handler import *
from user_event.event_behavior import *

pin_types = {
	'bcm'   : GPIO.BCM,
	'board' : GPIO.BOARD,
}

click = {
	'1' : True,
	'2' : False,
}

handlers = {
	'single' : SingleHandler(),
	'multi'  : MultipleHandler(),
	'term'   : TermHandler(),
	'all'    : AllHandler(),
}

behaviors = {
	'poweroff' : PoweroffSystem(),
	'sleep'    : SleepSystem(),
	'led'      : BlinkLED(),
}

args = sys.argv

pin_type   = pin_types[args[1]]
input_pin  = int(args[2])
output_pin = int(args[3])
click_type = args[4]

"""
def main():
	listener.PowerListener(listener.PowerHandler(action.LedBlink(pin_type, output_pin), click[click_type]), pin_type, input_pin).listen()
"""

def main():
	

if __name__ == '__main__':
	main()
