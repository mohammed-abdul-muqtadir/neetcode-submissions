class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta = []
        for i in tokens:
            if i == '+':
                a = sta.pop()
                b = sta.pop()
                sta.append(a+b)
            elif i == "-":
                a = sta.pop()
                b = sta.pop()
                sta.append(b-a)
            elif i == "*":
                a = sta.pop()
                b = sta.pop()
                sta.append(a*b)
            elif i == "/":
                a = sta.pop()
                b = sta.pop()
                sta.append(int(b/a))
            else:
                sta.append(int(i))
        
        return sta[0]

