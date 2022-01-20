class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        low = sys.maxsize
        max_profit = -sys.maxsize
                
        for present in prices:
            low = min(present, low)
            max_profit = max(max_profit, present - low)
            
        return max_profit
            
        