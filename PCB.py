from ReadyList import *#ready list
from  RCB import * #ready control block
from ListNode import *
class PCB:
	def __init__(self, ID, p):
		self.PID = ID 	#name that is given
		self.priority = p #(0,1,2)  
		self.other_resources = None #this is supposed to be a linked list of RCB's
		self.type = "Ready" #running blocked ready
		self.back_list = None#if running then pointing to the RL, if is it blocked, points to the resources which is blocking it
		self.parent = None; #pointer to another PCB
		self.child = None;      #linked list with pointer to many pcb's 

	def set_priority(self,p):
		if  (p <= 2 and p > 0):
			self.priority = p

	def set_other_resources(self,LN):
		self.other_resources = LN

	def set_type(self,newType):
		self.type = newType

	def set_back_list(self, LN):
		self.back_list = LN 
		#note that this could be different, could be RL and could be pointing to the resource that is blocking it

	def set_parent(self, parentLN):
		self.parent = parentLN

	def set_child(self, childLN):
		self.child = childLN

	def get_ID(self):
		return self.PID

	def get_priority(self):
		return self.priority

	def get_other_resources(self):
		return self.other_resources

	def get_type(self):
		return self.type

	def get_back_list(self):
		return self.back_list

	def get_parent(self):
		return self.parent

	def get_child(self):
		return self.child

'''
an example of how you would use some of the metthods, they are all internal so you have to say pcb.Whatever_function
not like with the list Nodes where they were outside of the function. 
	pcb = PCB(5,1)
	pcb.set_priority(2)
	print(pcb.get_priority())
	print("")
'''

	#create main function. to get the data inputted by the user