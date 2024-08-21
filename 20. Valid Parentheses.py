class Solution:
    def isValid(self, s: str) -> bool:
        queue = []

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for item in s:
            if item in pairs:
                queue.append(item)
            else:
                if queue:
                    pair = queue.pop()
                    if pairs.get(pair) != item:
                        return False
                else:
                    return False
        return True if not queue else False
