class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # heapq 모듈
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
            
        for _ in range(1, k):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)
    
        
#         # 1. heapify 사용    
#         print(nums)
        
#         heapq.heapify(nums)
        
#         print(nums)
        
#         for _ in range(len(nums) - k):
#             heapq.heappop(nums)
            
#         return heapq.heappop(nums)
        
#         # 2. heapq의 nlargest 사용
        
#         # k번째 큰 값이 가장 큰 값부터 순서대로 리턴됨. 
#         return heapq.nlargest(k, nums)[-1]
    