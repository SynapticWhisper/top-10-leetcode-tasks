from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = dict()
        for index, item in enumerate(nums):
            value: list = indexed.get(item, [])
            value.append(index)
            indexed[item] = value
        
        for i, n in enumerate(nums):
            value: int = target - n
            x: list | None = indexed.get(value, None)
            if x is None:
                continue
            else:
                if value == n and len(x) >= 2:
                    return x[:2]
                elif value == n and len(x) < 2:
                    continue
                else:
                    return [i, x[0]]
