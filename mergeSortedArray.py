class Solution:
  def merge(self, nums1: list[int], m:int, nums2: list[int], n: int) -> None:
    p1 = m-1 # pointer (at last)  for nums1 real element
    p2 = n-1 # pointer (at last) for nums2
    p = m + n -1 # pointer for empty space placement of nums1

    while p1 >= 0 and p2 >= 0 :  #  if both pointer has values
      if nums1[p1] > nums2[p2] :
        nums1[p] = nums1[p1]  # if greater then add the value at last
        p1 -= 1 #decrement the pointer
      else :  # if not greater then  put the nums2  big value at the nums[1] empty space 
        nums1[p] = nums2[p2]
        p2 -= 1
      p -= 1 # decrement the pointer from the last 

    # fter the loop, if there are any elements left in nums2, we need to copy them into nums1
    while p2 >= 0 :  # if nums2 has more value
      nums1[p] = nums2[p2]
      p2 -=1 # decreasing the pointer of p2 
      p -=1  # decreasing the pointer of nums1 emptyspace elemnet

sol = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
sol.merge(nums1, 3, nums2, 3)
print(nums1)  # as we put the value of nums2 in nums1 ...

 
