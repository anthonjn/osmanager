# class LN:
#     def __init__(self : "LN", value : object, nxt : "LN" = None):
#         self.value = value
#         self.next  = nxt
#     '''
#     this is used for something like:
#     for v in ll:
#     	print(v)
#     this will print things from the beginning to the end of the linked list
#     '''
#     def __iter__(self):
#     	curr = self
#     	while curr != None:
#     		yield curr.value
#     		curr = curr.next
#     def getVal(self):
#     	return self.value

# def delHeadNode(ll):
# 	ll = ll.next

# ln = LN(3)
# ln.next = LN(5)
# ln.next.next = LN(8)
# ln.next.next = LN(ln.getVal())
# delHeadNode(ln)


# for ele in ln:
# 	print(ele)

# def retTwo(a):
# 	return a, 2*a

# l = retTwo(5)
# print(l[0], " ", l[1])

from collections import defaultdict

def LRS(array, index, key):
    if(index<0):
        return -1
    if(array[index] == key):
        return index
    return LRS(array,index-1,key)
li = [-3,9,8,1,5]
x = LRS(li,4,8)
print(x)


defa = defaultdict(int)
if(defa["hello"]):
	pirnt('ok') 
defa["be"] +=1
for k,v in defa.items():
	print(k, " ", v)


# def a(b):
# 	return b,b

# z = a(5)
# l, m = z[0], z[1]
# print(l,m)



# Request: the first part
# use this to debug, not totally sure how the second part works, but this works for adding things

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

# 	request(1532,2,RCBList, rl)

# 	for k,v in pb.value.get_other_resources().items():
# 		print("key: ", k, " value: ", v)
# 			#use this to look at the waiting list, and see what's inside the list
# 	for ele in r1.waiting_list:
# 		print("ele: ",ele.value.PID)


# #the test for multiple running programs that are put on the waiting list, after they are running


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

# 	request(1532,200,RCBList, rl)

# 	pb2 = LN(PCB(6,2))
# 	pb2.value.set_type("Running")
# 	appendNode(pb,PCB(7,2))
# 	rl.set_list(2,pb2)

# 	request(1532,200,RCBList, rl)
# 	for k,v in pb.value.get_other_resources().items():
# 		print("key: ", k, " value: ", v)

	# for ele in r1.waiting_list:
	# 	print("ele: ",ele[0].value.PID)