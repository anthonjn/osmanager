#mainProgram
from ReadyList import *#ready list
from  RCB import * #ready control block
from ListNode import *



def create(name: "PID", priority : "Number", RL : "ReadyList"): #parent : "PCB" the paprent portion came from 10:02 from lecture 2
	newPCB = PCB(name,priority)
	parent = RL.get_List(2).value if (RL.get_List(2) != None and RL.get_List(2).value.type == "Running") else RL.get_List(1).value if (RL.get_List(1) != None and RL.get_List(1).value.type == "Running") else RL.get_List(0).value
	parentChildren = parent.get_child() #returns the head pointer of the children of running RL
	if(parentChildren == None):
		parent.set_child(LN(newPCB))
	else:
		appendNode(parentChildren, newPCB)

	# while(parentChildren != None):
	# 	parentChildren = parentChildren.next 
	# parentChildren.next = LN(newPCB)  #setting the child val within the PARENT PCB
	newPCB.set_parent(parent)
	newPCB.set_back_list(RL)	

	parentLN = RL.get_List(priority)
	if(parentLN == None):
		RL.set_list(priority,LN(newPCB))
	else:
		appendNode(parentLN, newPCB) #this will append the newPCB at the back of the linkedlist.
	scheduler(RL,0)

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
	currRunning = 0
	if(RL.get_List(2) != None and RL.get_List(2).value.get_type() == "Running"):
		currRunning = RL.get_List(2)
		level  =2
	elif(RL.get_List(1) != None and RL.get_List(1).value.get_type() == "Running"):
		currRunning = RL.get_List(1)
		level = 1
	elif(RL.get_List(0) != None and RL.get_List(0).value.get_type() == "Running"):
		currRunning = RL.get_List(0)
	return currRunning, level

