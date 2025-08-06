3# Code to find the largest number and second largest in a list

from typing import Optional, List


class LargestNum:
    def __init__(self):
        self.largest_num = float('-inf')

    def largest(self, nums: List[int]) -> int:
        max = self.largest_num
        for num in nums:
            if num > max:
                max = num
        return max
    
    def second_largest(self, nums: List[int]) -> int:
        max1 = float('-inf')
        max2 = float('-inf')

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2 and num != max1:   # Ensure that the maximum number is not counted as the second largest.
                max2 = num
        return max2 if max2 != float('-inf') else None

print(LargestNum().largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(LargestNum().second_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(LargestNum().second_largest([5]))         # ➜ None (only one item)
print(LargestNum().second_largest([5, 5, 5]))    # ➜ None (no distinct 2nd largest)
print(LargestNum().second_largest([-5, -2, -10])) # ➜ -5 (second largest negative)
print(LargestNum().second_largest([10, 9, 10]))   # ➜ 9 (duplicate max)
