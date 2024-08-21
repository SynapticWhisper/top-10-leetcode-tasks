class Solution:
    # using the str it is too easy, so I dont want to use it
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
    
        number = 0
        tmp = x

        maximum = 10
        while x % maximum != x:
            maximum *= 10
        maximum //= 10

        while tmp > 9:
            value = tmp % 10
            number += value * maximum
            maximum //= 10
            tmp //= 10
        number += tmp

        return number == x
