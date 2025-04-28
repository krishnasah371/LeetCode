class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        max_sum = -math.inf

        for i in range(k):
            curr_sum += nums[i]

        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i-k]
            print(curr_sum)
            max_sum = max(max_sum, curr_sum)
            print(max_sum)
        return max_sum/k
        