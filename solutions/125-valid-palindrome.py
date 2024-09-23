class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = list(filter(lambda c: self.isAlphanumeric(c), s.lower()))

        result = True
        for i in range(len(filtered) // 2):
            if filtered[i] != filtered[-1 - i]:
                result = False
                break

        return result
    
    def isAlphanumeric(self, c: str) -> bool:
        if 'a' <= c <= 'z':
            return True
        elif 'A' <= c <= 'Z': 
            return True
        elif '0' <= c <= '9':
            return True
        else:
            return False
