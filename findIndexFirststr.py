from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0  # If needle is empty, return 0 by definition

        for i in range(len(haystack) - len(needle) + 1):  # Loop through valid start indices
            match = True

            for j in range(len(needle)):  # Compare each character of needle
                if haystack[i + j] != needle[j]:  # If mismatch found
                    match = False
                    break  # Exit early if mismatch

            if match:
                return i  # Return starting index if full match found

        return -1  # If no match found

sol = Solution()
print(sol.strStr("sadbutsad", needle = "sad"))  # 0
print(sol.strStr("leetcode", needle = "leeto")) # -1
        


