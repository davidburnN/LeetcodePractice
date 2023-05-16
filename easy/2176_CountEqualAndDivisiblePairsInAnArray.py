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

        divList = []
        divNumList = []
        pairs = 0
        for i in range(0, numsl, k):
            n = nums[i]
            if n not in divList:
                divList.append(n)
                divNumList.append(1)
            else:
                divNumList[divList.index(n)] += 1
                

            nTotal = -1
            for j in range(numsl):
                if n == nums[j]:
                    nTotal += 1
            pairs += nTotal  
            print(nTotal)
        print(divList)
        print(divNumList)
        for i in divNumList:
            pairs -= counts(i)
        return int(pairs) 

sol = Solution()
pairs = sol.countPairs([10,2,3,4,9,6,3,10,3,6,3,9,1], 4)
print(pairs)