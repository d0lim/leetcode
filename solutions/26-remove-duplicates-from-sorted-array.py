class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        tmp = nums[0]
        for i, n in enumerate(nums):
            if n != tmp:
                tmp = n
                nums[k + 1] = n
                k += 1

        return k + 1

