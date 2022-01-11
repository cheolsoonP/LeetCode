class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. heapq 사용
        
        heap = []
        
        # key - num / value - count
        freq = collections.Counter(nums)
        
        for f in freq:
            # key - count / value - num
            # 힙은 키 순서로 정렬된다.
            # 빈도수 순서로 정렬하기 위해
            heapq.heappush(heap, (-freq[f], f))
            
        top = []
        for _ in range(k):
            top.append(heapq.heappop(heap)[1])
            
        return top
        
#         # 2. simple
#         # "zip, *" 기능 사용
#         return list(zip(*collections.Counter(nums).most_common(k)))[0]
    