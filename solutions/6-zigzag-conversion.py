from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_map = defaultdict(list)

        direction = 1
        line = 0
        for c in s:
            zigzag_map[line].append(c)
            
            if direction == 1:
                line += 1
            else:
                line -= 1
            
            if direction == 1 and line == numRows - 1:
                direction = 0
            elif direction == 0 and line == 0:
                direction = 1
            elif numRows == 1:
                direction = 1
                line = 0
        
        result = ''
        for i in range(numRows):
            result += ''.join(zigzag_map[i])
        
        return result
