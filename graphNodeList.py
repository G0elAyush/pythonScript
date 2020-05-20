from queue import Queue
import heapq
import sys
class Vertex:
    def __init__(self,data):
        self.data=data
        self.adjacent={}
        #set visited flag to use in traversal
        self.visited=False
        #set distance to use in unweightedShortestPath
        self.distance=sys.maxsize
        #set predecessor to use for path
        self.predecessor=None
    def addNeighbor(self,neighbor,cost=0):
        self.adjacent[neighbor]=cost
    def getConnections(self):
        return self.adjacent.keys()
    def __lt__(self,vertex):
        return self.distance < vertex.distance
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
        print(current.data,end=' ')
        for nbr in current.getConnections():
            self.dfs(nbr)
    def bfs(self,vertex):
        q=Queue()
        vertex.visited=True
        q.put(vertex)
        while not q.isEmpty():
            current=q.get()
            print(current.data,end=' ')
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
    def unweightedShortestPath(self,start):
        start.distance=0
        start.predecessor=start
        q=Queue()
        q.put(start)
        while not q.isEmpty():
            current=q.get()
            for nbr in current.getConnections():
                if nbr.distance == sys.maxsize:
                    nbr.distance=current.distance+1
                    nbr.predecessor=current
                    q.put(nbr)
        for vertex in self:
            print("distance from vertex %s to vertex %s via vertex %s is %s" %(start.data,vertex.data,vertex.predecessor.data,vertex.distance))
    def dijkstra(self,start):
        start.distance=0
        start.predecessor=start
        unvisitedQueue=[(v.distance,v) for v in self]
        heapq.heapify(unvisitedQueue)
        while unvisitedQueue:
            uv=heapq.heappop(unvisitedQueue)
            current=uv[1]
            if not current.predecessor:
                current.predecessor=current
            current.visited=True
            for nbr in current.getConnections():
                if not nbr.visited:
                    newDistance=current.distance+current.adjacent[nbr]
                    if newDistance < nbr.distance:
                        nbr.distance=newDistance
                        nbr.predecessor=current
            unvisitedQueue=[(v.distance,v) for v in self if not v.visited]
            heapq.heapify(unvisitedQueue)
        for vertex in self:
            print("distance from vertex %s to vertex %s via vertex %s is %s" %(start.data,vertex.data,vertex.predecessor.data,vertex.distance))
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
    print("total no. of vertices is %s" %G.numVertices)
    print("DFSTraversal", end='  ')
    G.traversal()
    print()
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
    print("total no. of vertices is %s" %G.numVertices)
    print("BFSTraversal",end ='  ')
    G.traversal('bfs')
    print()
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
    G.addEdge('A','G',13)
    print("unweightedShortestPath output")
    G.unweightedShortestPath(G.vertDict['A'])
    G=Graph()
    G.addEdge('A','B',4)
    G.addEdge('A','C',1)
    G.addEdge('C','B',2)
    G.addEdge('C','D',4)
    G.addEdge('B','E',4)
    G.addEdge('D','E',4)
    G.addEdge('F','H',5)
    print("Djikstra algo output")
    G.dijkstra(G.vertDict['A'])


