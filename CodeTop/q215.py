from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hh = []
        heapq.heapify(hh)
        for num in nums:
            heapq.heappush(hh,num)
            if len(hh) > k:
                heapq.heappop(hh)
        return heapq.heappop(hh)

print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))