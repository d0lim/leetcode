class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            solved = True
            for j in range(len(needle)):
                if i + j >= len(haystack):
                    solved = False
                    break
                if haystack[i + j] != needle[j]:
                    solved = False
                    break
            if solved:
                return i
        return -1
