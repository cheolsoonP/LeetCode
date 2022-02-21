class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
#         # 1. DP
#         counts = collections.defaultdict(int)
        
#         for num in nums:
#             if counts[num] == 0:
#                 counts[num] = nums.count(num)
            
#             if counts[num] > len(nums) // 2:
#                 return num
    
    
#         # 2. 분할정복
#         if not nums:
#             return None
#         if len(nums) == 1:
#             return nums[0]
        
        
#         half = len(nums) // 2
        
#         a = self.majorityElement(nums[:half])
#         b = self.majorityElement(nums[half:])
        
        
#         return [b, a][nums.count(a) > half]

    
        # 3. simple 
        # 222222111 -> 2
        return sorted(nums)[len(nums) // 2]