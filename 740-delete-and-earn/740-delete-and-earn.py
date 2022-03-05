class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, prev, curr = Counter(nums), 0, 0
    
        for value in range(max(points.keys()) + 1):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr