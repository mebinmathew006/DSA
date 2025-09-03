class Graph:
    def __init__(self):
        self.graph={}
    
    def add_vertex(self,vertex):
        self.graph[vertex]=[]
    
    def add_edge(self,vertex,edge,isBi):
        if not vertex in self.graph :
            self.add_vertex(vertex)
        if not edge in self.graph:
            self.add_vertex(edge)
            
        self.graph[vertex].append(edge)
        
        if isBi:
            self.graph[edge].append(vertex)
            
    def print_graph(self):
        for v,e in self.graph.items():
            print(str(v)+'->'+ str(e), end=' ')
            
    def bfs(self,start):
        visited=set()
        queue=[start]
        
        while queue:
            node=queue.pop(0)
            if node not in visited:
                print(node,end=' ')
                visited.add(node)
                queue.extend(self.graph[node])
                
    def dfs(self,node,vistied=None):
        if vistied==None:
            vistied=set()
        if node not in vistied:
            print(node, end=' ')
            vistied.add(node)   
            for neighbour in self.graph[node]:
                self.dfs(neighbour,vistied)
        
gr=Graph()        

gr.add_edge(10,2,True)
gr.add_edge(2,25,False)
gr.add_edge(15,52,True)
gr.add_edge(18,32,False)
gr.add_edge(85,27,True)
gr.print_graph()
print()

gr.bfs(10)
print()

gr.dfs(10)