class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = self.buildGraph(edges)
        self.on_path = set()
        self.visited = set()
        self.has_cycle = False
        self.path = []

        for v in range(n):
            self.traverse(v, graph)
        
        if self.has_cycle:
            return []
        
        return list(reversed(self.path))
    
    def buildGraph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            vertex_from, vertex_to = edge
            graph[vertex_from].append(vertex_to)
        return graph
    
    def traverse(self, v, graph):
        if v in self.on_path:
            self.has_cycle = True
            return
        if v in self.visited:
            return
        
        self.visited.add(v)
        self.on_path.add(v)
        for vertex_to in graph[v]:
            self.traverse(vertex_to, graph)
        self.on_path.remove(v)
        self.path.append(v)