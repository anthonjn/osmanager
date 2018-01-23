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