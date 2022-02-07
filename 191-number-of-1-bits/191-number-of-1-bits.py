class Solution:
    def hammingWeight(self, n: int) -> int:
#         # 1. Hamming distance
#         return bin(n).count('1')
        
        
        # 2. Bit
        count = 0
        while n != 0:
            n &= n - 1
            count += 1
        
        return count
        