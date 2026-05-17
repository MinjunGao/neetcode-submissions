class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        valid = 0
        slow = fast = 0
        start = end = 0
        length = float('inf')

        while fast < len(s):
            c = s[fast]
            fast += 1
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

            while valid == len(need):
                if fast - slow < length:
                    length = fast - slow
                    start, end = slow, fast
                d = s[slow]
                slow += 1
                window[d] -= 1
                if window[d] == need[d] - 1:
                    valid -= 1
        
        return s[start:end]