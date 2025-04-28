class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict:
                return [dict[complement], i]
            
            dict[nums[i]] = i
        