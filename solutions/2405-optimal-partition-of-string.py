class Solution:
    def partitionString(self, s: str) -> int:
        tmp = []
        count = 1
        for c in s:
            if c not in tmp:
                tmp.append(c)
            else:
                count += 1
                tmp = [c]
        return count
