from tqdm import tqdm

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        result = False
        assert num>=1 & num<=10**8, 'input number should be between 1 and a million'
        n = 0
        for i in tqdm(range(int(num/2))):
            n += num/(i+2)+(i+2) if num%(i+2)==0 else 0
            if n>num:
                return False
        if n == num:
            return True
        else:
            return False


sol = Solution()
sol2 = sol.checkPerfectNumber(496)
print(sol2)
