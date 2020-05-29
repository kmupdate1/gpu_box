from abc import ABCMeta, abstractmethod

from .event_behavior import *

class Handler(metaclass = ABCMeta):

	def __init__(self):
		super(PowerHandler, self).__init__()
		self.__behavior = None
	
	@abstractmethod
	def active(self, current_time):
		if not self.__is_action:
			handl(current_time)
			self.__action_time = current_time
			self.__is_action = True

	@abstractmethod
	def inactive(self, current_time):
		if self.__is_action:
			self.__action_time = current_time
			self.__is_action = False

	@abstractmethod
	def handl(self, current_time):
		pass

	def set_behavior(self, behavior):
		self.__behavior.append(behavior)


class SingleHandler(Handler):
	def __init__(self, receive_type):
		super(SingleHandler, self).__init__()
		self.__receive_type = receive_type
		self.__is_action   = False
		self.__action_time = 0.0

	def handl(self, current_time):
		self.__behavior.behave()


class MulitpleHandler(Handler):
	def __init__(self, receive_type):
		super(MulitpleHandler, self).__init__()
		self.__receive_type   = receive_type
		self.__is_action   = False
		self.__action_time = 0.0

	def handl(self, current_time):
		if current_time - self.__action_time < """??????""":
			self.__behavior.behave()


class TermHandler(Handler):
	def __init__(self, receive_type):
		super(TermHandler, self).__init__()
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
	def __init__(self, receive_type):
		super(AllHandler, self).__init__()
		self.__receive_type = receive_type

	def active(self, current_time):
		handl()

	def inactive(self, current_time):
		handl()
