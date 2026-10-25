class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        memo = [-1] * (n + 1)
        def dp(n):
            if n <= 2:
                return n
            
            # If already calculated, return the cached result
            if memo[n] != -1:
                return memo[n]
            
            # Compute and store the result in the memo array
            memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]
        return dp(n)