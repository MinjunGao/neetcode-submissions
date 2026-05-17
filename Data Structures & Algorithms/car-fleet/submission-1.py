class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stk = []
        for p, s in pair:
            if not stk or stk[-1] < (target - p) / s:
                stk.append((target - p) / s)
        return len(stk)