class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        slow = fast = 0
        valid = 0

        while fast < len(s2):
            c = s2[fast]
            fast += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            if fast - slow == len(s1):
                if valid == len(need):
                    return True
                d = s2[slow]
                slow += 1
                if d in window:
                    window[d] -= 1
                    if window[d] == need[d] - 1:
                        valid -= 1
        
        return False
            