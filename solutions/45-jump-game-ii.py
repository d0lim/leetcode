import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        result = [math.inf for _ in range(len(nums))]
        result[0] = 0

        for i, n in enumerate(nums):
            for j in range(1, n + 1):
                if i + j >= len(nums):
                    continue
                result[i + j] = min(result[i + j], result[i] + 1)
        
        return result[-1]
