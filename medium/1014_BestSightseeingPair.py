class Solution:
    def maxScoreSightseeingPair(self, values: 'list[int]') -> int:
        valueLen = len(values)

        assert valueLen>=2 and valueLen<=5*10**4, 'the length of values should be between 2 and 50000'
        
        maxValue = 0
        maxValueSpot = 0
        secondValue = 0
        secondValueSpot = 0

        for i in range(valueLen):
            val = values[i]
            assert val>=1 and val<=1000, f'{val} in values should be between 1 and 1000'
            if val > maxValue:
                maxValue = val
                maxValueSpot = i
            elif val>secondValue:
                secondValue = val
                secondValueSpot = i
        
        for i in range(abs(maxValueSpot-secondValueSpot)):
            pass

            




sol = Solution()
test = [1,2,3]
res = sol.maxScoreSightseeingPair(test)

print(res)