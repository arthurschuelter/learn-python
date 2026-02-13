from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [-1] * n
        suffix = [-1] * n

        cur_max = -1
        for i in range(n - 1, -1, -1):
            if height[i] > cur_max:
                cur_max = height[i]
            suffix[i] = cur_max

        cur_max = -1
        for i in range(0, n):
            if height[i] > cur_max:
                cur_max = height[i]
            prefix[i] = cur_max

        water = 0
        for i in range(n):
            cur_water = min(prefix[i], suffix[i]) - height[i]
            if cur_water > 0:
                water += cur_water

        return water