#Resource Control Block
class RCB:
	def __init__(self, Ri = None, start_units = None, current_units = None , waiting_list = None):
		self.RID = Ri
		self.start_units = start_units
		self.current_units = current_units
		self.waiting_list = waiting_list #list of blocked resource


	def set_RID(self, RID):
		self.RID = RID

	def set_startUnits(self,units):
		self.start_units = units

	def set_currentUnits(self,units):
		self.current_units = units

	#assuming that LN is a list head/linked list
	def set_waitingList(self,LN):
		self.waiting_list = LN

	def get_RID(self):
		return self.RID

	def get_startUnits(self):
		return self.start_units

	def get_currentUnits(self):
		return self.current_units

	def get_waitingList(self):
		return self.waiting_list

#results of request