class Solution: 
  def searchInsert(self, nums: list[int], target: int)-> int :

    left, right = 0, len(nums) - 1 # we have to take 2 pointers left and right. left start at index 0, and right = len(nums)-1
    while left <= right :
      mid = (left + right) // 2  # finding mid for binary search

      if target == nums[mid] :
        return mid  # if its equal at first chance means we found the value
      if target > nums[mid] : # if greater than we have to move our left pointer to right 
        left = mid + 1  # shifting mid pointer to right
      else:   # if its not greater than mid pointer
        right = mid - 1 # shift the right pointer to left
    
    return left  # we have to return the left pointer to khnow the index 
sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 5))  # Output: 2
print(sol.searchInsert([1, 3, 5, 6], 2))  # Output: 1
print(sol.searchInsert([1, 3, 5, 6], 7))  # Output: 4
