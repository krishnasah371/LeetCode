class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ["a", "e", "i", "o", "u"]
        char = list(s)
        print(char)

        left = 0
        right = len(char) - 1

        while left < right:
            if char[left].lower() in vowels and char[right].lower() in vowels:
                char[left], char[right] = char[right], char[left]
                left += 1
                right -= 1
            elif char[left].lower() not in vowels:
                left += 1
            elif char[right].lower() not in vowels:
                right -= 1
        return ''.join(char)

        