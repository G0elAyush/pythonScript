import math
class LinkedListNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,head=None):
        self.head=head
        self.length=0
    def printSingleNodeList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next
    def insertAtStart(self,data):
        newNode = LinkedListNode(data)
        if self.head is not None:
            newNode.next = self.head
        self.head = newNode
        return
			
    def checkIfLoop(self):
        nodeTravesed = set()
        currentNode= self.head
        while currentNode:
            if currentNode in nodeTravesed:
                return True
            nodeTravesed.add(currentNode)                
            currentNode = currentNode.next
        return False
    def insertAtEnd(self,data):
        newNode = LinkedListNode(data)
        count=1
        currentNode = self.head
        if currentNode is None:
            self.head = newNode
            self.length =count
            return
        while(currentNode.next):
            count += 1
            currentNode = currentNode.next
            
        currentNode.next = newNode
        count += 1
        self.length = count
        return
        
    def fillList(self,n):
        for i in range(1,n+1):
            self.insertAtEnd(i)
        return
    def makeListCircular(self):
        currentNode = self.head
        if(currentNode == None):
            return
        while(currentNode.next):
            currentNode = currentNode.next
        currentNode.next = self.head
    def getLastNode(self):
        currentNode = self.head
        while(self.length> 1):
            nodeToDelete = currentNode.next
            currentNode.next = nodeToDelete.next
            currentNode = currentNode.next
            self.length -=1
        print(currentNode.data)
    def getLastByMath(self,n):
        print((2*n)-(2**(math.floor(math.log2(n)) +1 ))+1)
    def reverseList(self):
        last = None
        current = self.head
        count = 0
        while current:
            count = count +1
            nextNode = current.next
            current.next = last
            last = current
            current = nextNode
        self.head = last
        return count
    def addList(self,list1,list2):
        length1 = list1.reverseList()
        length2 = list2.reverseList()
        count = 0
        d = length1 if (length1 - length2) < 0 else length2
        head1 = list1.head
        head2 = list2.head
        carry = 0
        temp1 = temp = LinkedListNode(-1)
        while count < d:
            sum = head1.data + head2.data + carry
            carry = sum // 10
            sum = sum % 10
            temp.next = LinkedListNode(sum)
            temp = temp.next
            head1 = head1.next
            head2 = head2.next
            count = count +1
        while head1:
            sum = carry  + head1.data
            carry = sum // 10
            sum = sum % 10
            temp.next = LinkedListNode(sum)
            temp = temp.next
            head1 = head1.next
        while head2:
            sum = carry  + head2.data
            carry = sum // 10
            sum = sum % 10
            temp.next = LinkedListNode(sum)
            temp = temp.next
            head1 = head2.next
        #print(carry)
        while carry :
            temp.next = LinkedListNode(carry % 10)
            carry = carry // 10

        self.head = temp1.next
        self.reverseList()
if __name__=='__main__':
    myList = LinkedList()
    myList1 = LinkedList()
    fisrtNode = LinkedListNode(9)
    secondNode = LinkedListNode(9)
    fisrtNode.next = secondNode
    thirdNode = LinkedListNode(9)
    secondNode.next = thirdNode
    fouth = LinkedListNode(9)
    thirdNode.next = fouth
    fifth = LinkedListNode(9)
    fouth.next = fifth
    six = LinkedListNode(9)
    fifth.next = six
    seven = LinkedListNode(9)
    #six.next = seven
    eight =LinkedListNode(9)
    seven.next = eight
    nine =LinkedListNode(9)
    eight.next = nine
    myList1.head = fisrtNode
    myList2 = LinkedList()
    fisrtNode = LinkedListNode(9)
    secondNode = LinkedListNode(9)
    fisrtNode.next = secondNode
    thirdNode = LinkedListNode(9)
    secondNode.next = thirdNode
    fouth = LinkedListNode(9)
    thirdNode.next = fouth
    fifth = LinkedListNode(9)
    fouth.next = fifth
    six = LinkedListNode(9)
    fifth.next = six
    myList2.head = fisrtNode
    myList1.printSingleNodeList()
    print('list chnage')
    myList2.printSingleNodeList()
    print('list as above')
    myList3 = LinkedList()
    myList3.addList(myList1,myList2)
    myList3.printSingleNodeList()
    print("done prog 1")
    #myList.printSingleNodeList()
    #listLength = myList.reverseList()
    #print (listLength)
    #print("ayush")
    #myList.printSingleNodeList()
    #print("goel")
##    nine.next = fifth
##    myList.head = fisrtNode
##    print(myList.checkIfLoop())
##    myList = LinkedList()
##    myList.fillList(100)
##    myList.makeListCircular()
##    myList.getLastNode()
##    myList.getLastByMath(100)
##    fisrtNode = LinkedListNode(0  )
##    myList = LinkedList(fisrtNode)
##    myList.fillList(50)
##    myList.printSingleNodeList()
##    print("ayush")
##    myList = LinkedList()
##    myList.insertAtStart(0)
##    myList.printSingleNodeList()
##    print("ayush")
##    fisrtNode = LinkedListNode(0)
##    myList = LinkedList(fisrtNode)
##    myList.insertAtStart(1)
##    myList.printSingleNodeList()
    
    
    
    
    
