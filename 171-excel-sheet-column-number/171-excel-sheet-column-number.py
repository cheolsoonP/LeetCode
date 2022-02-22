class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for char, i in zip(s, range(len(s), 0, -1)):
            result += 26 ** (i-1) * (ord(char) - 64)
        return result