from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start: int = 0
        end: int = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        
        return -1