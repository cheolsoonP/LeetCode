class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
#         # 1. two pointer
#         left, right = 0, len(numbers) - 1
#         while not left == right:
#             if numbers[left] + numbers[right] < target:
#                 left += 1
#             elif numbers[left] + numbers[right] > target:
#                 right -= 1
#             else:
#                 # index가 1부터 시작
#                 return left + 1, right + 1
            
            
#         # 2. 이진 검색
#         for k, v in enumerate(numbers):
#             left, right = k + 1, len(numbers) - 1
#             expected = target - v
#             # 이진 검색으로 나머지 값 판별
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if numbers[mid] < expected:
#                     left = mid + 1
#                 elif numbers[mid] > expected:
#                     right = mid - 1
#                 else:
#                     return k + 1, mid + 1
                
        # 3. bisect 모듈
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1
        