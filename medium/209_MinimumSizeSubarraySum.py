class Solution:
    def minSubArrayLen(self, target: int, nums: 'List[int]') -> int:
        currentNum = 0
        subArr = []
        lenSubArr = 0
        avaiLenSubArr = 1000000
        minLenSubArr = 1000000

        for i in nums:
            subArr.append(i)
            currentNum += i
            lenSubArr += 1
            while currentNum >= target:
                avaiLenSubArr = lenSubArr
                delNum = subArr.pop(0)
                currentNum -= delNum
                lenSubArr -= 1
            
            if minLenSubArr >= avaiLenSubArr:
                minLenSubArr = avaiLenSubArr
        if minLenSubArr == 1000000:
            minLenSubArr = 0
        return minLenSubArr

    
sol = Solution()
target = 7
nums = [2,3,1,2,4,3]
res1 = sol.minSubArrayLen(target, nums)
print(res1)




