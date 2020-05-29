import subprocess
import time

import Jetson.GPIO as GPIO


class PoweroffSystem(object):
	def __init__(self):
		super(PoweroffSystem, self).__init__()

	def behave(self):
		#poweroff
		subprocess.call('poweroff')
		exit()
		
class SleepSystem(object):
	def __init__(self):
		super(SleepSystem, self).__init__()

	def behave(self):
		#sleep
		subprocess.call('systemctl suspend')
#		sleepのときはアプリケーション終了するのか？特定のオブジェクトだけkillするとか？
#		exit()
		
class BlinkLED(object):
	def __init__(self, pin_type, output_pin):
		super(BlinkLED, self).__init__()
		self.__pin_type = pin_type
		self.__output_pin = output_pin

	def __blink(self):
		GPIO.setmode(self.__pin_type)
		GPIO.setup(self.__output_pin, GPIO.OUT, initial = GPIO.HIGH)
		
		curr_value = GPIO.HIGH
		try:
			GPIO.output(self.__output_pin, curr_value)
			curr_value ^= GPIO.HIGH
		finally:
			GPIO.cleanup()

	def behave(self):
		self.__blink()

	def behave_sample(self, message, clicked_time):
		print("{}{}".format(message, clicked_time))
