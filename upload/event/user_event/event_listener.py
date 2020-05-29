import time

import Jetson.GPIO as GPIO

from .event_handler import SingleHandler, MultipleHandler, TermHandler

#def detect_span(span):
#	time.sleep(span)

class EventNotify(object):
	def __init__(self, pin_type, input_pin):
		super(NotifyChaged, self).__init__()
		self.__input_pin = input_pin
		self.__handler   = None
		GPIO.setmode(pin_type)
		GPIO.setup(input_pin, GPIO.IN)
		
	def __notify(self):

		try:
			while True:

				value = GPIO.input(self.__input_pin)
				if value == GPIO.LOW:
					self.__handler.active(time.time())
				else:
					self.__handler.inactive(time.time())

				time.sleep(0.01)

		finally:
			GPIO.cleanup()

	def listen(self):
		self.__notify()

	def set_handler(self, handler):
		self.__handler.append(handler)
