class LN:
    def __init__(self : "LN", value : object , next : "LN" = None):
        self.value = value
        self.next  = next

class PCB:
	def __init__(self, ID, p):
		self.PID = ID
		self.priority = p
		self.other_resources = None #this is supposed to be a linked list which points to mem allocated
		self.type = "Ready" #running blocked ready
		self.back_list = []#if running then pointing to the RL, if is it blocked, points to the resources which is blocking it
		self.parent; #pointer to another PCB
		self.child;      #linked list with pointer to many pcb's 




	#create main function. to get the data inputted by the user