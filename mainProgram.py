#mainProgram
from ReadyList import *#ready list
from  RCB import * #ready control block
from ListNode import *

def create(name: "PID", priority : "Number", RL : "ReadyList"): #parent : "PCB" the paprent portion came from 10:02 from lecture 2
	newPCB = PCB(name,priority)
	parent = RL.get_List(2) if (RL.get_List(2) != None and RL.get_List(2).type == "Running") else RL.get_List(1) if (RL.get_List(1) != None and RL.get_List(1).type == "Running") else Rl.get_List(0)
	parentChildren = parent.get_child() #returns the head pointer of the children of running RL
	appendNode(parentChildren, newPCB)
	# while(parentChildren != None):
	# 	parentChildren = parentChildren.next 
	# parentChildren.next = LN(newPCB)  #setting the child val within the PARENT PCB
	newPCB.set_parent(parent)
	newPCB.set_back_list(RL)	

	parentLN = RL.get_List(priority);
	if(parentLN == None):
		set_list(priority,LN(newPCB))
	else:
		appendNode(parentLN, newPCB) #this will append the newPCB at the back of the linkedlist.


	#call scheduler

	'''
	create PCB data structure
	init PCB using params
	link PCB to creation tree
	insert(RL, PCB)
	scheduler()  - see who goes next
	'''
def getCurrentlyRunning(RL):
	level=0
	if(RL.get_List(2) != None and RL.get_List(2).value.get_type() == "Running"):
		currRunning = RL.get_List(2)
		level  =2
	elif(RL.get_List(1) != None and RL.get_List(1).value.get_type() == "Running"):
		currRunning = RL.get_List(1)
		level = 1
	elif(RL.get_List(0) != None and RL.get_List(0).value.get_type() == "Running"):
		currRunning = RL.get_List(0)
	return currRunning, level

