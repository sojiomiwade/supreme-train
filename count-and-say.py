class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        12111333
        x
        for each x in countAndSay(n-1): 
            ans = count(x)+x
        return ans
        n=5=>
        1211 => 11_12_21 <--- ans
        c(5)-c(4)-c(3)-c(2)-"1"
        c2:
            1
            i
            ans=11
        c3: 
            11
            i
            count=2
            ans=21
        c4:
            21
            i
            count=1
            i 
            5|67890
            count = 2

            i
            0
            i=0
            count=0
            i = 7
            7-2+1
        '''
        if n==1:
            return "1"
        s=self.countAndSay(n-1)
        i=0
        ans=''
        while i<len(s):
            count=0
            while i+1<len(s) and s[i]==s[i+1]:
                count+=1
                i+=1
            ans+=str(count+1)+s[i-count]
            i+=1
        return ans
