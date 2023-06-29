import numpy as np

class Solution:
    def maxMatrixSum(self, matrix: 'List[List[int]]') -> int:
        minAbs = 100000
        arrNeg = []
        sumMatr = 0
        nNeg = 0
        for row in matrix:
            for element in row:
                if minAbs>abs(element):
                    minAbs = abs(element)
                if element<0:
                    nNeg += 1
                    arrNeg.append(-element)
                else:
                    sumMatr += element

        if nNeg%2 == 0:
            return sumMatr + sum(arrNeg)
        else:
            return sumMatr + sum(arrNeg) - 2 * minAbs

sol = Solution()
matrix = [[1,-1],[-1,1]]
res = sol.maxMatrixSum(matrix)

print(res)
