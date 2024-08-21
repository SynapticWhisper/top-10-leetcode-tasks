from functools import reduce
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs, key=len)

        prefix = []

        for index, letter in enumerate(word):
            is_common = reduce(lambda x, y: x & y, map(lambda x: x[index] == letter, strs))
            if is_common:
                prefix.append(letter)
            else:
                break
        
        return "".join(prefix)