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
    
    def countPairs_vial(self, nums, k) -> int:
        numsl = len(nums)
        nums = np.array(nums)
        assert numsl>=1 and numsl<=100, 'length of array should be between 1 and 100.'
        assert (nums>=1).all() and (nums<=100).all(), 'integer in array should be between 1 and 100.'
        assert k>=1 and k<=100, 'k should be between 1 and 100.'
        
        pairs = 0
        for i in range(numsl):
            n = nums[i]
            for j in range(numsl-i-1):
                if (n == nums[i+j+1]) and ((i*(i+j+1))%k==0):
                    pairs += 1
        return pairs

sol = Solution()
pairs = sol.countPairs_vial([10, 2, 3, 4, 9, 6, 3,10, 3, 6, 3, 9, 1], 4)
# pairs = sol.countPairs_vi([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12], 4)
print(pairs)
print((5*(9))%4==0)