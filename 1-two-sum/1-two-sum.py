class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
#         # 1. 
#         for i in range(len(nums)):
#             for j in range(i +1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
        
        
        # 2. 
        
        dic = collections.defaultdict(list)
        
        
        # num : index
        for i, num in enumerate(nums):
            dic[num] = i
        
    
        for i, num in enumerate(nums):
            if target - num in dic and i != dic[target - num]:
                return [i, dic[target - num]]

