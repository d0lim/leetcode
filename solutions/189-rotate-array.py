class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copied = [n for n in nums]
        length = len(copied)
        
        for i in range(length):
            nums[i] = copied[(i - k) % length]
