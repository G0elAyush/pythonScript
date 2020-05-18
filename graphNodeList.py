from queue import Queue
class Vertex:
    def __init__(self,data):
        self.data=data
        self.adjacent={}
        self.visited=False
    def addNeighbor(self,neighbor,cost=0):
        self.adjacent[neighbor]=cost
    def getConnections(self):
        return self.adjacent.keys()
class Graph:
    def __init__(self):
        self.vertDict={}
        self.numVertices=0
    def __iter__(self):
        keys=sorted(self.vertDict.keys())
        return iter([self.vertDict.get(key) for key in keys])
    def addVertex(self,data):
        newVertex=Vertex(data)
        self.numVertices+=1
        self.vertDict[data]=newVertex
    def addEdge(self,frm,to,cost=0):
        if frm not in self.vertDict:
            self.addVertex(frm)
        if to not in self.vertDict:
            self.addVertex(to)
        self.vertDict[frm].addNeighbor(self.vertDict[to],cost)
    def dfs(self,current):
        if current.visited:
            return
        current.visited=True
        print(current.data)
        for nbr in current.getConnections():
            self.dfs(nbr)
    def bfs(self,vertex):
        q=Queue()
        vertex.visited=True
        q.put(vertex)
        while not q.isEmpty():
            current=q.get()
            print(current.data)
            for nbr in current.getConnections():
                if not nbr.visited:
                    nbr.visited=True
                    q.put(nbr)
    def traversal(self,mode='dfs'):
        for vertex in self:
            if not vertex.visited:
                if mode=='bfs':
                    self.bfs(vertex)
                elif mode=='dfs':
                    self.dfs(vertex)
                else:
                    print("%s is not a valid traversal. only 'dfs' or 'bfs' are valid." %mode)

if __name__=='__main__':
    G=Graph()
    G.addEdge('A','B',1)
    G.addEdge('A','C',2)
    G.addEdge('A','D',3)
    G.addEdge('B','F',4)
    G.addEdge('B','E',5)
    G.addEdge('F','J',6)
    G.addEdge('E','H',7)
    G.addEdge('C','E',8)
    G.addEdge('D','G',9)
    G.addEdge('G','H',10)
    G.addEdge('G','I',11)
    G.addEdge('D','K',12)
    print(G.numVertices)
    print("DFSTraversal")
    G.traversal()
    G=Graph()
    G.addEdge('A','B',1)
    G.addEdge('A','C',2)
    G.addEdge('A','D',3)
    G.addEdge('B','F',4)
    G.addEdge('B','E',5)
    G.addEdge('F','J',6)
    G.addEdge('E','H',7)
    G.addEdge('C','E',8)
    G.addEdge('D','G',9)
    G.addEdge('G','H',10)
    G.addEdge('G','I',11)
    G.addEdge('D','K',12)
    print("BFSTraversal")
    G.traversal('bfs')
