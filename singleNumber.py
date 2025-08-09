class Solution:
  def singleNumber(self, nums:list[int])-> int:
    #  best approach for these constraints is to use bitwise XOR (^)   a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
   result = 0   # We start with 0 because x ^ 0 = x, so the first XOR won’t change the number.
   for num in nums:
     result ^= num      # result = result ^ num---- Pairs of identical numbers will cancel out (become 0)
   return result
  
sol = Solution()
print(sol.singleNumber([4, 1, 2, 1, 2]))