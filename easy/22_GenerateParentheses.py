class Solution:
    def generateParenthesis(self, n):
        assert n>=1 and n<=8, 'input n should be between 1 and 8'

        resultList = []

        for i in range(2**n-2):
            combine = bin(i+1)[2:]
            combine = f'{int(combine):016d}'
            combine = combine[int(16-2*n):]
            if combine.count('1')!=n:
                continue




        return resultList

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
    
# sol = Solution()
# gen = sol.generateParenthesis(8)
# print(gen)
test = bin(35)
test = test[2:]
test = int(test)
test = f'{test:08d}'
print(test)
print(test.count('0'))
print(2**16)
