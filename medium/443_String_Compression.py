class Solution:
    def compress(self, chars: 'List[str]') -> int:
        arrayLen = 0
        s = ''
        sLen = 0
        newArray = []
        newArrayLen = 0
        chars.append('end')
        for i in chars:
            if i != s:
                if sLen > 1 and sLen < 10:
                    newArray.append(f'{sLen}')
                    newArrayLen += 1
                elif sLen > 9:
                    for j in f'{sLen}':
                        newArray.append(j)
                        newArrayLen += 1
                if i == 'end':
                    break
                newArray.append(i)
                newArrayLen += 1
                s = i
                sLen = 1
                    
            else:
                sLen += 1
            arrayLen += 1
        for i in newArray:
            chars.append(i)
        for i in range(arrayLen+1):
            chars.pop(0)
        return chars


chars = ['a', 'a', 'b', 'b', 'c' ,'c' ,'c']
chars2 = ["a"]
chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
sol = Solution()
res = sol.compress(chars)
print(res)