class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        for i in range(len(xstr) // 2):
            j = len(xstr) - 1 - i
            if xstr[i] != xstr[j]:
                return False
        else:
            return True
