from tqdm import trange

class Solution:
    def generateParenthesis(self, n):
        assert n>=1 and n<=8, 'input n should be between 1 and 8'

        resultList = []
        resultnumList = []

        for i in trange(2**(2*n)-2):
            combine = bin(i+1)[2:]
            combine = f'{int(combine):016d}'
            combine = combine[int(16-2*n):]
            if combine.count('1')!=n:
                continue
            invalid = 0
            res = ''
            for j in combine:
                if j == '0':
                    invalid += 1
                    res += '('
                elif j == '1':
                    invalid -= 1
                    res += ')'
                if invalid<0:
                    res = ''
                    break
            if res:
                resultList.append(res)
                resultnumList.append(combine)

        return resultList, resultnumList

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
    
sol = Solution()
gen, gen2 = sol.generateParenthesis(8)
print(gen)
print(gen2)
