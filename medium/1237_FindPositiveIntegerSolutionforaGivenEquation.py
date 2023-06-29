"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class CustomFunction():
    def f(self, x, y):
        return x + y
    
    def f(self, x, y):
        return x * y

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> 'List[List[int]]':
        output = []
        custFunc = CustomFunction()
        func = custFunc(customfunction)
        for i in range(z):
            for j in range(z):
                if func(i, j) == z:
                    output.append([i, j])
        return output

sol = Solution()
res = sol.findSolution(1, 5)
print(res)