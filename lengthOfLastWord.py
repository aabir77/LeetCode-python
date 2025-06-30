class Solution:
   def lengthOfLastWord(self, s:str)-> int:
      s = s.rstrip()  # Remove trailing spaces from the end
      length = 0  # setting a counter

      for i in range(len(s) - 1 ,-1,-1) :    #range(start, stop, step).. stop(-1) menas when it check from backward it will check untill 0.
                                            # step(-1).. means it will reverse check every 1 step at a time
        if s[i] == ' ' : # If space found, stop counting
           break 
        length += 1 # Count characters in last word
      return length
   
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("luffy is still joyboy"))