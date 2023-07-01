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
    def __init__(self, id):
        self.id = id
        
    def f1(self, x, y):
        return x + y
    
    def f2(self, x, y):
        return x * y
    
    def f3(self, x, y):
        return x + y +1
    
    def f4(self, x, y):
        return x + y +2
        
    def f5(self, x, y):
        return x * y +1
    
    def f6(self, x, y):
        return x + y +3
    
    def f7(self, x, y):
        return x + y +4
    
    def f8(self, x, y):
        return x * y +5
    
    def f9(self, x, y):
        return x + y +6
    
    def func(self):
        match self.id:
            case 1:
                self.f = self.f1
            case 2:
                self.f = self.f2
            case 3:
                self.f = self.f3
            case 4:
                self.f = self.f4
            case 5:
                self.f = self.f5
            case 6:
                self.f = self.f6
            case 7:
                self.f = self.f7
            case 8:
                self.f = self.f8
            case 9:
                self.f = self.f9
            
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> 'List[List[int]]':
        output = []
        cusFunc = CustomFunction(customfunction)
        cusFunc.func()

        for x in range(999):
            for y in range(999):
                if cusFunc.f(x+1, y+1)==z:
                    output.append([x+1, y+1])
        
        return output

sol = Solution()
res = sol.findSolution(3, 10)
# print(res)

for i in range(9):
    print(sol.findSolution(i+1, 10))
