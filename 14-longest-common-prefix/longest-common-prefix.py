class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #find minimum length of the string

        min_len = len(strs[0])
        prefix = ""

        for word in strs:
            if len(word) < min_len:
                min_len = len(word)

        for i in range(min_len):
            char_to_match = strs[0][i]

            for word in strs:
                if word[i] != char_to_match:
                    break
            else:
                prefix += char_to_match
                continue
            break
        return prefix
