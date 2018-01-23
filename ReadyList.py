#Ready List
from PCB import *
from ListNode import *
class ReadyList:
	def __init__(self, initList = None, userList = None, systemList = None):
		self.initList = initList #should only have one, might have to be a linked list that point to various PCB
		self.userList = userList
		self.systemList = systemList

	#assuming that the LN is a list Node/ linked list.
	def set_initList(self, LN):
		self.initList = LN 

	def set_userList(self, LN):
		self.userList = LN

	def set_systemList(self,LN):
		self.systemList = LN

'''
this is how it would look.
	rl = ReadyList()
	ll = LN(5)
	rl.set_initList(ll)
'''