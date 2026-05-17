class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stk = []
        for c in s:
            if c in mp:
                if not stk or stk[-1] != mp[c]:
                    return False
                else:
                    stk.pop()
            else:
                stk.append(c)
    
        return not stk