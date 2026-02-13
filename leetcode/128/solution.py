from typing import List
class Solution:
    # Time: O(n)
    # Space: O(n + n) => O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) # O(1) lookups
        max_seq = 0

        for n in nums:
            if (len(s) == 0): return max_seq
            cur_seq = 1

            # For nums = [5,4,3,2,1]
            # n: 5, checks if 4 exists
            #   True:   There is a sequence that includes 5, so don't start counting up. 
            #           The sequence may already be calculated or will be calculated in the future.
            #           In this case it will be calculated in the future, when n=1.
            #           Update max_seq just to be sure.
            #   False:  It is a new sequence, start counting up.
            if n-1 in s:
                max_seq = max(cur_seq, max_seq)
                continue
            
            next_n = n+1
            while next_n in s:
                s.remove(next_n) # Remove to don't lookup again in the future
                cur_seq += 1
                next_n += 1

            max_seq = max(cur_seq, max_seq)

        return max_seq