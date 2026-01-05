# 1010
#  111
# 1001
# carry, top, bot, buf
# append into buf
# then reverse buf at the end
#  11
#  11
# 110 <- expected
# a
# m n 2 2
# a   1 1
#   i
#   j
# b   1 1
# carry 3
# buf [0 1 1]
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        i, j = m-1, n-1
        carry, buf = 0, []
        while i>=0 or j>=0 or carry > 0:
            if i>=0:
                carry += int(a[i])
                i -= 1
            if j>=0:
                carry += int(b[j])
                j -= 1
            buf.append(str(carry % 2))
            carry //= 2
        return ''.join(reversed(buf))
