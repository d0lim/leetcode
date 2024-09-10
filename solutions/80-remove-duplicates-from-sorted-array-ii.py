class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        occurrence = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                occurrence += 1
            else:
                occurrence = 1
            
            if occurrence <= 2:
                nums[k] = nums[i]
                k += 1
        
        return k
