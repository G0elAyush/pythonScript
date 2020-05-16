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
        return iter(self.vertDict.values())
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
    def DFSTraversal(self):
        for current in self:
            if not current.visited:
                self.dfs(current)
    def bfs(self,vertex):
        q=Queue()
        q.put(vertex)
        while not q.isEmpty():
            current=q.get()
            print(current.data)
            current.visited=True
            for nbr in current.getConnections():
                if not nbr.visited:
                    q.put(nbr)
    def BFSTraversal(self):
        for vertex in self:
            if not vertex.visited:
                self.bfs(vertex)
if __name__=='__main__':
    G=Graph()
    G.addEdge('A','G',1)
    G.addEdge('A','B',2)
    G.addEdge('A','C',3)
    G.addEdge('B','H',4)
    G.addEdge('D','E',5)
    G.addEdge('D','F',6)
    G.addEdge('B','C',7)
    G.addEdge('F','H',8)
    G.addEdge('E','C',9)
    G.addEdge('G','F',10)
    G.addEdge('H','E',11)
    G.addEdge('G','D',12)
    print(G.numVertices)
    print("DFSTraversal")
    G.DFSTraversal()
    G=Graph()
    G.addEdge('A','G',1)
    G.addEdge('A','B',2)
    G.addEdge('A','C',3)
    G.addEdge('B','H',4)
    G.addEdge('D','E',5)
    G.addEdge('D','F',6)
    G.addEdge('B','C',7)
    G.addEdge('F','H',8)
    G.addEdge('E','C',9)
    G.addEdge('G','F',10)
    G.addEdge('H','E',11)
    G.addEdge('G','D',12)
    print(G.numVertices)
    print("BFSTraversal")
    G.BFSTraversal()
