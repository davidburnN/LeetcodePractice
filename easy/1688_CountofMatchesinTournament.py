class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        else:
            if n%2 == 0:
                matches = n/2
                return int(matches + self.numberOfMatches(matches))
            else:
                matches = (n-1)/2
                return int(matches + 1 + self.numberOfMatches(matches))
    

sol = Solution()
n = 14
nofmatch = sol.numberOfMatches(n)
print(nofmatch)
