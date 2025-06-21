class Solution: 
  def longestCommonPrefix(self, strs: list[str]) -> str :

    if not strs : 
     return ""
    
    prefix = strs[0] # Let's start with the first word as the possible common prefix str[0] = flower
    for word in strs[1:]: # starts wtih each word in the string expect the first word (flower)
      while not word.startswith(prefix):
        prefix = prefix[:-1] # cut the last letter of the word
        if not prefix: 
          return "" # if not start with prefix return empty 
    return prefix
  
sol = Solution()
print(sol.longestCommonPrefix(["dog","racecar","car"]))
