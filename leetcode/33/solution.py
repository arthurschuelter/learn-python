# 33. Search in Rotated Sorted Array

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        def binarySearch(l: int, r: int):
            mid = l + ((r - l) // 2)

            if target == nums[l]:
                return l
            if target == nums[r]:
                return r 
            if target == nums[mid]:
                return mid
            if l >= r:
                return -1

            # print(f"l: {l} | r: {r} | target: {target} | mid: {mid} | nums[mid]: {nums[mid]} | target == nums[mid]: {target == nums[mid]}")
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    return binarySearch(mid+1, r)
                else:
                    return binarySearch(l, mid)
            else:
                if target < nums[mid] or target > nums[r]:
                    return binarySearch(l, mid)
                else:
                    return binarySearch(mid+1, r)

        return binarySearch(l, r)