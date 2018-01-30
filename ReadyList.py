#Ready List
from PCB import *
from ListNode import *
class ReadyList:
	def __init__(self, initList = None, userList = None, systemList = None):
		self.initList = initList #should only have one, might have to be a linked list that point to various PCB
		self.userList = userList
		self.systemList = systemList

	#assuming that the LN is a list Node/ linked list.
	def set_list(self, priority, LN):
		if(priority > 2):
			raise Exception("that priority is out of range")
		if(priority == 0):
			self.initList = LN
		elif(priority == 1):
			self.userList = LN
		else:
			self.systemList = LN
			
	def get_List(self,num: "priority"):
		return self.initList if (num == 0) else self.userList if (num == 1) else self.systemList
'''
this is how it would look.
	rl = ReadyList()
	ll = LN(5)
	rl.set_initList(ll)
'''