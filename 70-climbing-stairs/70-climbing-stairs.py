class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        
#         # 1. simillar fibonach
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        # 2. DP
        
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]