from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up dp(constant space)
        n = len(cost)
        a, b = 0, 0 
        for i in range(2, n + 1):
            a, b = b, min(cost[i - 2] + a, cost[i - 1] + b)  

        return b
    

sol = Solution()
print(sol.minCostClimbingStairs([10,15,20]))