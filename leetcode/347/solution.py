import heapq
from collections import Counter
from typing import List

class Solution:
    # Time:     O(n * log(k))
    # Space:    O(n + k) -> O(n)

    # With Heap:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = Counter(nums)
    #     heap = []

    #     for key, value in counter.items():
    #         if len(heap) < k:
    #             heapq.heappush(heap, (value, key))
    #         else:
    #             heapq.heappushpop(heap, (value, key))

    #     return [h[1] for h in heap]



    # Time:     O(n)
    # Space:    O(n + k) -> O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counter = Counter(nums)
        print(counter)

        for key, value in counter.items():
            freq[value].append(key)
            # print(f"Inserting {key} at freq[{value}]")
            # print(f"freq[{value}] = {freq[value]}")
        
        # print(freq)
        freq = freq[::-1] # Invert it
        # print(freq)
        ans = []
        for f in freq:
            if len(f) == 0:
                continue
            
            ans.extend(f)
            
            if len(ans) == k:
                break

        return ans