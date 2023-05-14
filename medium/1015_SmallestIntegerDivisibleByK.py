class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        if k == 1:
            return 1
        for i in range(k):
            remainder = (remainder*10+1)%k
            if remainder == 0:
                return i+1
        return -1
            
    
sol = Solution()
testn = 19
N = sol.smallestRepunitDivByK(testn)
print(N)
            




sol = Solution()
# print(sol.smallestRepunitDivByK(12357))