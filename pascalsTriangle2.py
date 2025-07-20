class Solution:
  def getRow(self, rowIndex: int) -> list[int]:
    if rowIndex == 0:
      return [1]  # 0th row is always one
    
    row = [1]  # because even the 0th row has a value — it's [1].

    for i in range(1, rowIndex + 1):  # Repeat this process until we build up to the rowIndex-th row
      new_row = [1]  # every row starts with 1
      for j in range(1, len(row)):  # It adds up two numbers from the previous row.
        new_row.append(row[j - 1] + row[j])  # Adds two adjacent numbers from the previous row 
      new_row.append(1)  # every row ends with [1]
      row = new_row  # Update current row

    return row
sol = Solution()
print(sol.getRow(2))  # Output: [1, 3, 3, 1]
