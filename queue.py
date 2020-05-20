class Queue:
    def __init__(self):
        self.queue=[]
        self.length=0
    def __str__(self):
        return str(self.queue)
    def put(self,data):
        self.queue.append(data)
        self.length+=1
    def get(self):        
        if self.length > 0:
            self.length-=1
            return self.queue.pop(0)
    def isEmpty(self):
        if self.length<1:
            return True
        return False
if __name__ =='__main__':
    q=Queue()
    print(q)
    q.put(3)
    q.put(5)
    print(q.get())
    q.put(2)
    print(q.get())
    print(q.isEmpty())
    print(q.get())
    print(q.isEmpty())
    print(q.get())

