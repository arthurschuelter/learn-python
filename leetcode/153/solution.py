from typing import List
class Solution:
    # Time:     O(n)
    # Space:    O(1)
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        return self.binarySearch(nums, l, r)

    def binarySearch(self, nums: List[int], l: int, r: int) -> int:
        if l >= r:
            return nums[l]

        n = len(nums)   
        mid = (l + r) // 2

        # print(f"l: {l} | r: {r} | mid: {mid} | nums[mid]: {nums[mid]}")

        if nums[(mid + 1) % n] < nums[mid]:
            return nums[(mid + 1) % n]
        elif nums[mid] > nums[r]:
            return self.binarySearch(nums, mid+1, r)
        else:
            return self.binarySearch(nums, l, mid)
        
        