class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = self.buildGraph(edges)
        indegrees = [0] * n
        for edge in edges:
            vertex_from, vertex_to = edge
            indegrees[vertex_to] += 1
        q = deque()
        for v, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(v)
        
        self.path = []

        while q:
            v = q.popleft()
            self.path.append(v)
            for vertex_to in graph[v]:
                indegrees[vertex_to] -= 1
                if indegrees[vertex_to] == 0:
                    q.append(vertex_to)
        
        return self.path if len(self.path) == n else []

    def buildGraph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            vertex_from, vertex_to = edge
            graph[vertex_from].append(vertex_to)
        return graph