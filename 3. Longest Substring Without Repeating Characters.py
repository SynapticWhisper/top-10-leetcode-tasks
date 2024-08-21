class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1
        
        sub_max = 0

        for i in range(len(s)):
            values: set = set()
            values.add(s[i])
            for letter in s[i+1:]:
                if letter in values:
                    break
                values.add(letter)
            sub_max = max(sub_max, len(values))
        return sub_max
