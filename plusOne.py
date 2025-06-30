class Solution:
  def plusOne(self, digits: list[int])-> list[int]:

    for i in range(len(digits) - 1, -1 , -1 ) : #range(start, stop, step).. stop(-1) menas when it check from backward it will check untill 0.
                                            # step(-1).. means it will reverse check every 1 step at a time
      if digits[i] < 9:  # if its less then 9 then we can add 1 with it
        digits[i] += 1
        return digits # after adding return the whole digits 
      digits[i] = 0 # if its 9, then we have to put 0 in digits[i]. and carry the one 

    return [1] + digits  #  if ALL digits are 9, none of the if digits[i] < 9: will ever be true.if all values are [9,9,9] then add 1 with it,add carry 1 at the front
        
    
sol = Solution()
print(sol.plusOne([1, 2, 3]))
print(sol.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]