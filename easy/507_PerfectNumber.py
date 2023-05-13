from tqdm import tqdm

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        result = False
        assert num>=1 & num<=10**8, 'input number should be between 1 and a million'
        
        factorList = [1]
        for i in tqdm(range(int(num/2))):
            if (num%(i+2)==0) & ((i+2) not in factorList):
                factorList.append(i+2)
                factorList.append(num/(i+2))
            if sum(factorList)>num:
                return result
        if sum(factorList) == num:
            return True
        else:
            return False


sol = Solution()
sol2 = sol.checkPerfectNumber(33550336)
print(sol2)