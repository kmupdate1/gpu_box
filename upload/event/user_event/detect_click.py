import sys
import time
import subprocess

import Jetson.GPIO as GPIO

from .controll_sys import LedBlink

class PowerListener(object):
	"""docstring for PowerListener"""
	def __init__(self, handler, pin_type, input_pin):
		super(PowerListener, self).__init__()
		self.__handler   = handler
		self.__input_pin = input_pin
		self.__mode      = GPIO.setmode(pin_type)
		self.__setting   = GPIO.setup(input_pin, GPIO.IN)
		
	def __listen(self):

		try:
			called_low = False
			while True:

				value = GPIO.input(self.__input_pin)
				if value == GPIO.LOW:
					if not called_low:
						self.__handler.clicked(time.time())
						called_low = True
				else:
					if called_low:
						self.__handler.unclicked(time.time())
						called_low = False

				time.sleep(0.01)

		finally:
			GPIO.cleanup()

	def run(self):
		self.__listen()

class PowerHandler(object):

	__double_click_pre_time = 0.0

	def __init__(self, led_blink, click_type):
		super(PowerHandler, self).__init__()
		self.__led_blink    = led_blink
		self.__click_type   = click_type
		self.__is_clicked   = False
		self.__clicked_time = 0.0
	
	def clicked(self, current_time):
		self.__is_clicked   = True
		self.__clicked_time = current_time

	def unclicked(self, current_time):
		if self.__click_type:
			self.__three_secs(current_time)
		else:
			self.__double_click()

		self.__is_clicked = False

	def __three_secs(self, current_time):
		__double_click_pre_time = current_time

		if self.__is_clicked:
			if current_time - self.__clicked_time < 3.0:
				#sleep
				self.__led_blink.print_result("sleep     : ", current_time - self.__clicked_time) ### delete this line ###
#				subprocess.call('suspend')
#				exit()
			elif current_time - self.__clicked_time < 4.0:
				#shut down
				self.__led_blink.print_result("shut down : ", current_time - self.__clicked_time) ### delete this line ###
#				subprocess.call('poweroff')
#				exit()
			elif current_time - self.__clicked_time < 5.0:
				pass
			else:
				exit()
#				pass

	def __double_click(self, current_time):
		if self.__is_clicked:
			if current_time - self.__clicked_time < 3.0:
				#sleep
				self.__led_blink.print_result("sleep     : ", current_time - self.__clicked_time) ### delete this line ###
			elif current_time - self.__clicked_time < 4.0:
				#shut down
				self.__led_blink.print_result("shut down : ", current_time - self.__clicked_time) ### delete this line ###
#			elif :
#				pass
			else:
				exit()
#				pass
