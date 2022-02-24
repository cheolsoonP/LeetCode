class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # # 1. memoization 
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        # return max(nums)
    
    
        # 2. 카데인 
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
            
        return best_sum