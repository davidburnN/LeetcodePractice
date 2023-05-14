from tqdm import tqdm

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        result = False
        assert num>=1 & num<=10**8, 'input number should be between 1 and a million'
        n = 1
        factorList = [1]
        for i in tqdm(range(int(num/2))):
            if (num%(i+2)==0):
                n += (i+2)
            if n>num:
                return result
        if n == num:
            return True
        else:
            return False


sol = Solution()
#33550336
sol2 = sol.checkPerfectNumber(99999991)
print(sol2)