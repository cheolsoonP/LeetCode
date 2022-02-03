class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # 1 brute force
        result: Set = set()
            
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
                    
        return result
    
#         # 2. binary
#         result: Set = set()
#         nums2.sort()
        
#         for n1 in nums1:
#             i2 = bisect.bisect_left(nums2, n1)
#             if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
#                 result.add(n1)
#         return result