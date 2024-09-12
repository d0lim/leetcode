from collections import deque

class Solution:
    def romanToInt(self, s: str) -> int:
        stack = deque()

        """
        III -> I I I

        1 + 1 + 1

        LVIII -> I I I V L

        1 + 1 + 1 + 5 + 50

        MCMXCIV 
        -> M C M / 1000 -100 + 1000
        -> X C / -10 + 100 
        -> I V /  -1 + 5
        """

        result = 0
        for c in list(s):
            if len(stack) == 0:
                stack.appendleft(c)
            else:
                if self.needSubtraction(stack[0], c):
                    result = result - self.convert(stack.popleft()) + self.convert(c)
                else:
                    stack.appendleft(c)
        
        while len(stack) > 0:
            result += self.convert(stack.popleft())
        
        return result
                        
    def convert(self, r: str) -> int:
        if r == 'I':
            return 1
        elif r == 'V':
            return 5
        elif r == 'X':
            return 10
        elif r == 'L':
            return 50
        elif r == 'C':
            return 100
        elif r == 'D':
            return 500
        elif r == 'M':
            return 1000
        else:
            raise Exception('Wrong roman')

    def needSubtraction(self, a: str, b: str) -> bool:
        if a == 'I':
            if b == 'V' or b == 'X':
                return True
        if a == 'X':
            if b == 'L' or b == 'C':
                return True
        if a == 'C':
            if b == 'D' or b == 'M':
                return True
        
        return False

    
