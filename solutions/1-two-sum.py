class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            remainder = target - num
            if remainder in dic:
                return [dic[remainder], idx]
            dic[num] = idx
