class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        res = ""
        lst = self.store[key]
        l, r = 0, len(lst) - 1
        while l <= r:
            m = (l + r) // 2
            if lst[m][1] <= timestamp:
                res = lst[m][0]
                l = m + 1
            elif lst[m][1] > timestamp:
                r = m - 1
        return res
