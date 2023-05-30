class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        sl = len(s)
        assert sl>=1 and sl<=100, 'length of input string should be between 1 and 100'
        
        onelen = 0
        onelenList = []
        zerolen = 0
        zerolenList = []

        for i in s:
            i = int(i)
            if i == 1:
                onelen += 1
                zerolenList.append(zerolen)
                zerolen = 0
            elif i == 0:
                zerolen += 1
                onelenList.append(onelen)
                onelen = 0
            else:
                assert i==0 or i==1, f'{i} in string is not 0 or 1'

        if onelen!=0:
            onelenList.append(onelen)
        if zerolen!=0:
            zerolenList.append(zerolen)

        print(max(onelenList), max(zerolenList))

        if max(onelenList)>max(zerolenList):
            return True
        else:
            return False
        
sol = Solution()
s = '111000'
res = sol.checkZeroOnes(s)
print(res)
    

