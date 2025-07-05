class Solution:
  def mySqrt(self, x: int)-> int:
    left,right, = 0,x
    ans = 0
    while left<=right :
      mid = (left + right) // 2  #checking mid of 9
      if mid * mid == x :  #3 # Perfect square case
        return mid # if mid is equal to actual mid then return the value
      elif mid * mid < x :
        ans = mid
        left = mid + 1
      elif mid * mid > x :
         right = mid - 1  # 2--> (2+3)//2 == 2-----> mid = 4<9 == 3
    return ans
  
sol = Solution()
print(sol.mySqrt(9)) 