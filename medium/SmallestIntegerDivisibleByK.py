class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        kStr = f'{k}'
        kStrLen = len(kStr)
        nStart = int(f'{"1"*kStrLen}')
        remainder = nStart%k
        remainderList = [remainder]
        if remainder == 0:
            return kStrLen
        for i in range(k):
            remainder = (remainder*10+1)%k
            if remainder == 0:
                return int(f'{"1"*(kStrLen+1)}')
            elif remainder in remainderList:
                return -1
            else:
                kStrLen += 1
                remainderList.append(remainder)
        return -1
    
sol = Solution()
testn = 13
N = sol.smallestRepunitDivByK(testn)
print(N)
print(N%testn)
            




sol = Solution()
# print(sol.smallestRepunitDivByK(12357))