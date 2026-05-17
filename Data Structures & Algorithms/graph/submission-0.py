class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dst not in self.adj_list:
            self.adj_list[dst] = []
        self.adj_list[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        if dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        def dfs(vertex):
            if vertex in visited:
                return False
            if vertex == dst:
                return True
            res = False
            visited.add(vertex)
            for neighbor in self.adj_list[vertex]:
                if dfs(neighbor):
                    res = True
            visited.remove(vertex)
            return res
        return dfs(src)