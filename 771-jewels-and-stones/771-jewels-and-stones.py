class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         ## 1. 해시테이블
#         freqs = {}
#         count = 0
        
#         # Stone
#         for char in stones:
#             if char not in freqs:
#                 freqs[char] = 1
#             else:
#                 freqs[char] += 1
        
#         # Jewely
#         for char in jewels:
#             if char in freqs:
#                 count += freqs[char]
            
#         return count

#         ## 2. defaultdict
#         freqs = collections.defaultdict(int)
#         count = 0
        
#         for char in stones:
#             freqs[char] += 1
            
#         for char in jewels:
#             count += freqs[char]
            
#         return count

#         ## 3. Counter
#         freqs = collections.Counter(stones)
#         count = 0
        
#         for char in jewels:
#             count += freqs[char]
            
#         return count


        ## 4. simple
        return sum(s in jewels for s in stones)
        
        