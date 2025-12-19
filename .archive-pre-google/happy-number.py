class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        key thing here is if you cycle back to a number 
        you have seen, then you return False. but if you
        hit 1 first (as a digit sum), then return true
        as far as the 100 one. we actaully dont need squares
        oh wait we do, to progress.
        use modulo to get the squares for successive digits
        19
        have {19 82 100}
        n 82
        '''
        have=set()
        while n not in have:
            have.add(n)
            nn=0
            while n:
                dig=n%10
                n//=10
                nn+=dig*dig
            n=nn
            if n==1:
                return True
        return False
