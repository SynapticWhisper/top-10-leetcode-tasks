from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed: dict = dict()

        for index, number in enumerate(nums):
            number_indexes: list = indexed.get(number, [])
            number_indexes.append(index)
            indexed[number] = number_indexes
        
        for index, number in enumerate(nums):
            target_num: int = target - number
            number_indexes: list | None = indexed.get(target_num, None)
            if number_indexes is None:
                continue
            else:
                if target_num == number and len(number_indexes) >= 2:
                    return number_indexes[:2]
                elif target_num == number and len(number_indexes) < 2:
                    continue
                else:
                    return [index, number_indexes[0]]
