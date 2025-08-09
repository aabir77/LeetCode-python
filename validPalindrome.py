class Solution:
  def isPalindrome(self, s: str) -> bool:
    #need two pointers to check 
    left = 0
    right = len(s) - 1
    while left < right:   #left is checked before the right
      while left < right and not s[left].isalnum():  #while we check left pointer and string of left pointer is non-alphanumeric we move left pointer one step forward
        left += 1
      while left < right and not s[right].isalnum():  # checking right from the backward
          right -= 1
      if s[left].lower() != s[right].lower(): # make the string of left and right to lowercase and if they are not equal return false
          return False
      left += 1  # after making lower move from left to right & right to left
      right -= 1 
    return True  #If you finished scanning all pairs without returning False, then the string is a palindrome.
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))