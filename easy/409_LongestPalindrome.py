class Solution:
    def longestPalindrome(self, s: str) -> int:
        sl = len(s)
        assert sl>=1 and sl<=2000, 'the length of input string should be between 1 and 2000'

        letterN = {}
        for i in s:
            letterN[i] = 0

        for i in s:
            letterN[i] += 1

        ifOne = 0
        maxPal = 0
        for i in letterN:
            if letterN[i]%2==1:
                ifOne = 1
            maxPal += int(letterN/2)

        return maxPal+ifOne


test = {'a': 2, 'b': 3, 'c': 1}
print(test)
print(len(test))
for i in test:
    print(i, ' ', test[i])



