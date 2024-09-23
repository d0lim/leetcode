from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i, n in enumerate(numbers):
            dic[n] = i
        
        for i, n in enumerate(numbers):
            if dic[target - n] > 0:
                return [i + 1, dic[target - n] + 1]
