class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min = curr_max = max_sum = min_sum = nums[0]
        total = sum(nums)

        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
        

        for num in nums[1:]:
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        if max_sum <0:
            return max_sum
        
        return max(max_sum, total - min_sum)