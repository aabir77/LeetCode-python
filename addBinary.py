class Solution:
  def addBinary(self, a:str, b:str)->str:
    i,j =len(a)-1, len(b)-1
    carry = 0
    result=[]
    
    while i >= 0 or j >= 0 or carry :
      digit_a = int(a[i]) if i >= 0 else 0  #Get the digit from string a, or use 0 if there are no more digits left.
      digit_b = int(b[j]) if j >= 0 else 0 # Get the digit from string b, or use 0 if there are no more digits left.

      total = digit_a + digit_b + carry  # Sum of both digits and carry
      result.append(str(total%2))   # Append binary digit (0 or 1)
      carry = total // 2  # update the carry with 0 or 1

      i -= 1  #start adding from lest most value
      j -= 1
    return ''.join(result[::-1])
sol = Solution()
print(sol.addBinary("11", "1"))




