class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None
class LinkedList:
	def __init__(self,head=None):
		self.head=head
	def printList(self):
		result=[]
		current=self.head
		while current:
			result.append(current.data)
			current=current.next
		#print (result)
		return result
	def listLength(self):
		length=0
		current=self.head
		while current:
			length+=1
			current=current.next
		return length
	def headInsert(self,data):
		node=Node(data)
		if self.head:
			node.next=self.head
		self.head=node
		return
	def tailInsert(self,data):
		node=Node(data)
		if not self.head:
			self.head=node
			return
		else:
			current=self.head
			while current.next:
				current=current.next
			current.next=node
		return
	def posInsert(self,data,pos):
		if pos<0 or pos > self.listLength():
			print ("Invalid position")
			return
		else:
			if pos==0:
				self.headInsert(data)
			else:
				node=Node(data)
				count=1
				current=self.head
				while count < pos:
					current=current.next
					count = count+1
				node.next = current.next
				current.next=node	
				return
	def headDelete(self):
		if self.head:
			self.head=self.head.next
		return
	def tailDelete(self):
		if self.head:
			if not self.head.next:
				self.head=None
				return
			previous = self.head
			current = self.head
			while current.next:
				previous = current
				current = current.next
			previous.next=None
		return
	def posDelete(self,pos):
		length= self.listLength()
		if pos < 0 or pos >= length:
			print ("Invalid Position")
			return
		if pos == 0:
			return self.headDelete()
		if pos == length-1:
			return self.tailDelete()
		count = 0
		current = self.head
		previous = self.head
		while count < pos:
			previous = current
			current = current.next
			count = count + 1
		
		previous.next =current.next
		return
	def lastKthNode(self,k):
		if not self.head or k <= 0:
			return None
		fast = self.head
		slow=None
		count = 1
		while count < k and fast:
			fast=fast.next
			count += 1
		if fast:
			slow = self.head
			while fast.next:
				fast = fast.next
				slow = slow.next
		return slow
	def detectCycle(self):
		fast = self.head
		slow = self.head
		while slow and fast:
			fast = fast.next
			if slow == fast:
				return True
			if not fast:
				return False
			fast = fast.next
			if slow == fast:
				return True
			slow = slow.next
		return False
	def cycleStart(self):
		if not self.head or not self.head.next:
			return None
		slow=self.head.next
		fast = slow.next
		while slow != fast:
			slow = slow.next
			try:
				fast = fast.next.next
			except AttributeError:
				return None
		slow = self.head
		while fast!= slow:
			slow=slow.next
			fast=fast.next
		return slow
	def cycleLength(self):
		if not self.head or not self.head.next:
			return 0
		slow = self.head.next
		fast = slow.next
		while slow != fast:
			slow = slow.next
			try:
				fast = fast.next.next
			except AttributeError:
				return 0
		count = 1
		fast = fast.next
		while slow!=fast:
			fast=fast.next
			count += 1
		return count
			
if __name__=='__main__':
	node0=Node(0)
	node0.next=Node(1)
	list=LinkedList(node0)
	print("linkedList ==> "+ str(list.printList()))
	print("list Length--> " + str(list.listLength()))
	list.headInsert(5)
	print("linkedList after head insert ==> "+ str(list.printList()))
	list.tailInsert(3)
	print("linkedList after tail insert ==> "+ str(list.printList()))
	list.posInsert(4,4)
	print("linkedList after insert at 4==> "+ str(list.printList()))
	list.posInsert(10,-1)
	print("linkedList after insert at -1==> "+ str(list.printList()))
	list.posInsert(6,list.listLength())
	print("linkedList after insert at tail==> "+ str(list.printList()))
	list.posInsert(8,list.listLength()+1)
	print("linkedList after insert at tail + 1==> "+ str(list.printList()))
	list.posInsert(16,0)
	print("linkedList after insert at 0==> "+ str(list.printList()))
	list.posInsert(14,3)
	print("linkedList after insert at 3==> "+ str(list.printList()))
	list.headDelete()
	print("linkedList after headDelete==> "+ str(list.printList()))
	list2=LinkedList()
	list2.headDelete()
	print("blank linkedList after headDelete==> "+ str(list2.printList()))
	list.tailDelete()
	print("linkedList after tailDelete==> "+ str(list.printList()))
	list2.tailDelete()
	print("blank linkedList after tailDelete==> "+ str(list2.printList()))
	list2.headInsert(3)
	print("blank linkedList after head insert ==> "+ str(list2.printList()))
	list2.tailDelete()
	print("only head linkedList after tailDelete==> "+ str(list2.printList()))
	list.posDelete(0)
	print("linkedList after Delete at pos 0==> "+ str(list.printList()))
	list.posDelete(list.listLength())
	print("linkedList after Delete at listLength==> "+ str(list.printList()))
	list.posDelete(list.listLength()-1)
	print("linkedList after Delete at length -1==> "+ str(list.printList()))
	list2.posDelete(0)
	print("blank linkedList after delete at 0==> "+ str(list2.printList()))
	list2.posDelete(10)
	print("blank linkedList after delete at 10==> "+ str(list2.printList()))
	list2.headInsert(3)
	print("blank linkedList after head insert ==> "+ str(list2.printList()))
	list2.posDelete(1)
	print("blank linkedList after delete at 1==> "+ str(list2.printList()))
	list2.posDelete(0)
	print("blank linkedList after delete at 0==> "+ str(list2.printList()))
	list.posDelete(1)
	print("linkedList after Delete at 1==> "+ str(list.printList()))
	node = list.lastKthNode(-1)
	print("last -1 node ==> "+  str(node.data) if node else "last -1 node ==> "+ str(node))
	node = list.lastKthNode(0)
	print("last 0 node ==> "+  str(node.data) if node else "last 0 node ==> "+ str(node))
	node = list.lastKthNode(1)
	print("last 1 node ==> "+  str(node.data) if node else "last 1 node ==> "+ str(node))
	node = list.lastKthNode(2)
	print("last 2 node ==> "+  str(node.data) if node else "last 2 node ==> "+ str(node))
	node = list.lastKthNode(4)
	print("last 4 node ==> "+  str(node.data) if node else "last 4 node ==> "+ str(node))
	nodex =Node(1)
	snake = LinkedList(nodex)
	nodex.next = Node(2)
	nodex.next.next=Node(3)
	nodex.next.next.next=Node(4)
	nodex.next.next.next.next=Node(5)
	nodex.next.next.next.next.next=Node(6)
	nodex.next.next.next.next.next.next=Node(7)
	nodex.next.next.next.next.next.next.next = nodex.next.next
	print("detect loop in snake-->" + str(snake.detectCycle()))
	print("start point of loop in snake-->" + str(snake.cycleStart().data))
	print("length of loop in snake-->" + str(snake.cycleLength()))
	print("detect loop in list-->" + str(list.detectCycle()))
	print("start point of loop in list-->" + str(list.cycleStart()))
	print("length of loop in list-->" + str(list.cycleLength()))
	
	
	