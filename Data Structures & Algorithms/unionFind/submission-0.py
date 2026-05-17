class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p, q = self.find(x), self.find(y)
        if p == q:
            return False
        if self.size[p] > self.size[q]:
            self.parent[q] = p
            self.size[p] += self.size[q]
        elif self.size[q] < self.size[p]:
            self.parent[p] = q
            self.size[q] += self.size[p]
        else:
            self.parent[q] = p
            self.size[p] += self.size[q]
        self.count -= 1
        return True

    def getNumComponents(self) -> int:
        return self.count
