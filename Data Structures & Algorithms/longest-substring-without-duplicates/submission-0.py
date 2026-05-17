class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        slow = fast = 0
        window = set()
        res = 0

        while fast < len(s):
            c = s[fast]
            fast += 1
            while c in window:
                d = s[slow]
                slow += 1
                window.remove(d)
            window.add(c)
            res = max(res, len(window))
        
        return res