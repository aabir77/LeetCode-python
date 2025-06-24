from typing import List
class Solution:
 def removeDuplicates(self, nums : list[int]) -> int :
  if not nums :  # if the list is empty it will return o
   return 0
  i = 1  # first value is always unique, and i=  is the place where we will write the unique values

  for j in range(1, len(nums)) :
    if nums[j] != nums[j-1] :     # not equal mean unique value
      nums[i] = nums[j]
      i += 1  # increase the value of i 

  return i
 
sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(nums)
print("output:", k)  # print how many unique numbers 
print("nums = ", nums[:k] + ['_'] * (len(nums) - k)) # [:k] print the first unique elements,,   
                                                     #  ['_'] * (len(nums) - k) — fills the rest with underscores _ to show those positions are ignored.  







  
 