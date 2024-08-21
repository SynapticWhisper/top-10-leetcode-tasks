class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        index = 0
        result = 0

        while index < len(s):
            num = s[index]

            if index + 1 < len(s):
                next_num = s[index+1]
                next_num = values.get(next_num)
            else:
                next_num = None
            
            num = values.get(num)

            if next_num and next_num > num:
                result += next_num - num
                index += 2
            else:
                result += num
                index += 1
        return result
