class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for n in nums2:
            i = nums1.index(0)
            nums1[i] = n
        nums1.sort()
