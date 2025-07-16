class Solution:
  def generate(self, numRows: int)-> list[list[int]] :
    if numRows == 0 : #if asks for o rows it will return an empty list[]  
     return []
    triangle = [[1]] # initialize pascals triangle with [1] always
    if numRows == 1 : # if asked for 1 rows we are already done by initializing
      return triangle  #  return the triangle
    for i in range(1, numRows): #We already added the 1st row, now we loop from row 2 to numRows
      prev_row = triangle[i-1] #look at the previous row to calculate the current one.
      row = [1] #every row starts with 1

      # Fill in the middle values
      for j in range(1,len(prev_row)) : # as first value of each row is 1 and from thier go to end values of that row
        row.append(prev_row[j-1] + prev_row[j]) # ADDING THE MIDDLE 2 VALUES OF PREVISOUS ROW TO GET THE NEXT ROW VALUE
      row.append(1) # end the row wirh 1
      triangle.append(row) # add the row to the triangle
    return triangle
  
sol = Solution()
print(sol.generate(5))
    
    

