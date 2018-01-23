#mainProgram
from ReadyList import *#ready list
from  RCB import * #ready control block
from ListNode import *
def create(name: "PID", priority : "Number"):
	pass
	'''
	create PCB data structure
	init PCB using params
	link PCB to creation tree
	insert(RL, PCB)
	scheduler()  - see who goes next
	'''

def request(rid, n_units):
	pass
	#check if n_units > than start_units
	'''
	r = GET_RCB(rid)
	if(current units >= n):
		u -= n
		insert(self->other_resources, n)
	else:
		self->status.type = Blocked
		self->status.list = r      #the back pointer would point to the resource that is doing the blocking
		remove(RL, self)
		insert(r->waiting_list, self)
		scheduler()
		'''
	
def release(rid, n_units):
	pass
	'''
	r = GET_RCB(rid)
	u = u+n //updating the number of avaliable units, we now have n_units avaliable
	remove(self->Other_resources,r)
	while(r->waiting_list != empty and u >= request):	//units avaliable is greater or equal to the requesting units
		u = u-request
		remove(r->waitingList, q)
		q->status.type = 'ready'
		q->status.list = RL
		insert(q->Other_Resources, r, units)
		insert(RL, q)
	Scheduler
	'''

def Kill_tree(p):
	'''
	for all children processes q, kill tree Q
	free resources  								#free when you get down to the leaves
	delete PCB and update all pointers
	'''

def destroy(PID):
	pass
	'''
	get pointer p to PCB using pid
	Kill_tree(p)
	scheduler()
	'''

	#recursive call that will destroy the root, PID and all the children after





if __name__ == '__main__' :
	lll = LN(5)
	rcb = RCB(5,waiting_list = lll)


	print("") 