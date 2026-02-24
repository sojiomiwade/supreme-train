class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        x = columnNumber
        ans = []
        while x != 0:
            mod = (x-1) % 26
            ans.append(chr(ord('A') + mod))
            x = (x-1) // 26
        return ''.join(reversed(ans))