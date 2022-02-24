class Solution:
    
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
#         # 1. brute force
#         if n <= 1:
#             return n
#         return self.fib(n - 1) + self.fib(n - 2)
    
    
#         # 2. top down
#         # 한번만 계산하여 저장해놓기 때문에 빠르다. 
#         if n <= 1:
#             return n
        
#         if self.dp[n]:
#             return self.dp[n]
#         self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
#         return self.dp[n]
        
        
#         # 3. bottom up
#         self.dp[0] = 0
#         self.dp[1] = 1
        
#         for i in range(2, n + 1):
#             self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        
#         return self.dp[n]
        
        
        # 4. saving memory
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
        return x