'''
first: ss: can use one such set: then iterate on t until you find an element not in ss. time, space: O(n), O(26)
can use an integer instead as the set for t. time, space: O(n), O(1)

s : a
t : aa
tcounter : a:1

'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tcounter = Counter(t)
        for el in s:
            tcounter[el] -= 1
        for let, count in tcounter.items():
            if count == 1:
                return let
        assert Exception('no added element')
        
        

        # vector = 0
        # for el in s:
        #     mask = 1 << (ord(el) - ord('a'))
        #     vector |= mask
        # for el in t:
        #     mask = 1 << (ord(el) - ord('a'))
        #     if vector & mask == 0:
        #         return el
        # assert Exception('no added element')