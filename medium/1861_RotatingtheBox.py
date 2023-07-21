class Solution:
    def rotateTheBox(self, box: 'List[List[str]]') -> 'List[List[str]]':
        xl, yl = 0, 0
        stoneArr = []
        stoneN = 0
        for i in box:
            xl = 0
            for j in i:
                if j == '#':
                    stoneArr.append([yl, xl])
                    stoneN += 1
                xl += 1
            yl += 1

        for i in range(stoneN):
            i = stoneN - i - 1
            y = stoneArr[i][0]
            x = stoneArr[i][1]
            for xx in range(xl-x-1):
                if box[y][x+xx+1] == '.':
                    box[y][x+xx+1] = '#'
                    box[y][x+xx] = '.' 
                else:
                    break  
        
        boxFinal = []

        for y in range(xl):
            boxFinal.append([])
            for x in range(yl):
                boxFinal[y].append(box[yl-x-1][y])

        return boxFinal


box1 = [["#",".","*","."],
              ["#","#","*","."]]
box2 = [["#","#","#",".","#","."]]
sol = Solution()
res = sol.rotateTheBox(box1)
print(res)
