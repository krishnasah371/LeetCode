class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefix_sum = 0
        prefix_freq = defaultdict(int)
        prefix_freq[0] = 1

        for num in nums:
            prefix_sum += num
            count += prefix_freq[prefix_sum - k]
            prefix_freq[prefix_sum] += 1

        return count