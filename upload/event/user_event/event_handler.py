from abc import ABCMeta, abstractmethod

from .event_behavior import *

class Handler(metaclass = ABCMeta):

#	__double_click_pre_time = 0.0

	def __init__(self, behavior):
		super(PowerHandler, self).__init__()
		self.__behavior = behavior
#		self.__is_clicked   = False
#		self.__clicked_time = 0.0
	
	@abstractmethod
	def active(self, current_time):
		if not self.__is_action:
			handl(current_time)
			self.__action_time = current_time
			self.__is_action = True
#		self.__is_clicked   = True
#		self.__clicked_time = current_time

	@abstractmethod
	def inactive(self, current_time):
		if self.__is_action:
			self.__action_time = current_time
			self.__is_action = False
"""
		if self.__click_type:
			self.__three_secs(current_time)
		else:
			self.__double_click()

		self.__is_clicked = False
"""
	@abstractmethod
	def handl(self, current_time):
		pass

"""

	def __three_secs(self, current_time):
		__double_click_pre_time = current_time

		if self.__is_clicked:
			if current_time - self.__clicked_time < 3.0:
				#sleep
				self.__led_blink.print_result("sleep     : ", current_time - self.__clicked_time) ### delete this line ###
				subprocess.call('suspend')
				exit()
			elif current_time - self.__clicked_time < 4.0:
				#shut down
				self.__led_blink.print_result("shut down : ", current_time - self.__clicked_time) ### delete this line ###
				subprocess.call('poweroff')
				exit()
			elif current_time - self.__clicked_time < 5.0:
				pass
			else:
				exit()
				pass

	def __double_click(self, current_time):
		if self.__is_clicked:
			if current_time - self.__clicked_time < 3.0:
				#sleep
				self.__led_blink.print_result("sleep     : ", current_time - self.__clicked_time) ### delete this line ###
			elif current_time - self.__clicked_time < 4.0:
				#shut down
				self.__led_blink.print_result("shut down : ", current_time - self.__clicked_time) ### delete this line ###
			elif :
				pass
			else:
				exit()
				pass
"""

class SingleHandler(Handler):
	"""docstring for SingleHandler"""
	def __init__(self, behavior, receive_type):
		super(SingleHandler, self).__init__(behavior)
		self.__receive_type = receive_type
		self.__is_action   = False
		self.__action_time = 0.0

	def handl(self, current_time):
		self.__behavior.behave()


class MulitpleHandler(Handler):
	"""docstring for MulitpleHandler"""
	def __init__(self, behavior, receive_type):
		super(MulitpleHandler, self).__init__(behavior)
		self.__receive_type   = receive_type
		self.__is_action   = False
		self.__action_time = 0.0

	def handl(self, current_time):
		if current_time - self.__action_time < ??:
			self.__behavior.behave()


class TermHandler(Handler):
	"""docstring for TermHandler"""
	def __init__(self, behavior, receive_type):
		super(TermHandler, self).__init__(behavior)
		self.__receive_type   = receive_type
		self.__is_action   = False
		self.__action_time = 0.0

	def inactive(self, current_time):
		if self.__is_action:
			handl(current_time)
			self.__action_time = current_time
			self.__is_action = False

	def handl(self, current_time):
		if self.__is_action:
			if current_time - self.__clicked_time < 3.0:
				#sleep
				self.__behavior.behave_sample("sleep     : ", current_time - self.__clicked_time) ### delete this line ###
#				subprocess.call('suspend')
#				exit()
			elif current_time - self.__clicked_time < 4.0:
				#shut down
				self.__behavior.behave_sample("shut down : ", current_time - self.__clicked_time) ### delete this line ###
#				subprocess.call('poweroff')
#				exit()
			elif current_time - self.__clicked_time < 5.0:
				pass
			else:
				exit()


class AllHandler(Handler):
	"""docstring for AllHandler"""
	def __init__(self, receive_type):
		super(AllHandler, self).__init__()
		self.__receive_type = receive_type

	def active(self, current_time):
		handl()

	def inactive(self, current_time):
		handl()
