import time

import Jetson.GPIO as GPIO

from .event_handler import SingleHandler, MultipleHandler, TermHandler

#def detect_span(span):
#	time.sleep(span)

class EventNotify(object):
	"""docstring for NotifyChaged"""
	def __init__(self, handler, pin_type, input_pin):
		super(NotifyChaged, self).__init__()
		self.__handler   = handler
		self.__input_pin = input_pin
		self.__mode      = GPIO.setmode(pin_type)
		self.__setting   = GPIO.setup(input_pin, GPIO.IN)
		
	def __notify(self):

		try:
#			called_low = False
			while True:

				value = GPIO.input(self.__input_pin)
				if value == GPIO.LOW:
#					if not called_low:
					self.__handler.active(time.time())
#						called_low = True
				else:
#					if called_low:
					self.__handler.inactive(time.time())
#						called_low = False

				time.sleep(0.01)

		finally:
			GPIO.cleanup()

	def listen(self):
		self.__notify()
