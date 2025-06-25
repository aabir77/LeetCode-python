from typing import List
class Solution:
  def removeElement(self, nums :list[int], val : int) ->int :
    k = 0 # we have to put the new  values in k and return it

    for i in range(len(nums)):
      if nums[i] != val :  # if numbers are not = to val then put k = that num[i]
        nums[k] = nums[i]
        k += 1
    return k 

sol = Solution()
nums = [0,1,2,2,3,0,4,2]
k = sol.removeElement(nums, 2) #  we have called the remove elment fn so, we have to give 2 parameters, an array and value
print("output :", k)
print("nums =", nums[:k] + ['_'] * (len(nums) - k))

