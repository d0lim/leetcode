class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic.setdefault(n, 0)
            dic[n] += 1
        
        length = len(nums)

        for key, value in dic.items():
            if value > length // 2:
                return key
