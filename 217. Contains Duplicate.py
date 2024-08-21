from typing import List

class Solution:
    # There are many ways to solve this task
    def containsDuplicate_1(self, nums: List[int]) -> bool:
        # First way and the easyest one, in my mind, is to check length of list and set
        return len(nums) != len(set(nums))
    
    def containsDuplicate_2(self, nums: List[int]) -> bool:
        # Second one is adding unique numbers to set
        values: set = set()
        for num in nums:
            if num in values:
                return True
            values.add(num)
        return False
    
    def containsDuplicate_3(self, nums: List[int]) -> bool:
        # We also can use dict to solve this task
        values: dict = {}
        for num in nums:
            if values.get(num, False):
                return True
            values[num] = True
        return False
    
    # At all there is no difference between second and third solutions, couse `num in set`is O(1)
    # and `dict.get(num, False)` is O(1)
