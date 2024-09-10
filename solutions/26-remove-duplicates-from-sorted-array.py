class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        new = True
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                new = False
            else:
                new = True
            
            if new:
                nums[k] = nums[i]
                k += 1

        return k

