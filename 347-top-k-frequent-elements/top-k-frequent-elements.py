class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        print(count)

        return [num for num, freq in count.most_common(k)]
        