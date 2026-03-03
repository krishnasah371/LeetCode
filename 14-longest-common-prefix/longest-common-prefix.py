class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #find minimum length of the string

        minimum_length = len(strs[0])
        prefix = ""

        for word in strs:
            if len(word) < minimum_length:
                minimum_length = len(word)

        for i in range(minimum_length):
            char_to_match = strs[0][i]

            for word in strs:
                if word[i] != char_to_match:
                    break
            else:
                prefix += char_to_match
                continue
            break
        return prefix
                