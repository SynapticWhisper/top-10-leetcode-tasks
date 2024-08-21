from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = dict()
        for index, item in enumerate(nums):
            value: list = indexed.get(item, [])
            value.append(index)
            indexed[item] = value
        
        for index, number in enumerate(nums):
            target_num: int = target - number
            indexes: list | None = indexed.get(target_num, None)
            if indexes is None:
                continue
            else:
                if value == indexes and len(indexes) >= 2:
                    return indexes[:2]
                elif value == indexes and len(indexes) < 2:
                    continue
                else:
                    return [index, indexes[0]]
