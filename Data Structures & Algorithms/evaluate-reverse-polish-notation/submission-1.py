class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stk = []
        for t in tokens:
            if t not in '+-*/':
                stk.append(t)
            else:
                n2, n1 = int(stk.pop()), int(stk.pop())
                num = 0
                if t == '+':
                    num = n1 + n2
                elif t == '-':
                    num = n1 - n2
                elif t == '*':
                    num = n1 * n2
                elif t == '/':
                    num = int(n1 / n2)
                stk.append(num)
        return stk[0]