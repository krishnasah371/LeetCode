class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_list = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrams_list[key].append(word)
        return list(anagrams_list.values())
            
