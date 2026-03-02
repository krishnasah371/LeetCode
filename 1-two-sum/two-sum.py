class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[compliment], i]

    

       
             

        