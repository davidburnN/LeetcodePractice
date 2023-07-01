class Solution:
    def maximizeSum(self, nums: 'List[int]', k: int) -> int:
        maxN = 0
        for i in nums:
            if i > maxN:
                maxN = i
        return int((maxN+maxN+k-1)*k/2)