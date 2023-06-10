class Solution:
    def reverseString(self, s) -> None:
        sl = len(s)
        assert sl>=1 and sl<=10**5, 'the length of input array should be between 1 and 100000'
        for i in range(int(sl/2)):
            cache = s[i]
            s[i] = s[-i-1]
            s[-1-i] = cache

        return s

sol = Solution()
test = [1,2,3,4,5]
res = sol.reverseString(test)

print(test)