class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True

        for i, n in enumerate(nums):
            if n == 0:
                flag = False
                for j in range(i):
                    if j + nums[j] > i or j + nums[j] >= length - 1:
                        flag = True
                        break
                if not flag:
                    return False
        return True
