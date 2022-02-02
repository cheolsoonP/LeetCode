class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 파이썬은 최소 힙
        heap = []
        
        
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
        
        print(heap)
        result = []
        
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x,y))
        return result