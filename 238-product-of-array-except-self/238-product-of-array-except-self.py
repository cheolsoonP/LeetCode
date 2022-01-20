class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        p = 1
        
        # 왼쪽 곱
        for i, num in enumerate(nums):
            results.append(p)
            p = p * num
        p = 1
        
        # 왼쪽 곱에 오른쪽 값 곱하기
        for i in range(len(nums) - 1, 0 - 1, -1):
            results[i] = results[i] * p
            p = p * nums[i]
        
        return results
            