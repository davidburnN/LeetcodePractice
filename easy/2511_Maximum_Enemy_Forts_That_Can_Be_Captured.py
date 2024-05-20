class Solution:
    def captureForts(self, forts: list[int]) -> int:
        max_enemys = 0
        enemys = 0
        value = 0
        for fort in forts:
            if fort == value:
                enemys = 0
            value += fort
            if value == 0:
                if max_enemys<enemys:
                    max_enemys = enemys
                enemys = 0
                value += fort
            elif value > 1:
                value = 1
                enemys = 0
            elif value < -1:
                value = -1
                enemys = 0
            else:
                if fort == 0:
                    enemys += 1
            print(f'value: {value}, fort: {fort}, enemys: {enemys}')
        return max_enemys
    
sol = Solution()
forts = [1,0,0,-1,0,0,0,0,1]
forts2 = [0,0,1,-1]
print(sol.captureForts(forts))

