import numpy as np
class Solution:
    def countPairs(self, nums, k) -> int:
        def counts(number):
            return number*(number-1)/2
        
        numsl = len(nums)
        nums = np.array(nums)
        assert numsl>=1 and numsl<=100, 'length of array should be between 1 and 100.'
        assert (nums>=1).all() and (nums<=100).all(), 'integer in array should be between 1 and 100.'
        assert k>=1 and k<=100, 'k should be between 1 and 100.'

        divlist = []
        pairs = 0
        for i in range(0, numsl, k):
            n = nums[i]
            if n not in divlist:
                divlist.append(n)
            else:
                continue

            nTotal = 0
            for j in range(numsl):
                if n == nums[j]:
                    nTotal += 1
            pairs += counts(nTotal)  
        return pairs

sol = Solution()
pairs = sol.countPairs([5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3], 7)
print(pairs)