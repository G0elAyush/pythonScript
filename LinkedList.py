import math
class LinkedListNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0
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
        if(currentNode == None):
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

        
if __name__=='__main__':
    myList = LinkedList()
    fisrtNode = LinkedListNode(1)
    secondNode = LinkedListNode(2)
    fisrtNode.next = secondNode
    thirdNode = LinkedListNode(3)
    secondNode.next = thirdNode
    fouth = LinkedListNode(4)
    thirdNode.next = fouth
    fifth = LinkedListNode(5)
    fouth.next = fifth
    six = LinkedListNode(6)
    fifth.next = six
    seven = LinkedListNode(7)
    six.next = seven
    eight =LinkedListNode(8)
    seven.next = eight
    nine =LinkedListNode(9)
    eight.next = nine
    nine.next = fifth
    myList.head = fisrtNode
    print(myList.checkIfLoop())
    myList = LinkedList()
    myList.fillList(100)
    myList.makeListCircular()
    myList.getLastNode()
    myList.getLastByMath(100)
    
    
    
    
