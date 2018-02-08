# # class LN:
# #     def __init__(self : "LN", value : object, nxt : "LN" = None):
# #         self.value = value
# #         self.next  = nxt
# #     '''
# #     this is used for something like:
# #     for v in ll:
# #     	print(v)
# #     this will print things from the beginning to the end of the linked list
# #     '''
# #     def __iter__(self):
# #     	curr = self
# #     	while curr != None:
# #     		yield curr.value
# #     		curr = curr.next
# #     def getVal(self):
# #     	return self.value

# # def delHeadNode(ll):
# # 	ll = ll.next

# # ln = LN(3)
# # ln.next = LN(5)
# # ln.next.next = LN(8)
# # ln.next.next = LN(ln.getVal())
# # delHeadNode(ln)


# # for ele in ln:
# # 	print(ele)

# # def retTwo(a):
# # 	return a, 2*a

# # l = retTwo(5)
# # print(l[0], " ", l[1])

# from collections import defaultdict

# def LRS(array, index, key):
#     if(index<0):
#         return -1
#     if(array[index] == key):
#         return index
#     return LRS(array,index-1,key)
# li = [-3,9,8,1,5]
# x = LRS(li,4,8)
# print(x)


# defa = defaultdict(int)
# if(defa["hello"]):
# 	pirnt('ok') 
# defa["be"] +=1
# for k,v in defa.items():
# 	print(k, " ", v)


# # def a(b):
# # 	return b,b

# # z = a(5)
# # l, m = z[0], z[1]
# # print(l,m)



# # Request: the first part
# # use this to debug, not totally sure how the second part works, but this works for adding things

# # 	rl = ReadyList()
# # 	pb = LN(PCB(4,2))
# # 	pb.value.set_type("Running")
# # 	appendNode(pb,PCB(6,2))
# # 	rl.set_list(2,pb)

# # 	r1 = RCB(1532,20,20)
# # 	r2 = RCB(1533,20,20)
# # 	r3 = RCB(1534,20,20)
# # 	r4 = RCB(1535,20,20)
# # 	RCBList = [r1,r2,r3,r3]

# # 	request(1532,2,RCBList, rl)

# # 	for k,v in pb.value.get_other_resources().items():
# # 		print("key: ", k, " value: ", v)
# # 			#use this to look at the waiting list, and see what's inside the list
# # 	for ele in r1.waiting_list:
# # 		print("ele: ",ele.value.PID)


# # #the test for multiple running programs that are put on the waiting list, after they are running


# # 	rl = ReadyList()
# # 	pb = LN(PCB(4,2))
# # 	pb.value.set_type("Running")
# # 	appendNode(pb,PCB(6,2))
# # 	rl.set_list(2,pb)

# # 	r1 = RCB(1532,20,20)
# # 	r2 = RCB(1533,20,20)
# # 	r3 = RCB(1534,20,20)
# # 	r4 = RCB(1535,20,20)
# # 	RCBList = [r1,r2,r3,r3]

# # 	request(1532,200,RCBList, rl)

# # 	pb2 = LN(PCB(6,2))
# # 	pb2.value.set_type("Running")
# # 	appendNode(pb,PCB(7,2))
# # 	rl.set_list(2,pb2)

# # 	request(1532,200,RCBList, rl)
# # 	for k,v in pb.value.get_other_resources().items():
# # 		print("key: ", k, " value: ", v)

# 	# for ele in r1.waiting_list:
# 	# 	print("ele: ",ele[0].value.PID)


# 	rl = ReadyList()
# 	pb = LN(PCB(4,2))
# 	pb.value.set_type("Running")
# 	appendNode(pb,PCB(6,2))
# 	rl.set_list(2,pb)

# 	r1 = RCB(1532,20,20)
# 	r2 = RCB(1533,20,20)
# 	r3 = RCB(1534,20,20)
# 	r4 = RCB(1535,20,20)
# 	RCBList = [r1,r2,r3,r3]
# 	#printLevels(rl)
# 	request(1532,2,RCBList, rl)

# 	pb2 = LN(PCB(9,2))
# 	pb2.value.set_type("Running")
# 	appendNode(pb2,PCB(7,2))
# 	rl.set_list(2,pb2)
# 	appendNode(rl.get_List(2),PCB(90,2)) #this is how you append things to the back of the RL.

# 	#printLevels(rl)
# 	request(1532,19,RCBList, rl)
# 	# for k,v in pb.value.get_other_resources().items():
# 	# 	print("key: ", k, " value: ", v)


