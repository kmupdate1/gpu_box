import time

import Jetson.GPIO as GPIO


class SystemPoweroff(object):
	"""docstring for SystemPoweroff"""
	def __init__(self, arg):
		super(SystemPoweroff, self).__init__()
		self.arg = arg
		
class SystemSleep(object):
	"""docstring for SystemSleep"""
	def __init__(self, arg):
		super(SystemSleep, self).__init__()
		self.arg = arg
		
class BlinkLED(object):
	"""docstring for LedBlink"""
	def __init__(self, pin_type, output_pin):
		super(LedBlink, self).__init__()
		self.__pin_type = pin_type
		self.__output_pin = output_pin

	def __blink(self):
		GPIO.setmode(self.__pin_type)
		GPIO.setup(self.__output_pin, GPIO.OUT, initial=GPIO.HIGH)
		
		curr_value = GPIO.HIGH
		try:
			GPIO.output(self.__output_pin, curr_value)
			curr_value ^= GPIO.HIGH
		finally:
			GPIO.cleanup()

	def call_back(self):
		self.__blink()

	def behave_sample(self, message, clicked_time):
		print("{}{}".format(message, clicked_time))
