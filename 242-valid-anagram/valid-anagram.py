class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count = Counter(s)
        t_count = Counter(t)

        if len(s) != len(t):
            return False
        
        for key, val in s_count.items():
            if t_count[key] != val:
                return False
        return True

        
