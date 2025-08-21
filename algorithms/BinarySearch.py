# Solution for Binary search problem for geeks for geeks
"""
Question:

Given a sorted array arr[] and an integer k, find the position(0-based indexing) at which k is present in the array using binary search. If k doesn't exist in arr[] return -1. 

Note: If multiple occurrences are there, please return the smallest index.

"""
class Solution:
    def binarysearch(self, arr, k):

        # Handle an edge case of not in an arr
        if not arr:
            return -1
        
        # detect sort order first
        sort_order = self.detect_sort_order(arr)
        if sort_order == 'ascending':
            return self.binary_search_asc(arr, k)
        elif sort_order == 'descending':
            return self.binary_search_desc(arr, k)
        else: # Unsorted cases go with linear search
            return self.linear_search(arr, k)
        
    def detect_sort_order(self, arr):
        if len(arr) <= 1:
            return 'ascending'
        if arr[0] < arr[-1]:
            return 'ascending'
        elif arr[0] > arr[-1]:
            return 'descending'
        else:
            # Checks if all elements are identical
            if all(x == arr[0] for x in arr):
                return 'ascending'
            else:
                return 'unsorted'
    def search_ascending(self, arr, k):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right -left) // 2
            mid_arr = arr[mid]
            if mid_arr == k:
                result = mid
                right = mid -1
            elif mid_arr < k:
                left = mid + 1
            elif mid_arr > k:
                right = mid - 1
        return result
    
    def search_descending(self, arr, k):
        left, right = 0, len(arr) -1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            mid_arr = arr[mid]
            if mid_arr == k:
                result = mid
                left = mid + 1
            elif mid_arr < k:
                right = mid - 1
            elif mid_arr > k:
                left = mid + 1
        return result
    
    def search_linear(self, arr, k):
        i = 0
        while i < len(arr):
            if arr[i] == k:
                return i
            i += 1
        return -1
