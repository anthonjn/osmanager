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
    def getVal(self):
    	return self.value

def delHeadNode(ll):
	ll = ll.next

ln = LN(3)
ln.next = LN(5)
ln.next.next = LN(8)
ln.next.next = LN(ln.getVal())
delHeadNode(ln)


for ele in ln:
	print(ele)

def retTwo(a):
	return a, 2*a

l = retTwo(5)
print(l[0], " ", l[1])