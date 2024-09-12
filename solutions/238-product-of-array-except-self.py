class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        count_zero = 0
        
        for n in nums:
            if n == 0:
                count_zero += 1
                continue
            else:
                total_product *= n

        result = [0 for _ in range(len(nums))]

        for i, n in enumerate(nums):
            if count_zero == len(nums):
                result[i] = 0
            elif n == 0:
                if count_zero > 1:
                    result[i] = 0
                else:
                    result[i] = total_product
            else:
                result[i] = total_product // n if count_zero == 0 else 0

        return result