def request(rid, n_units, RCBList, RL):
	#also going to have a list param, that has all 4 RCB's and so you can iterate through and look for the 
	#correct RID. 
	#Getting the correct RCB
	for rcb in RCBList:
		if(rcb.get_RID() == rid):
			RCB = rcb
	currRunning, level = getCurrentlyRunning(RL)
		
	if(RCB.get_currentUnits() >= n_units): #we were able to subtract some units within the RCB
		RCB.set_currentUnits(RCB.get_currentUnits()-n_units)
		currRunning.value.other_resources[rid] += n_units	#increment the values within the default dict.
	else:
		currRunning.value.set_type("Blocked")
		currRunning.value.set_back_list(RCB)
		RL.set_list(level, delHeadNode(RL.get_List(level))) #this deletes the head node, for that particular level
		insert_waitingList(RCB, (currRunning,n_units))   #the currently running pcb along wiht n_units is now inserted into the waiting list of the resource
		print("this is the curr running", RCB.waiting_list.value)
		print("this is the units: ", RCB.waiting_list.value[1])
		print("go tto the end else statement")
		return;
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
		insert(r->waiting_list, self)	#put it at the back of the ready list. 
		scheduler()
		'''
	
def release(rid, n_units, RCBList, RL):
	for rcb in RCBList:
		if(rcb.get_RID() == rid):
			RCB = rcb
	RCB.set_currentUnits(RCB.get_currentUnits()+n_units) #increased the number of units
	#we have to release from the currently running process. 
	currRunning, level = getCurrentlyRunning(RL) #currRunning is a ListNode of a PCB
	currRunning.value.other_resources[rid] = 0 #setting the value of the RID equal to 0, essentially deleting the value from the dictionary
	while(RCB.waiting_list != None and n_units >= RCB.waiting_list.value[1]):

	pass
	'''
	r = GET_RCB(rid)
	u = u+n //updating the number of avaliable units, we now have n_units avaliable
	remove(self->Other_resources,r)
	while(r->waiting_list != empty and u >= request):	//units avaliable is greater or equal to the requesting units of the PCB on the waiting list
		u = u-request
		remove(r->waitingList, q)
		q->status.type = 'ready'
		q->status.list = RL
		insert(q->Other_Resources, r, units)
		insert(RL, q)
	Scheduler
	'''
def get_PCB_priority(RL,p):
	currPCB = None
	priority = 2
	if(findNode(RL.get_List(2),p.PID)):
		#we know that the PID is in the LL of val 2...
		currPCB = RL.get_List(2)
	elif(findNode(RL.get_List(1),p.PID)):
		currPCB = RL.get_List(1)
		priority = 1
		#currPCB = getNodeLN(RL.get_List(1), p.PID)
	elif(findNode(RL.get_List(0),p.PID)):
		currPCB = RL.get_List(0)
		priority = 0
	return currPCB, priority
	
#WITHIN HERE HAVE TO LOOK OUT FOR THE BLOCKED LIST TO SEE IF THE PROCESS IS ON THERE TOO
#OTHERWISE THINGS COULD GO VERY WRONG...

def Kill_tree(RL,p):
	if(p.child == None): #we know that there is nothing that spawned off of it
		tempPCB = get_PCB_priority(RL,p)
		if(tempPCB[0].value.PID == p.PID): #This is the first PCB....
			RL.set_list(tempPCB[1], delHeadNode(tempPCB[0]))
			print("got to remove node:, ",p.PID, "currentPCB: ", tempPCB[0])
		else:
			print("got to remove node second: ",p.PID)
			removeNode(tempPCB[0], p.PID)
		return
	for child in p.child:
		Kill_tree(RL,child)

	tempPCB = get_PCB_priority(RL,p)
	if(tempPCB[0].value.PID == p.PID): #This is the first PCB....
		RL.set_list(tempPCB[1], delHeadNode(tempPCB[0]))
		print("got to remove node:, ",p.PID, "currentPCB: ", tempPCB[0])
	else:
		print("got to remove node second: ",p.PID)
		removeNode(tempPCB[0], p.PID)
	return
	'''
	for all children processes q, kill tree Q
	free resources  								#free when you get down to the leaves
	delete PCB and update all pointers
	'''

def destroy(RL,PID):
	#not too sure how to get the value of the PCB....
	currPCB = None
	if(findNode(RL.get_List(2),PID)):
		#we know that the PID is in the LL of val 2...
		currPCB = getNode(RL.get_List(2), PID) #This is now equal to the PCB with the PID
	elif(findNode(RL.get_List(1),PID)):
		currPCB = getNode(RL.get_List(1), PID)
	elif(findNode(RL.get_List(0),PID)):
		currPCB = getNode(RL.get_List(0), PID)
	if(currPCB == None):
		raise Exception("PID Not in ReadyList")
	Kill_tree(RL,currPCB)
	'''
	get pointer p to PCB using pid
	Kill_tree(p)
	scheduler()
	'''

	#recursive call that will destroy the root, PID and all the children after





if __name__ == '__main__' :
	
	rl = ReadyList()
	pb = LN(PCB(4,2))
	pb.value.set_type("Running")
	appendNode(pb,PCB(6,2))
	rl.set_list(2,pb)

	r1 = RCB(1532,20,20)
	r2 = RCB(1533,20,20)
	r3 = RCB(1534,20,20)
	r4 = RCB(1535,20,20)
	RCBList = [r1,r2,r3,r3]

	request(1532,200,RCBList, rl)

	pb2 = LN(PCB(6,2))
	pb2.value.set_type("Running")
	appendNode(pb,PCB(7,2))
	rl.set_list(2,pb2)

	request(1532,200,RCBList, rl)
	for k,v in pb.value.get_other_resources().items():
		print("key: ", k, " value: ", v)

	for ele in r1.waiting_list:
		print("ele: ",ele[0].value.PID)
	# rl = ReadyList()
	# pb = LN(PCB(4,2))
	# appendNode(pb,PCB(6,2))
	# rl.set_list(2,pb)
	# z = LN(PCB(8,1))
	# rl.set_list(1,z)
	# father = PCB(7,1)
	# c1 = PCB(5,2)
	# c2 = PCB(4,2)
	# c1.set_child(LN(c2))
	# rl.set_list(2,LN(c1))
	# father.set_child(LN(c1))
	# appendNode(rl.get_List(2),c2)
	# appendNode(rl.get_List(1),father)
	# for v in rl.get_List(1):
	# 	print("pid is : ", v.PID)
	# for v in rl.get_List(2):
	# 	print("pid is : ", v.PID)

	# #rl.set_list(1,removeNode(rl.get_List(1),8)) # could do this, or just check if val is the first one and then call delHeadNode

	# destroy(rl, 7)

	# for v in rl.get_List(1):
	# 	print("pid is : ", v.PID)
	# print(rl.get_List(2))
	# for v in rl.get_List(2):
	# 	print("pid is : ", v.PID)



# 	lll = LN(5)
# 	appendNode(lll, 4)
# #setter methods for a linked list. 
# 	rl.set_list(1,lll)
# 	appendNode(rl.get_List(1),7)
# 	for ele in rl.get_List(1):
# 		print(ele)
# 	destroy()
# 	#print(x.value)
# 	rcb = RCB(5,waiting_list = lll)


	print("") 

	#How to use the LN along with the destory function. 
	# rl = ReadyList()

	# pb = LN(PCB(4,2))
	# appendNode(pb,PCB(6,2))
	# rl.set_list(2,pb)
'''
		if(p.child == None): #we know that there is nothing that spawned off of it
		currPCB = None
		priority = 2
		if(findNode(RL.get_List(2),p.PID)):
			#we know that the PID is in the LL of val 2...
			currPCB = RL.get_List(2)
		elif(findNode(RL.get_List(1),p.PID)):
			currPCB = RL.get_List(1)
			priority = 1
			#currPCB = getNodeLN(RL.get_List(1), p.PID)
		elif(findNode(RL.get_List(0),p.PID)):
			currPCB = RL.get_List(0)
			priority = 0
			#currPCB = getNodeLN(RL.get_List(0), p.PID)
		print("This is the current value of pcb: ",currPCB.value.PID)
		if(currPCB.value.PID == p.PID): #This is the first PCB....
			RL.set_list(priority, delHeadNode(currPCB))
			print("got to remove node:, ",p.PID, "currentPCB: ", currPCB)
		else:
			print("got to remove node second: ",p.PID)
			removeNode(currPCB, p.PID)
		return
	for child in p.child:
		Kill_tree(RL,child)
	currPCB = None
	priority = 2
	if(findNode(RL.get_List(2),p.PID)):
		#we know that the PID is in the LL of val 2...
		currPCB = RL.get_List(2)
	elif(findNode(RL.get_List(1),p.PID)):
		currPCB = RL.get_List(1)
		priority = 1
		#currPCB = getNodeLN(RL.get_List(1), p.PID)
	elif(findNode(RL.get_List(0),p.PID)):
		currPCB = RL.get_List(0)
		priority = 0
		#currPCB = getNodeLN(RL.get_List(0), p.PID)
	print("This is the current value of pcb: ",currPCB.value.PID)
	if(currPCB.value.PID == p.PID): #This is the first PCB....
		RL.set_list(priority, delHeadNode(currPCB))
		print("got to remove node:, ",p.PID, "currentPCB: ", currPCB)
	else:
		print("got to remove node second: ",p.PID)
		removeNode(currPCB, p.PID)
	return
	'''