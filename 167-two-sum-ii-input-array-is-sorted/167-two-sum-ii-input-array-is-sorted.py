class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 1. two pointer
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                # index가 1부터 시작
                return left + 1, right + 1
            
        
        
        