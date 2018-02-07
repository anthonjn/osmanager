#class List Node, is used for all the other things including PCB, ect. 
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


'''
if we had something like 4->5->3
and call delHeadNode(4), would result in 5->3
'''
def delHeadNode(ll):
	ll = ll.next
	return ll

#setter methods for a linked list. 
def appendNode(ll,nextValue):
	if ll == None:
		return LN(nextValue)
	else:
		ll.next = appendNode(ll.next,nextValue)
		return ll

def findNode(ll, PID):
	curr = ll
	prev = None
	while curr:
		#print("this is curr:",curr.value.PID)
		if curr.value.PID == PID:
			return True
		curr = curr.next
	return False

def findNodeWL(ll, PID):
	curr = ll
	prev = None
	#print("this is curr: ", curr.value)
	while curr:
		#print("this is curr:",curr.value.PID)
		if curr.value[0].PID == PID:
			return True
		curr = curr.next
	return False

def getNode(ll, PID):
	curr = ll
	prev = None
	while curr:
		if curr.value.PID == PID:
			return curr.value
		curr = curr.next
	return None

def getNodeWL(ll, PID):
	curr = ll
	prev = None
	while curr:
		if curr.value[0].PID == PID:
			return curr.value[0]
		curr = curr.next
	return None

def getNodeLN(ll, PID): #this returns the LN version of the right PID
	curr = ll
	prev = None
	while curr:
		if curr.value.PID == PID:
			return curr
		curr = curr.next
	return None

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

def removeNodeWaitingList(ll, data: "tuple"):
	if(ll is None):
		raise Excption("trying to delete from a empty linked list")
	prev = None
	curr = ll
	if(curr is not None):
		if (curr.value == data):
			return delHeadNode(ll)
	while curr:
		if(curr.value == data):
			break
		prev = curr
		curr = curr.next
	if(curr == None):
		return ll 
	prev.next = curr.next
	del curr
	return ll
'''
Example of how to use the Linked List...
remember to set LinkedList = delHeadNode for it to work.

LinkedList = LN(4)
appendNode(LinkedList,7)
appendNode(LinkedList,9)
appendNode(LinkedList,79)
appendNode(LinkedList,76)
LinkedList = delHeadNode(LinkedList)
for v in LinkedList:
	print(v)
'''