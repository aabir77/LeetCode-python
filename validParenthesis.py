from inspect import stack


class Solution:
  def isValid(self, s: str) ->bool:
    #stack will store opening brackets we see. 
    stack = [] #track opening bracket
    mapping = {  # mapping tells us what each closing bracket needs to match.Example: if we see ")", it must match "(" on top of the stack.
      ')' : '(', ']' : '[', '}' : '{', 
    }
    for char in s: #go through every charecter input
      if char in mapping.values(): # if first char is an opening
        stack.append(char) # push onto the stack

      elif char in mapping: # if its a closing bracket
        if not stack or stack[-1] != mapping[char]: # if stacj is not empty OR first value is not equal to charecters we pushed in to the stack then return flase
          return False # brackets not matched
        stack.pop() # if matched then pop it 

    return not stack #if the stacks were empty and all charecters match means it's correct and it will return True.
      
sol = Solution()
print(sol.isValid('([])'))
        

