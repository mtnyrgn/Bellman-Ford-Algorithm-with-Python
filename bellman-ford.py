class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
    def _AddEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def _PrintGraph(self,dist):
        print("Distance:")
        for i in range(self.V):
            print("%d \t\t %d "%(i,dist[i]))
    def BellmanFord(self,src):
        dist=[float("Inf")]*self.V 
        dist[src]=0
        for u,v,w in self.graph:
            if dist[u] != float("Inf") and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
        for u,v,w in self.graph:
             if dist[u] != float("Inf") and dist[u]+w<dist[v]:
                 print("Graph contains negative cycle!!")
                 return
        self.printGraph(dist)
        
vertices=int(input("Enter number of vertices:\n"))
edges=int(input("Enter number of edges:\n"))
g=Graph(vertices)
for i in range(edges):
    u=int(input("Source vertex:\n"))
    v=int(input("Destination vertex:\n"))
    w=int(input("weight of Edge:\n"))
    g.addEdge(u,v,w)
g.BellmanFord(0) 