# 	# #release(1532,2,RCBList,rl)
# 	# for ele in r1.waiting_list:
# 	# 	print("ele: ",ele[0].value.PID)

# 	# for ele in r1.waiting_list:
# 	# 	print("ele2: ",ele)



# 	pb3 = LN(PCB(10,2))
# 	pb3.value.set_type("Running")
# 	appendNode(pb3,PCB(11,2))
# 	rl.set_list(2,pb3)
# 	print("before the end: ")
# 	printLevels(rl)
# 	release(1532,2,RCBList,rl)
# 	print("after")
# 	printLevels(rl)


# 	Time_out(RL)
# 	destroy(RL,"z",RCBList)
# 	printLevels(RL)
# 	create("a",2,RL)
# 	create("B",2,RL)
# 	create("C",2,RL)

# 	request(1532,19,RCBList, RL)
# 	request(1533,22,RCBList, RL)
# 	print("R1 TOTAL UNITS AFTER: ",R1.get_currentUnits())
# 	printWaitList(RCBList)
# 	destroy(RL, "a",RCBList)
# 	print("AFTER")
# 	print("R1 TOTAL UNITS AFTER: ",R1.get_currentUnits())
# 	printWaitList(RCBList)
# 	printLevels(RL)





# 	RL = ReadyList()
# 	initPros = PCB("init",0)
# 	initPros.set_type("Running")
# 	initPros.set_back_list(RL)
# 	RL.set_list(0,LN(initPros)) #setting it equal to the very first value. 
# 	printLevels(RL)
# 	create("z",2,RL)
# 	# currRunningProcess, priorityLvl = getCurrentlyRunning(RL)
# 	# print("this is curr running: ",currRunningProcess.value.PID)
# 	R1 = RCB(1532,20,20)
# 	R2 = RCB(1533,20,20)
# 	R3 = RCB(1534,20,20)
# 	R4 = RCB(1535,20,20)
# 	RCBList = [R1,R2,R3,R4]
# 	print("BEFORE")
# 	printLevels(RL)
# 	request(1532,19,RCBList, RL)
# 	print("DURING")

# 	printLevels(RL)
# 	request(1532,5,RCBList, RL)
# 	printWaitList(RCBList)
# 	print("AFTER")
# 	printLevels(RL)
# 	printWaitList(RCBList)
# 	destroy(RL,"z",RCBList)
# 	printLevels(RL)
# 	printWaitList(RCBList)
from PCB import *
class LN:
    def __init__(self : "LN", value : object, nxt : "LN" = None):
        self.value = value
        self.next  = nxt
    '''
    this is used for something like:
    for v in ll:
    	print(v)
    this will print things from the beginning to the end of the linked list
    '''
    def __iter__(self):
    	curr = self
    	while curr != None:
    		yield curr.value
    		curr = curr.next

def removeNode(ll, PID):
	if(ll is None):
		raise Excption("trying to delete from a empty linked list")
	prev = None
	curr = ll
	if(curr is not None):
		if (curr.value.PID == PID):
			return delHeadNode(ll)
	while curr:
		if(curr.value.PID == PID):
			break
		prev = curr
		curr = curr.next
	if(curr == None):
		return ll 
	prev.next = curr.next
	del curr
	return ll


A = LN(PCB(5,2))
print(removeNode(A,5))


##FIRST SAMPLE TEST CASE
create("x",2,RL)
	create("y",1,RL)
	Time_out(RL)
	create("z",2,RL)
	Time_out(RL)
	request(1532,1,RCBList,RL)
	Time_out(RL)
	request(1532,1,RCBList,RL)
	destroy(RL, "z", RCBList)
	release(1532,1,RCBList, RL)
	destroy(RL,"x", RCBList)

#seoncd example test case
	create("x",1,RL)
	create("p",1,RL)
	create("q",1,RL)
	create("r",1,RL)
	Time_out(RL)
	request(1533,1,RCBList,RL)
	Time_out(RL)
	request(1534,3, RCBList, RL)
	Time_out(RL)
	request(1535,3, RCBList, RL)
	Time_out(RL)
	Time_out(RL)
	request(1534,1, RCBList, RL)
	request(1535,2, RCBList, RL)
	request(1533,2, RCBList, RL)
	Time_out(RL)
	destroy(RL, "q", RCBList)
	Time_out(RL)
	Time_out(RL)