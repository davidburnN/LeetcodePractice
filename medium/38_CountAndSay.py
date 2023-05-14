from tqdm import tqdm, trange

class Solution:
    def countAndSay(self, n: int) -> str:
        assert n>=1 & n<=30, 'input number should be between 1 and 30'
        saying = '1'

        for i in range(n-1):
            saying_mid = ''
            saylen = len(saying)
            n = 1
            for j in range(saylen):
                if j == saylen-1:
                    saying_mid += f'{n}{saying[j]}'
                    n = 1
                    break
                if saying[j+1] == saying[j]:
                    n += 1
                else:
                    saying_mid += f'{n}{saying[j]}'
                    n = 1
            saying = saying_mid
        return saying


sol = Solution()
for i in range(10):
    say = sol.countAndSay(i+1)
    print(i+1, ' ', say)