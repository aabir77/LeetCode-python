class Solution:
  def maxProfit(self, prices: list[int])-> int :
    min_price = float('inf') #float('inf') just means a very large number
    max_profit = 0  # initially we make profit 0
    for price in prices :
      if price < min_price :
         min_price = price # if price is less than min price, this will be our new price
      else:    # it will be our max price, so we eill earn price 
        profit = price - min_price  # profit will be difference btw the price we bought today and price at we sell
        max_profit = max(max_profit,profit) # update the best profit

    return max_profit
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))