def getHighestPcb(RL):
	level=0
	currRunning = 0
	if(RL.get_List(2) != None):
		currRunning = RL.get_List(2)
		level  =2
	elif(RL.get_List(1) != None):
		currRunning = RL.get_List(1)
		level = 1
	elif(RL.get_List(0) != None):
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
	print("CURRENT UNITS: ",RCB.get_currentUnits(), "units requesting: ",n_units)
	if(RCB.get_currentUnits() >= n_units): #we were able to subtract some units within the RCB

		RCB.set_currentUnits(RCB.get_currentUnits()-n_units)
		print("Now current units: ",RCB.get_currentUnits())
		currRunning.value.other_resources[rid] += n_units	#increment the values within the default dict.
	else:
		currRunning.value.set_type("Blocked")
		currRunning.value.set_back_list(RCB)
		RL.set_list(level, delHeadNode(RL.get_List(level))) #this deletes the head node, for that particular level
		insert_waitingList(RCB, (currRunning.value,n_units))   #the currently running pcb along wiht n_units is now inserted into the waiting list of the resource
		# print("this is the curr running", RCB.waiting_list.value)
		# print("this is the units: ", RCB.waiting_list.value[1])
		# print("this is the units: ", RCB.waiting_list.value[0].PID)
		# print("go tto the end else statement")
	scheduler(RL,1)
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
		insert(r->waiting_list, self)	#put it at the back of the waiting list. 
		scheduler()
		'''
	
def release(rid, n_units, RCBList, RL): #something has to be running before it can release anythin
	for rcb in RCBList:
		if(rcb.get_RID() == rid):
			RCB = rcb
	RCB.set_currentUnits(RCB.get_currentUnits()+n_units) #increased the number of units
	#we have to release from the currently running process. 
	currRunning, level = getCurrentlyRunning(RL) #currRunning is a ListNode of a PCB
	currRunning.value.other_resources[rid] = 0 #setting the value of the RID equal to 0, essentially deleting the value from the dictionary
	waitList = RCB.get_waitingList()

	# print("before while loop")
	# print("this is waitlist: ", waitList)
	# print("this is RCB's current units, ", RCB.get_currentUnits())
	# print("waitlist val: ",waitList.value[1])

	while(waitList != None and RCB.get_currentUnits() >= waitList.value[1]):
		newPCB = waitList.value[0] #this is a PCB, that we have to add to the back
		#print("this should be PCB: ",newPCB)
		RCB.set_currentUnits(RCB.get_currentUnits()-n_units) #sub units bc we are running that instance
		RCB.set_waitingList(removeNodeWaitingList(RCB.get_waitingList(), waitList.value)) #removes the node within the waiting list in the RCB.
		newPCB.set_type("Ready")
		newPCB.set_back_list(RL)
		newPCB.other_resources[rid] += n_units
		parentLN = RL.get_List(newPCB.get_priority())
		if(parentLN == None):
			set_list(priority,LN(newPCB))
		else:
			appendNode(parentLN, newPCB) #this will append the newPCB at the back of the linkedlist.
		waitList = waitList.next
		#print("inside while loop:")
	#print("finished the release")
	scheduler(RL,0)
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
	priority = -1
	if(findNode(RL.get_List(2),p.PID)):
		#we know that the PID is in the LL of val 2...
		currPCB = RL.get_List(2)
		priority = 2
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
def updateResources(RCBList, p, RL):
	#this is the PID WE WANT TO PUDATE RESOURCES FOR
	RCB = None
	unit = 0
	for RID, units in p.other_resources.items():
		#print("this is RID: ", RID, "units: ", units)
		for resource in RCBList:
			if(resource.RID == RID):
				RCB = resource
				unit = units
				RCB.set_currentUnits(RCB.get_currentUnits() + unit) #update the num of units, and then add new process to the RL
				#print("this is the resource's current units: ",RCB.get_currentUnits())
				waitList = RCB.get_waitingList()

				while(waitList != None and RCB.get_currentUnits() >= waitList.value[1]):
					newPCB = waitList.value[0] #this is a PCB, that we have to add to the back OF READY LIST
					#print("this should be PCB: ",newPCB)
					RCB.set_currentUnits(RCB.get_currentUnits()-unit) #sub units bc we are running that instance
					RCB.set_waitingList(removeNodeWaitingList(RCB.get_waitingList(), waitList.value)) #removes the node within the waiting list in the RCB.
					newPCB.set_type("Ready")
					newPCB.set_back_list(RL)
					newPCB.other_resources[RCB.RID] += unit
					parentLN = RL.get_List(newPCB.get_priority())
					if(parentLN == None):
						RL.set_list(newPCB.get_priority(),LN(newPCB))
					else:
						appendNode(parentLN, newPCB) #this will append the newPCB at the back of the linkedlist.
					waitList = waitList.next
				break
	if(RCB == None):
		return
	


def Kill_tree(RL,p, RCBList):
	#print("this is the PID: ", p.PID)
	if(p.child == None): #we know that there is nothing that spawned off of it
		updateResources(RCBList, p, RL)
		tempPCB = get_PCB_priority(RL,p)
		if(tempPCB[1] != -1):
			#This means that it'sn not within the RCB's 
			#HAVE TO REMEMBER TO GO BACK AND DELETE IT FROM THE PARENT.
			#print("***********************************", p.PID)
			if(tempPCB[0].value.PID == p.PID): #This is the first PCB....
				RL.set_list(tempPCB[1], delHeadNode(tempPCB[0]))
				#print("got to remove node:, ",p.PID, "currentPCB: ", tempPCB[0])
			else:
				#print("got to remove node second: ",p.PID)
				RL.set_list(tempPCB[1],removeNode(tempPCB[0], p.PID))
			
			if(p.parent != None):
				#go into the parent and delete this p.PID
				parentPCB = p.get_parent()
				parentPCB.set_child(removeNode(parentPCB.get_child(), p.PID))
			return
		#this value is within the waiting list
		tempRCB = None
		currWaitList = None
		for RCB in RCBList:
			#print("this is the PID we have ", p.PID)
			if (RCB.get_waitingList() != None and findNodeWL(RCB.get_waitingList(), p.PID)):
				currWaitList = RCB.get_waitingList() #this will get the right value within the waiting list
				tempRCB = RCB
		if(currWaitList.value[0].PID == p.PID): #first value
			tempRCB.set_waitingList(delHeadNode(currWaitList))
			#print("removed a node within the WL")
		else:  #within the waiting list, further down
			tempRCB.set_waitingList(removeNode(currWaitList,p.PID)) #removing that PID within the current wait list

		if(p.parent != None):
			#go into the parent and delete this p.PID
			parentPCB = p.get_parent()
			parentPCB.set_child(removeNode(parentPCB.get_child(), p.PID))
		return
	for child in p.child:
		Kill_tree(RL,child,RCBList)
	Kill_tree(RL, p, RCBList)
	# tempPCB = get_PCB_priority(RL,p)
	# if(tempPCB[0].value.PID == p.PID): #This is the first PCB....
	# 	RL.set_list(tempPCB[1], delHeadNode(tempPCB[0]))
	# 	print("got to remove node:, ",p.PID, "currentPCB: ", tempPCB[0])
	# else:
	# 	print("got to remove node second: ",p.PID)
	# 	removeNode(tempPCB[0], p.PID)
	# return
	'''
	for all children processes q, kill tree Q
	free resources  								#free when you get down to the leaves
	delete PCB and update all pointers
	'''

def destroy(RL,PID, RCBList):
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
		#check in the Wait list
		for RCB in RCBList:
			if (RCB.get_waitingList() != None and findNodeWL(RCB.get_waitingList(), PID)):
				currPCB = getNodeWL(RCB.get_waitingList(), PID)
				#print("this is current pcb: ", getNodeWL(RCB.get_waitingList(), PID).PID)
	#currPCB is the PCB that we want/is currently running
	if(currPCB == None):
		raise Exception("Trying to delete a PCB not in here.")
	#print("this is the current PCB: ", currPCB)
	Kill_tree(RL,currPCB,RCBList)
	scheduler(RL,1)
	'''
	get pointer p to PCB using pid
	Kill_tree(p)
	scheduler()
	'''

	#recursive call that will destroy the root, PID and all the children after


def printLevels(RL):
	print("********************NEW********************")
	currPCB = None
	currentPCB = RL.get_List(2)
	print("Level 2: ")
	while(currentPCB != None):
		print(currentPCB.value.PID, ":{",currentPCB.value.get_type(),"}", sep = '',end = " ")
		currentPCB = currentPCB.next
	print("None")
	print("Level 1: ")
	currentPCB = RL.get_List(1)
	while(currentPCB != None):
		print(currentPCB.value.PID, ":{",currentPCB.value.get_type(),"}",  sep = '',end = " ")
		currentPCB = currentPCB.next
	print("None")
	print("Level 0: ")
	currentPCB = RL.get_List(0)
	while(currentPCB != None):
		print(currentPCB.value.PID, ":{",currentPCB.value.get_type(),"}",  sep = '', end = " ")
		currentPCB = currentPCB.next
	print("None")

def printWaitList(RCBList):
	R1,R2,R3,R4 = RCBList[0],RCBList[1],RCBList[2],RCBList[3]
	ele = R1.get_waitingList()
	print("R1 {currUnits: ", R1.get_currentUnits(),"}")
	while (ele != None):
		print(ele.value[0], "wants : ",ele.value[1],"units", end = " ")
		ele = ele.next
	ele = R2.get_waitingList()
	print("None")
	print("R2 {currUnits: ", R2.get_currentUnits(), "}")
	while (ele != None):
		print(ele.value[0], "wants : ",ele.value[1],"units", end = " ")
		ele = ele.next
	print("None")	
	ele = R3.get_waitingList()
	print("R3 {currUnits: ", R3.get_currentUnits(), "}")
	while (ele != None):
		print(ele.value[0], "wants : ",ele.value[1],"units", end = " ")
		ele = ele.next
	print("None")
	ele = R4.get_waitingList()
	print("R4 {currUnits: ", R4.get_currentUnits(), "}")
	while (ele != None):
		print(ele.value[0], "wants : ",ele.value[1],"units", end = " ")
		ele = ele.next
	print("None")
def scheduler(RL, destroy):
	currRunningProcess, priorityLvl = getCurrentlyRunning(RL)		#this curr running process is a list Node
	# print(currRunningProcess)
	#print(currRunningProcess.value.PID, " this is currenty running")
	highestPriorityProcess, highPrioritylvl = getHighestPcb(RL)
	# print("this is curr running process. value: ", currRunningProcess)
	# print("this is HIGHEST running process. value: ", highestPriorityProcess.value.PID)
	if(destroy == 1 or currRunningProcess.value.get_type() == "Running" or currRunningProcess.value.get_priority() < highestPriorityProcess.value.get_priority()):
		#means that there is a process that got deleted while running, so have to just set thhe highest priority process =  Running
		if(currRunningProcess != 0):
			currRunningProcess.value.set_type("Ready")
			highestPriorityProcess.value.set_type("Running")
		else:
			highestPriorityProcess.value.set_type("Running")	
		output = open("Output.txt","a")
		output.write(highestPriorityProcess.value.get_ID())	
		output.write(" ")
		print("THIS IS HIGHEST priority: ",highestPriorityProcess.value.get_ID(), end = " ")
		output.close()
		#print(highestPriorityProcess.value.get_type())
	'''
	find highest priority process p
	if(self -> priorty < p->priority || self->Status.Type != 'running' || self ==  Nill):
		preempt(p,self) or swap		
	'''

def Time_out(RL):
	currRunningProcess, priorityLvl = getCurrentlyRunning(RL)
	currRunningProcess.value.set_type("Ready")
	RL.set_list(priorityLvl,removeNode(RL.get_List(priorityLvl), currRunningProcess.value.get_ID()))
	RL.set_list(priorityLvl,appendNode(RL.get_List(currRunningProcess.value.get_priority()), currRunningProcess.value))
	RL.get_List(priorityLvl).value.set_type("Running")
	scheduler(RL,0)

def Check_units(RCBList, rid,units):
	RCB = None
	for rcb in RCBList:
		if(rcb.get_RID() == rid):
			RCB = rcb
	if(units > RCB.get_startUnits()):
		return 0 #cannot work
	return 1

def FileCheck(fn):
    try:
      open(fn, "r")
      return 1
    except IOError:
      print ("Error: File does not appear to exist.")
      return 0

def error_Write():
	print("error")
	output = open("Output.txt","a")
	output.write("error")	
	output.write(" ")
	output.close()
if __name__ == '__main__' :
	#resetting all the values within the textfile
	output = open("Output.txt","w")
	output.write("init ")
	output.close()
	RL = ReadyList()
	initPros = PCB("init",0)
	initPros.set_type("Running")
	initPros.set_back_list(RL)
	RL.set_list(0,LN(initPros)) #setting it equal to the very first value. 
	R1 = RCB("R1",1,1) #32
	R2 = RCB("R2",2,2) #33
	R3 = RCB("R3",3,3) #34 
	R4 = RCB("R4",4,4) #35
	RCBList = [R1,R2,R3,R4]
	# create("x",1,RL)
	# create("p",1,RL)
	# create("q",1,RL)
	# create("r",1,RL)
	# Time_out(RL)
	# request("R2",1,RCBList,RL)
	# Time_out(RL)
	# request("R3",3, RCBList, RL)
	# Time_out(RL)
	# request("R4",3, RCBList, RL)
	# Time_out(RL)
	# Time_out(RL)
	# request("R3",1, RCBList, RL)
	# request("R4",2, RCBList, RL)
	# request("R3",2, RCBList, RL)
	# Time_out(RL)
	# destroy(RL, "q", RCBList)
	# Time_out(RL)
	# Time_out(RL)

	#this is to check that the input is correct.
	# fname = input('Enter file name: ') #uncomment this and then go from there
	# while(not FileCheck(fname)):
	# 	fname = input("Enter a real file: ")

	fname = "input.txt"
	file = open(fname,"r")
	for line in file:
		line = line.strip('\n').split()
		print(line)
		if(line == []):
			print('\n')
			output = open("Output.txt","a")
			output.write("\n")
			output.close()
		elif(line[0] == "cr"):
			pid = line[1]
			priority = int(line[2])

			create(pid,priority,RL)

		elif(line[0] == "de"):
			pid = line[1]
			if(pid == "init"):
				error_Write()
			else:	
				destroy(RL, line[1], RCBList)

		elif(line[0] == "rel"):
			rcbID = line[1]
			units = int(line[2])
			if ( not Check_units(RCBList, rcbID,units)):
				error_Write()
			else:
				release(rcbID,units,RCBList, RL)

		elif(line[0] == "req"):
			rcbID = line[1]
			units = int(line[2])
			if ( not Check_units(RCBList, rcbID,units)):
				error_Write()
			else:
				request(rcbID,units, RCBList, RL)
		elif(line[0] == "to"):
			Time_out(RL)
		elif(line[0] == "init"):
			print("got to init:")
			kid = initPros.get_child()
			if(kid == None):
				scheduler(RL,0)
			while(kid != None):
				destroy(RL, kid.value.PID, RCBList)
				kid = kid.next
			printLevels(RL)
			printWaitList(RCBList)
			#destroys everything within the child. 
		else:
			#this is an invalid output
			error_Write()
		printLevels(RL)
		printWaitList(RCBList)

	# 	print(line)


'''
#commands: 
init: will kill everything and "restart the system" you can do this by destroying init and then creating the init process again at lvl 0
cr <name> <priority> :priority is between 1&2, name will only be one char
de <name> this will dstroy the thing in de
req <resource name> <#of units>: reousrce name will be {R1,R2,R3,R4}
rel <resource name> <#of units>: reousrce name will be {R1,R2,R3,R4}
to : timeout, no params but will move that currently running process to the back of the list





IF DESTROY HAVE TO UPDATE THE NUMBER OF UNITS THAT IS ALLOWED NOW.   
'''

