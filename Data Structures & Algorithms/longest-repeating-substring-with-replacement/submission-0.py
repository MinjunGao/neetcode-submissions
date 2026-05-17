class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = r = 0
        res = 0
        while r < len(s):
            c = s[r]
            r += 1
            freq[ord(c) - ord('A')] += 1
            while r - l - max(freq) > k:
                d = s[l]
                l += 1
                freq[ord(d) - ord('A')] -= 1
            res = max(res, r - l)
        return res